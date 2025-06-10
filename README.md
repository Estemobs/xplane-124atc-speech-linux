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

# xplane-124atc-speech

A simple Python script to vocalize 124thATC plugin messages from X-Plane 11's `Log.txt` file.

---

## Table of Contents

-   [Overview](#overview)
-   [Features](#features)
-   [Prerequisites](#prerequisites)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Configuration](#configuration)
-   [Troubleshooting](#troubleshooting)
-   [Contributing](#contributing)
-   [License](#license)

---

## Overview

This Python script is designed to enhance the flight simulation experience with X-Plane 11 and the 124thATC plugin. It monitors X-Plane's `Log.txt` file in real-time. When a communication message from 124thATC is detected, the script extracts the text and uses your system's text-to-speech engine to read it aloud. This allows you to hear ATC instructions without having to read the text in the simulator window, leading to increased immersion.

---

## Features

-   **Real-time monitoring** of X-Plane's `Log.txt` for 124thATC messages.
-   **Automatic extraction** of ATC messages.
-   **Vocal playback** of messages via `flite` (or `spd-say` as a fallback).

---

## Prerequisites

To use this script, you will need:

1.  **Python 3**: Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2.  **X-Plane 11**: The flight simulator.
3.  **124thATC Plugin**: The ATC plugin for X-Plane 11.
4.  **Text-to-Speech (TTS) Engine**:
    * **`flite`** (recommended): A lightweight TTS engine.
        * On Debian/Ubuntu: `sudo apt-get install flite`
        * On Fedora/CentOS: `sudo dnf install flite`
    * **`speech-dispatcher`** (with `spd-say`): An alternative if `flite` is not available or preferred.
        * On Debian/Ubuntu: `sudo apt-get install speech-dispatcher`
        * On Fedora/CentOS: `sudo dnf install speech-dispatcher`

---

## Installation

1.  **Create a folder** for the script on your computer, for example, `~/xplane_atc_reader/`.
2.  **Create a file** named `atc_voice_reader.py` (or your preferred name) inside this folder.
3.  **Copy and paste the Python code** provided [here](link_to_your_code_on_github) into this file.
4.  **Update the `Log.txt` path**: Open `atc_voice_reader.py` and modify the following line to point to the actual path of your X-Plane 11 `Log.txt` file.

    ```python
    XPLANE_LOG_PATH = '/home/estemobs/.steam/steam/steamapps/common/X-Plane 11/Log.txt'
    # Adapt this path to your X-Plane installation (Windows, macOS, Linux)
    ```
    * **Common path examples:**
        * **Windows:** `C:\X-Plane 11\Log.txt` (or Steam equivalent)
        * **macOS:** `/Users/YourUsername/Desktop/X-Plane 11/Log.txt` (or Steam equivalent)
        * **Linux (Steam):** `/home/YourUsername/.steam/steam/steamapps/common/X-Plane 11/Log.txt`

---

## Usage

1.  **Launch X-Plane 11** and ensure the 124thATC plugin is active.
2.  **Open a terminal** (Linux/macOS) or command prompt (Windows).
3.  **Navigate to the folder** where you saved the script:
    ```bash
    cd ~/xplane_atc_reader/
    ```
4.  **Execute the Python script:**
    ```bash
    python3 atc_voice_reader.py
    ```
5.  The script will start monitoring the `Log.txt` file. When 124thATC issues a communication, the message will be spoken aloud by your system.
6.  To stop the script, press `Ctrl+C` in the terminal.

---

## Configuration

You can adjust the following parameters at the beginning of the `atc_voice_reader.py` file:

-   `XPLANE_LOG_PATH`: The full path to your X-Plane 11 `Log.txt` file. **This is the most important modification to make.**
-   `ATC_KEYWORD`: The keyword used to detect 124thATC messages in the log. Default: `"124thATC"`.

---

## Troubleshooting

-   **"Error: 'flite' (or 'spd-say') not found."**: Ensure the TTS engine is correctly installed and its executable is accessible via your system's `PATH`.
-   **"Error: The log file '[path]' does not exist."**: Verify that the path specified in `XPLANE_LOG_PATH` is correct and complete.
-   **Script is not reading ATC messages**:
    -   Ensure 124thATC is properly installed and is writing its communications to X-Plane's `Log.txt`.
    -   Verify that the `ATC_KEYWORD` (`"124thATC"`) matches what is written in your log.
    -   Check that your TTS engine works by running a simple command in the terminal, e.g.: `flite -t "Test message"` or `spd-say "Test message"`.

---

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or suggestions, feel free to open an "issue" or submit a "pull request" on this GitHub repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
