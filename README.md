# xplane-124atc-speech

Un script Python simple pour lire vocalement les messages ATC du plugin 124thATC de X-Plane 11 directement depuis le fichier `Log.txt`.

---

## Table des matières

-   [Présentation](#présentation)
-   [Fonctionnalités](#fonctionnalités)
-   [Prérequis](#prérequis)
-   [Installation](#installation)
-   [Utilisation](#utilisation)
-   [Configuration](#configuration)
-   [Dépannage](#dépannage)
-   [Contribution](#contribution)
-   [Licence](#licence)

---

## Présentation

Ce script Python est conçu pour améliorer l'expérience de simulation de vol avec X-Plane 11 et le plugin 124thATC. Il surveille en temps réel le fichier `Log.txt` de X-Plane. Lorsqu'un message de communication du 124thATC est détecté, le script extrait le texte et le fait lire par un moteur de synthèse vocale de votre système. Cela vous permet d'entendre les instructions ATC sans avoir à lire le texte dans la fenêtre du simulateur, pour une immersion accrue.

---

## Fonctionnalités

-   **Surveillance en temps réel** du `Log.txt` de X-Plane pour les messages 124thATC.
-   **Extraction automatique** des messages ATC.
-   **Lecture vocale** des messages via `flite` (ou `spd-say` en tant que solution de secours).

---

## Prérequis

Pour utiliser ce script, vous aurez besoin de :

1.  **Python 3** : Assurez-vous que Python 3 est installé sur votre système. Vous pouvez le télécharger depuis [python.org](https://www.python.org/downloads/).
2.  **X-Plane 11** : Le simulateur de vol.
3.  **Plugin 124thATC** : Le plugin ATC pour X-Plane 11.
4.  **Moteur de synthèse vocale (TTS) :**
    * **`flite`** (recommandé) : Un moteur TTS léger.
        * Sur Debian/Ubuntu : `sudo apt-get install flite`
        * Sur Fedora/CentOS : `sudo dnf install flite`
    * **`speech-dispatcher`** (avec `spd-say`) : Une alternative si `flite` n'est pas disponible ou préféré.
        * Sur Debian/Ubuntu : `sudo apt-get install speech-dispatcher`
        * Sur Fedora/CentOS : `sudo dnf install speech-dispatcher`

---

## Installation

1.  **Créez un dossier** pour le script sur votre ordinateur, par exemple `~/xplane_atc_reader/`.
2.  **Créez un fichier** nommé `atc_voice_reader.py` (ou le nom que vous préférez) dans ce dossier.
3.  **Copiez-collez le code Python** fourni [ici](lien_vers_votre_code_sur_github) dans ce fichier.
4.  **Mettez à jour le chemin du `Log.txt`** : Ouvrez `atc_voice_reader.py` et modifiez la ligne suivante pour qu'elle pointe vers le chemin réel de votre fichier `Log.txt` de X-Plane 11.

    ```python
    XPLANE_LOG_PATH = '/home/estemobs/.steam/steam/steamapps/common/X-Plane 11/Log.txt'
    # Adaptez ce chemin à votre installation X-Plane (Windows, macOS, Linux)
    ```
    * **Exemples de chemins courants :**
        * **Windows:** `C:\X-Plane 11\Log.txt` (ou équivalent Steam)
        * **macOS:** `/Users/VotreNomUtilisateur/Desktop/X-Plane 11/Log.txt` (ou équivalent Steam)
        * **Linux (Steam):** `/home/VotreNomUtilisateur/.steam/steam/steamapps/common/X-Plane 11/Log.txt`

---

## Utilisation

1.  **Lancez X-Plane 11** et assurez-vous que le plugin 124thATC est actif.
2.  **Ouvrez un terminal** (Linux/macOS) ou une invite de commande (Windows).
3.  **Naviguez jusqu'au dossier** où vous avez enregistré le script :
    ```bash
    cd ~/xplane_atc_reader/
    ```
4.  **Exécutez le script Python :**
    ```bash
    python3 atc_voice_reader.py
    ```
5.  Le script commencera à surveiller le fichier `Log.txt`. Lorsque 124thATC émettra une communication, le message sera lu vocalement par votre système.
6.  Pour arrêter le script, appuyez sur `Ctrl+C` dans le terminal.

---

## Configuration

Vous pouvez ajuster les paramètres suivants au début du fichier `atc_voice_reader.py` :

-   `XPLANE_LOG_PATH`: Le chemin complet vers votre fichier `Log.txt` de X-Plane 11. **C'est la modification la plus importante à faire.**
-   `ATC_KEYWORD`: Le mot-clé utilisé pour détecter les messages du 124thATC dans le log. Par défaut : `"124thATC"`.

---

## Dépannage

-   **"Erreur : 'flite' (ou 'spd-say') n'a pas été trouvé."** : Assurez-vous que le moteur TTS est correctement installé et que son exécutable est accessible via votre `PATH`.
-   **"Erreur : Le fichier log '[chemin]' n'existe pas."** : Vérifiez que le chemin spécifié dans `XPLANE_LOG_PATH` est correct et complet.
-   **Le script ne lit pas les messages ATC :**
    -   Assurez-vous que 124thATC est correctement installé et qu'il écrit bien ses communications dans le `Log.txt` de X-Plane.
    -   Vérifiez que le `ATC_KEYWORD` (`"124thATC"`) correspond bien à ce qui est écrit dans votre log.
    -   Vérifiez que votre moteur TTS fonctionne en lançant une commande simple dans le terminal, par exemple : `flite -t "Test message"` ou `spd-say "Test message"`.

---

## Contribution

Les contributions sont les bienvenues ! Si vous avez des idées d'améliorations, des corrections de bugs, ou des suggestions, n'hésitez pas à ouvrir une "issue" ou à soumettre une "pull request" sur ce dépôt GitHub.

---

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

---
---
