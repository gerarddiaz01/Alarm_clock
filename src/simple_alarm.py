import random
import time
from datetime import datetime, timedelta
import webbrowser

def load_video_urls(file_path="videos.txt"):
    '''Read the list of YouTube URLs'''
    try:
        with open(file_path, "r") as f: # read the file
            urls = f.read().splitlines() # split into different lines
            urls = [url for url in urls if url.strip() != ""] # filter out blank lines
        if not urls:
            raise ValueError("No URLs found in the file.")
        return urls
    except FileNotFoundError:
        print("❌ The file 'videos.txt' was not found.")
        return []
    except Exception as e:
        print(f"❌ Error loading videos: {e}")
        return []

# Get alarm time from the user and calculate wait time
def get_alarm_time():
    '''Handles user input for the alarm time and calculates how long to wait until the alarm'''
    while True:
        user_input = input("⏰ Enter alarm time (HH:MM, 24h format): ").strip() # strip to remove whitespace

        try:
            # Parse the input time
            alarm_hour, alarm_minute = map(int, user_input.split(":")) # Split the input using ":" as separator, converts them as int, and returns the variables
            if not (0 <= alarm_hour < 24 and 0 <= alarm_minute < 60): # Validation hour 0-23 and minute 0-59 if not raises error
                raise ValueError("Hour or minute out of range")
            
            # Get the current time
            now = datetime.now() # Retrieves the current time and date
            alarm_time = now.replace(hour=alarm_hour, minute=alarm_minute, second=0, microsecond=0) # Creates the alarm object with user input

            # If the alarm time has already passed today, schedule it for tomorrow
            if alarm_time <= now:
                alarm_time += timedelta(days=1) # Add one day to the alarm
            
            # Calculate the time difference in seconds
            time_until_alarm = (alarm_time - now).total_seconds()
            print(f"🕐 Alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M:%S')} " # strftime(): Formats the datetime object into a readable string
                  f"({int(time_until_alarm)} seconds from now)") # Displays the alarm time and the number of seconds until the alarm
            
            return time_until_alarm # Returns the calculated wait time in seconds, which can be used later to trigger the alarm
        
        except ValueError:
            print("❌ Invalid time format. Please enter in HH:MM (24h) format.")

def wait_and_play(wait_seconds, video_list):
    '''Wait for the alarm time and play a random video from the list'''
    print("⏳ Waiting for the alarm...")
    try:
        time.sleep(wait_seconds) # wait for the specified number of seconds
    except KeyboardInterrupt:
        print("⏹️ Alarm cancelled manually.")
        return

    print("⏰ ALARM! Time to wake up!")
    if video_list:
        chosen_url = random.choice(video_list) # Pick a random URL video from the .txt
        print(f"🎥 Playing: {chosen_url}")
        webbrowser.open(chosen_url) # Open the video in th default web browser
    else:
        print("⚠️ No video URLs available.")

# Main block to glue everything together
if __name__ == "__main__":
    video_list = load_video_urls()
    if not video_list:
        print("🚫 Exiting: No video list found.")
    else:
        wait_seconds = get_alarm_time()
        wait_and_play(wait_seconds, video_list)
