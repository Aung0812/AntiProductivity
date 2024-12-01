import keyboard
import sys
from time import sleep
from open_video import open_random_video

API_KEY = sys.argv[1]

typed_text = ""
last_key = None
word_list = ['def', 'int', 'str', 'func', 'float', 'print', 'true', 'false', 'log', "if", "for", "while"]

def check_for_words():
    global typed_text
    for word in word_list:
        if word in typed_text.lower():
            print(f"Hmmm I think it's time you had a break!")
            try:
                open_random_video(API_KEY)
                typed_text = ""
            except Exception as e:
                print(f"Error opening video: {e}")

while True:
    event = keyboard.read_event()

    if event.event_type == keyboard.KEY_DOWN and event.name != last_key:
        key = event.name

        # Handle special keys
        if key == 'space':
            typed_text += ' '
        elif key == 'backspace':
            typed_text = typed_text[:-1]
        elif len(key) == 1:
            typed_text += key

        # Update the last key pressed
        last_key = event.name

    elif event.event_type == keyboard.KEY_UP:
        # Reset last_key when key is released to avoid key repeats
        last_key = None

    check_for_words()

    sleep(0.01)