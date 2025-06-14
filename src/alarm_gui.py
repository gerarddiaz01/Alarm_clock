import tkinter as tk
from tkinter import messagebox
import time
from datetime import datetime, timedelta
import random
import webbrowser

def load_video_urls(file_path="videos.txt"):
    '''Read the list of YouTube URLs and load them'''
    try:
        with open(file_path, "r") as f:
            urls = [url.strip() for url in f if url.strip()]  # Read and filter non-empty lines
        if not urls:
            raise ValueError("No URLs found.")
        return urls
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load videos: {e}")
        return []

def update_clock():
    '''Function that sets up the live clock, updates every second and avoids freezing the interface'''
    now = time.strftime("%H:%M:%S")  # Get current time as HH:MM:SS
    clock_label.config(text="Current time: " + now)  # Update the clock label
    root.after(1000, update_clock)  # Schedule the function to run every second (1000 miliseconds)

def set_alarm():
    '''Validates the user input for the alarm time'''
    global alarm_id # This variable allows us to manage this scheduled task later, and use it across the program (different functions)
    try:
        hour = int(hour_var.get())  # Get the hour from the input
        minute = int(minute_var.get())  # Get the minute from the input
        if not (0 <= hour < 24 and 0 <= minute < 60):  # Validate the input
            raise ValueError
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid hour (0–23) and minute (0–59).")
        return # If error exits the function early

    now = datetime.now()
    alarm_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
    if alarm_time <= now:  # If the alarm time has already passed, schedule it for tomorrow
        alarm_time += timedelta(days=1)

    wait_ms = int((alarm_time - now).total_seconds() * 1000)  # Convert wait time to milliseconds

    status_label.config(text=f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")  # Update the status label
    alarm_id = root.after(wait_ms, trigger_alarm)  # Schedule the alarm after the calculated delay (wait_ms)

def trigger_alarm():
    '''When the alarm is triggered, it picks a random video from the list and opens it in the browser, shows the snooze button and 
    make the repeat logic'''
    status_label.config(text="⏰ Alarm ringing! Time to wake up! 🎶") # Update the status label
    if video_list:
        chosen = random.choice(video_list)  # Pick a random video
        webbrowser.open(chosen)  # Open the video in the default browser
    else:
        messagebox.showwarning("No Videos", "No video to play.")  # Warn if no videos are available
    
    # Show the snooze button
    snooze_button.pack()

    # Repeat logic
    if repeat_var.get():  # If the "Repeat daily" checkbox is checked
        print("🔁 Rearming for tomorrow...")
        next_day = 24 * 60 * 60 * 1000  # 24 hours in milliseconds
        root.after(next_day, trigger_alarm)  # Schedule the alarm for the next day
        status_label.config(text="⏰ Alarm will repeat tomorrow.")

def snooze(minutes):
    '''Snooze the alarm for the specified number of minutes'''
    snooze_ms = minutes * 60 * 1000  # Convert minutes to milliseconds (after() only works with milliseconds)
    root.after(snooze_ms, trigger_alarm)  # Reschedule the alarm after the snooze period
    status_label.config(text=f"😴 Snoozed for {minutes} minutes.")  # Update the status label
    snooze_button.pack_forget()  # Hide the snooze button again
    
# Initialize the GUI
root = tk.Tk()
root.title("Alarm Clock 🎵")
root.geometry("400x250")

# Current Time Label
clock_label = tk.Label(root, font=("Arial", 18))
clock_label.pack(pady=10)

# Alarm Time Inputs
time_frame = tk.Frame(root) # We create a frame regroup related widgets together
time_frame.pack(pady=5)

tk.Label(time_frame, text="Hour (0–23):").grid(row=0, column=0) # Label widget with information
hour_var = tk.StringVar() # StringVar allows us dynamic binding between the variable and the widget
hour_entry = tk.Entry(time_frame, textvariable=hour_var, width=5) # Entry widget for the user to input the hour, links this input with hour_var
hour_entry.grid(row=0, column=1) # Positioning

tk.Label(time_frame, text="Minute (0–59):").grid(row=0, column=2)
minute_var = tk.StringVar()
minute_entry = tk.Entry(time_frame, textvariable=minute_var, width=5)
minute_entry.grid(row=0, column=3)

# Repeat Daily Checkbox
repeat_var = tk.BooleanVar()  # Boolean variable to track the checkbox state, is it checked or unchecked?
repeat_check = tk.Checkbutton(root, text="Repeat daily", variable=repeat_var) # Widget that allows the user to toggle the repeat option
repeat_check.pack()  # Add the checkbox to the GUI

# Confirmation Label
status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.pack(pady=5)

# Set Alarm Logic
alarm_id = None  # To store the ID of the scheduled alarm

# Trigger the Alarm
video_list = load_video_urls()

# Set Alarm Button
set_alarm_button = tk.Button(root, text="Set Alarm", command=set_alarm, font=("Arial", 12))
set_alarm_button.pack(pady=10)

# Snooze Button
snooze_button = tk.Button(root, text="Snooze 5 minutes", command=lambda: snooze(5))
snooze_button.pack(pady=5)
snooze_button.pack_forget()  # Hide the snooze button by default, it will only be shown when the alarm rings.

# Start the live clock
update_clock()

# Run the GUI event loop
root.mainloop()