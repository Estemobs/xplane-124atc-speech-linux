import time
import subprocess
import re
import os

# --- Configuration ---
# Remplacez ceci par le chemin réel de votre fichier log.txt de X-Plane
XPLANE_LOG_PATH = '/home/estemobs/.steam/steam/steamapps/common/X-Plane 11/Log.txt' 

# Mot-clé pour identifier les messages ATC 124th
ATC_KEYWORD = "124thATC"


# --- Fonction pour lire le message avec speech-dispatcher ---
def speak(text):
    print(f"Tentative de lecture : '{text}'")
    try:
        # La commande 'spd-say' est l'interface en ligne de commande pour speech-dispatcher
        subprocess.run(['flite', '-t', text], check=True)
        print("Message lu avec succès.")
    except FileNotFoundError:
        print("Erreur : 'spd-say' n'a pas été trouvé. Assurez-vous que speech-dispatcher est installé et dans votre PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'appel à spd-say : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue lors de la lecture : {e}")

# --- Fonction pour extraire le message ATC ---
def extract_atc_message(log_line):
    # Regex pour capturer tout ce qui suit "Communication: "
    match = re.search(r"Communication:\s*(.*)", log_line)
    if match:
        return match.group(1).strip()
    return None

# --- Surveillance du fichier log (méthode simple sans 'tailer') ---
def follow_log(filepath):
    # Vérifie si le fichier existe
    if not os.path.exists(filepath):
        print(f"Erreur : Le fichier log '{filepath}' n'existe pas. Veuillez vérifier le chemin.")
        return

    print(f"Surveillance du fichier log : {filepath}")
    # Ouvre le fichier en mode lecture et se positionne à la fin
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        f.seek(0, os.SEEK_END)  # Aller à la fin du fichier

        while True:
            line = f.readline()
            if not line:
                # Aucune nouvelle ligne, attendre un peu et réessayer
                time.sleep(0.5) 
                continue
            
            # Traite la ligne si elle contient le mot-clé ATC
            if ATC_KEYWORD in line:
                print(f"Ligne ATC détectée : {line.strip()}")
                message = extract_atc_message(line)
                if message:
                    speak(message)
                else:
                    print("Impossible d'extraire le message ATC de la ligne.")

# --- Point d'entrée du script ---
if __name__ == "__main__":
    try:
        follow_log(XPLANE_LOG_PATH)
    except KeyboardInterrupt:
        print("\nArrêt de la surveillance du log par l'utilisateur.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")