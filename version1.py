import ipywidgets as widgets
import time
import threading

SLEEP_TIME = 30*60

button = widgets.Button(description="Click Me to start", tooltip="Start Countdown")

def update_button_state(button, description, next_function=None):
    button.description = description
    if next_function:
        threading.Thread(target=next_function, args=(button,)).start()

def print_countdown_time(remaining_time):
    for i in range(remaining_time, 0, -1):
        print(f"Remaining time: {i} seconds")
        time.sleep(1)
        
def button_clicked(b):
    update_button_state(b, "中文时间", first_countdown)
    
def first_countdown(button):
    print_countdown_time(SLEEP_TIME)
    update_button_state(button, "English Time", second_countdown)

def second_countdown(button):
    print_countdown_time(SLEEP_TIME)
    update_button_state(button, "Good Night!")


button.on_click(button_clicked)

button
