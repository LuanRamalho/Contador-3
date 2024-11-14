import time
import tkinter as tk

def start_timer():
    global running
    running = True
    update_timer()

def update_timer():
    if running:
        global seconds
        seconds += 1
        minutes, secs = divmod(seconds, 60)
        timer_label.config(text=f"{minutes:02}:{secs:02}")
        root.after(1000, update_timer)

def stop_timer(event):
    global running
    running = False

seconds = 0
running = False

root = tk.Tk()
root.title("Simple Python Timer")
root.configure(bg='yellow')

start_button = tk.Button(root, text="Click to start Timer", command=start_timer)
start_button.pack(pady=20)

timer_label = tk.Label(root, text="00:00", font=("Helvetica", 36), bg='yellow', fg='purple')
timer_label.pack(pady=20)

root.bind("<Button-1>", stop_timer)  # Click anywhere to stop the timer
root.mainloop()
