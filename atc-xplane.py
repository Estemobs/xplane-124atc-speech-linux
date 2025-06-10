import time
import subprocess
import re
import os

# --- Configuration ---
# Remplacez ceci par le chemin réel de votre fichier log.txt de X-Plane
XPLANE_LOG_PATH = '/home/estemobs/.steam/steam/steamapps/common/X-Plane 11/Log.txt' 

# Mot-clé pour identifier les messages ATC 124th
ATC_KEYWORD = "124thATC"

# Dictionnaire alphabet phonétique OTAN
PHONETIC_DICT = {
    'A': 'Alpha',   'B': 'Bravo',    'C': 'Charlie', 'D': 'Delta',
    'E': 'Echo',    'F': 'Foxtrot',  'G': 'Golf',    'H': 'Hotel',
    'I': 'India',   'J': 'Juliett',  'K': 'Kilo',    'L': 'Lima',
    'M': 'Mike',    'N': 'November', 'O': 'Oscar',   'P': 'Papa',
    'Q': 'Quebec',  'R': 'Romeo',    'S': 'Sierra',  'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor',   'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee',  'Z': 'Zulu'  
}

def to_phonetic(text):
    # Transforme chaque lettre/chiffre en phonétique, laisse les espaces
    return ' '.join(PHONETIC_DICT.get(char, char) for char in text if char != ' ')

def replace_callsign_with_phonetic(message):
    # Cherche le callsign avant ou après la virgule
    # Exemples : "CFJ 05, turn right heading 036." ou "Turn right heading 036, CFJ 05"
    match = re.search(r'([A-Z]{2,}\s?\d{1,3})[,\.]', message)
    if not match:
        match = re.search(r'[,\.]\s*([A-Z]{2,}\s?\d{1,3})', message)
    if match:
        callsign = match.group(1)
        phonetic = to_phonetic(callsign.replace(' ', ''))
        # Remplace le callsign par sa version phonétique dans le message
        return message.replace(callsign, phonetic)
    return message

# --- Fonction pour lire le message avec speech-dispatcher ---
def speak(text):
    print(f"Tentative de lecture : '{text}'")
    try:
        # Ajoute la conversion phonétique du callsign
        text = replace_callsign_with_phonetic(text)
        subprocess.run(['flite', '-t', text], check=True)
        print("Message lu avec succès.")
    except FileNotFoundError:
        print("Erreur : 'spd-say' n'a pas été trouvé. Assurez-vous que speech-dispatcher est installé.")
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