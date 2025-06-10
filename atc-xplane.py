import time
import subprocess
import re
import os

# --- Configuration ---
# Replace this with the actual path to your X-Plane log.txt file
XPLANE_LOG_PATH = '/home/estemobs/.steam/steam/steamapps/common/X-Plane 11/Log.txt' 

# Keyword to identify 124th ATC messages
ATC_KEYWORD = "124thATC"

# NATO phonetic alphabet dictionary
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
    # Converts each letter/number to phonetic, keeps spaces
    return ' '.join(PHONETIC_DICT.get(char, char) for char in text if char != ' ')

def replace_callsign_with_phonetic(message):
    # Looks for the callsign before or after the comma
    # Examples: "CFJ 05, turn right heading 036." or "Turn right heading 036, CFJ 05"
    match = re.search(r'([A-Z]{2,}\s?\d{1,3})[,\.]', message)
    if not match:
        match = re.search(r'[,\.]\s*([A-Z]{2,}\s?\d{1,3})', message)
    if match:
        callsign = match.group(1)
        phonetic = to_phonetic(callsign.replace(' ', ''))
        # Replace the callsign with its phonetic version in the message
        return message.replace(callsign, phonetic)
    return message

# --- Function to read the message with speech synthesis ---
def speak(text):
    print(f"Attempting to read: '{text}'")
    try:
        # Add phonetic conversion of the callsign
        text = replace_callsign_with_phonetic(text)
        subprocess.run(['flite', '-t', text], check=True)
        print("Message read successfully.")
    except FileNotFoundError:
        print("Error: 'flite' was not found. Make sure flite is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Error when calling flite: {e}")
    except Exception as e:
        print(f"An unexpected error occurred during speech synthesis: {e}")

# --- Function to extract the ATC message ---
def extract_atc_message(log_line):
    # Regex to capture everything after "Communication: "
    match = re.search(r"Communication:\s*(.*)", log_line)
    if match:
        return match.group(1).strip()
    return None

# --- Log file monitoring (simple method without 'tailer') ---
def follow_log(filepath):
    print(f"Monitoring log file: {filepath}")
    last_inode = None
    last_size = 0
    f = None

    while True:
        try:
            if not os.path.exists(filepath):
                print(f"Waiting for log file '{filepath}' to be created...")
                time.sleep(1)
                continue

            stat = os.stat(filepath)
            inode = stat.st_ino
            size = stat.st_size

            # Open or reopen the file if replaced or truncated
            if inode != last_inode or size < last_size or f is None:
                if f:
                    f.close()
                f = open(filepath, 'r', encoding='utf-8', errors='ignore')
                f.seek(0, os.SEEK_END)
                last_inode = inode
                print("Log file (re)opened and monitoring resumed.")

            last_size = size

            # Read new lines
            while True:
                line = f.readline()
                if not line:
                    break
                if ATC_KEYWORD in line:
                    print(f"ATC line detected: {line.strip()}")
                    message = extract_atc_message(line)
                    if message:
                        speak(message)
                    else:
                        print("Unable to extract ATC message from line.")
            time.sleep(0.5)
        except Exception as e:
            print(f"Error while monitoring log: {e}")
            time.sleep(1)

# --- Script entry point ---
if __name__ == "__main__":
    try:
        intro_message = (
            "Speech synthesis for X-Plane 11 is now enabled. "
            "Please start the game."
        )
        print(intro_message)
        subprocess.run(['flite', '-t', intro_message], check=True)
        follow_log(XPLANE_LOG_PATH)
    except KeyboardInterrupt:
        print("\nLog monitoring stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")