import msvcrt
from datetime import datetime

LOG_FILE = "keystrokes_log.txt"

def log_key(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {key}\n")

def format_key(key):
    if key == b'\r':
        return "[ENTER]"
    elif key == b' ':
        return "[SPACE]"
    elif key == b'\x08':
        return "[BACKSPACE]"
    elif key == b'\x1b':
        return "[ESC]"
    else:
        try:
            return key.decode("utf-8")
        except:
            return str(key)

def main():
    print("=== Educational Keystroke Logging Demo ===")
    print("Logs keys typed inside this program only.")
    print("Press ESC to stop.\n")

    while True:
        key = msvcrt.getch()

        formatted = format_key(key)

        if formatted == "[ESC]":
            log_key(formatted)
            print("\nExiting...")
            break

        print(formatted, end="", flush=True)
        log_key(formatted)

if __name__ == "__main__":
    main()
