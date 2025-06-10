# xplane-124atc-speech-linux

A simple Python script to read aloud ATC messages from the 124thATC plugin for X-Plane 11 directly from the `Log.txt` file.

---

## Table of Contents

-   [Overview](#overview)
-   [Features](#features)
-   [Requirements](#requirements)
-   [Installation](#installation)
-   [Usage](#usage)
-   [Configuration](#configuration)
-   [Troubleshooting](#troubleshooting)
-   [Contributing](#contributing)
-   [License](#license)

---

## Overview

This Python script is designed to enhance your flight simulation experience with X-Plane 11 and the 124thATC plugin. It monitors the X-Plane `Log.txt` file in real time. When a communication message from 124thATC is detected, the script extracts the text and reads it aloud using your system's speech synthesis engine. This allows you to hear ATC instructions without having to read the text in the simulator window, for greater immersion.

---

## Features

-   **Real-time monitoring** of X-Plane's `Log.txt` for 124thATC messages.
-   **Automatic extraction** of ATC messages.
-   **Text-to-speech reading** of messages via `flite` (or `spd-say` as a fallback).

---

## Requirements

To use this script, you will need:

1.  **Python 3**: Make sure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2.  **X-Plane 11**: The flight simulator.
3.  **124thATC Plugin**: The ATC plugin for X-Plane 11.
4.  **Text-to-Speech (TTS) engine:**
    * **`flite`** (recommended): A lightweight TTS engine.
        * On Debian/Ubuntu: `sudo apt-get install flite`
        * On Fedora/CentOS: `sudo dnf install flite`
    * **`speech-dispatcher`** (with `spd-say`): An alternative if `flite` is not available or preferred.
        * On Debian/Ubuntu: `sudo apt-get install speech-dispatcher`
        * On Fedora/CentOS: `sudo dnf install speech-dispatcher`

---

## Installation

1.  **Create a folder** for the script on your computer, for example `~/xplane_atc_reader/`.
2.  **Create a file** named `atc_voice_reader.py` (or any name you prefer) in this folder.
3.  **Copy and paste the provided Python code** [here](link_to_your_code_on_github) into this file.
4.  **Update the `Log.txt` path**: Open `atc_voice_reader.py` and edit the following line to point to the actual path of your X-Plane 11 `Log.txt` file.

    ```python
    XPLANE_LOG_PATH = '/home/estemobs/.steam/steam/steamapps/common/X-Plane 11/Log.txt'
    # Adjust this path to your X-Plane installation (Windows, macOS, Linux)
    ```
    * **Common path examples:**
        * **Windows:** `C:\X-Plane 11\Log.txt` (or Steam equivalent)
        * **macOS:** `/Users/YourUsername/Desktop/X-Plane 11/Log.txt` (or Steam equivalent)
        * **Linux (Steam):** `/home/YourUsername/.steam/steam/steamapps/common/X-Plane 11/Log.txt`

---

## Usage

1.  **Start X-Plane 11** and make sure the 124thATC plugin is active.
2.  **Open a terminal** (Linux/macOS) or command prompt (Windows).
3.  **Navigate to the folder** where you saved the script:
    ```bash
    cd ~/xplane_atc_reader/
    ```
4.  **Run the Python script:**
    ```bash
    python3 atc_voice_reader.py
    ```
5.  The script will start monitoring the `Log.txt` file. When 124thATC issues a communication, the message will be read aloud by your system.
6.  To stop the script, press `Ctrl+C` in the terminal.

---

## Configuration

You can adjust the following settings at the beginning of the `atc_voice_reader.py` file:

-   `XPLANE_LOG_PATH`: The full path to your X-Plane 11 `Log.txt` file. **This is the most important setting to change.**
-   `ATC_KEYWORD`: The keyword used to detect 124thATC messages in the log. Default: `"124thATC"`.

---

## Troubleshooting

-   **"Error: 'flite' (or 'spd-say') was not found."**: Make sure the TTS engine is properly installed and its executable is accessible via your `PATH`.
-   **"Error: Log file '[path]' does not exist."**: Check that the path specified in `XPLANE_LOG_PATH` is correct and complete.
-   **The script does not read ATC messages:**
    -   Make sure 124thATC is properly installed and is writing its communications to X-Plane's `Log.txt`.
    -   Check that the `ATC_KEYWORD` (`"124thATC"`) matches what is written in your log.
    -   Verify that your TTS engine works by running a simple command in the terminal, for example: `flite -t "Test message"` or `spd-say "Test message"`.

---

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or suggestions, feel free to open an issue or submit a pull request on this GitHub repository.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
