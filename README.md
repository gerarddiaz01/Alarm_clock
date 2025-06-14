# Youtube Alarm Clock ⏰

This project offers two practical implementations of a customizable alarm clock in Python:
  - Terminal version: Lightweight, functional, and runs in any terminal.
  - GUI version: Interactive, user-friendly interface built with tkinter, offering snooze, live clock, and repeat options.

Both versions use a fun and unique twist: when the alarm goes off, they open a random YouTube video from a playlist you define. That’s right — instead of waking up to a default buzzer, you get a surprise song, podcast, or motivational video to start your day.

---

## Learning Context 📚

This project was developed in May 2025 as part of my effort to better understand datetime, scheduling logic, file handling, and GUI responsiveness. It helped me shift from CLI tools into GUI programming and experiment with cross-concept integration (time, multimedia, dynamic UI).

I started by building the terminal version to nail down the core logic, then expanded it into a GUI — mirroring how I learn best: iterate, expand, and reflect.

---

## How to Run the Application 🚀

**1. Terminal-Based Alarm (`simple_alarm.py`)**

1. **Prepare the Video List**:
   - Use the `videos.txt` file with the songs by default or include your own choices as YouTube video URLs, one per line.

2. **Run the Script**:
   - Open a terminal, install libraries, and run the script.

3. **Set the Alarm**:
   - Enter the alarm time in `HH:MM` (24-hour format) when prompted.
   - The script will wait until the specified time and then play a random YouTube video.

---

**2. GUI-Based Alarm (`alarm_gui.py`)**

1. **Prepare the Video List**:
   - Use the `videos.txt` file with the songs by default or include your own choices as YouTube video URLs, one per line.

2. **Run the Script**:
   - Open a terminal, install libraries, and run the script.

3. **Use the GUI**:
   - Set the alarm time using the input fields for hour and minute.
   - Optionally, enable the "Repeat Daily" checkbox to rearm the alarm automatically for the next day.
   - When the alarm rings, use the "Snooze 5 minutes" button to delay the alarm.

---

## Features ✨

**Terminal-Based Alarm (`simple_alarm.py`)**
- Minimal setup — no GUI dependencies
- Handles past time by scheduling for the next day
- Opens a random YouTube video as the alarm
- Graceful input and file error handling

**GUI-Based Alarm (`alarm_gui.py`)**
- Live digital clock updated every second
- Input fields for hour and minute
- Snooze button (5 minutes)
- Repeat Daily toggle
- Responsive interface using tkinter.after()
- Error popups for invalid input or missing videos

---

## Tools and Concepts Used 🧰

- `datetime` and `timedelta`: Scheduling alarms and handling time shifts.
- `time.sleep()`: Pauses the script until the alarm time is reached.
- `webbrowser.open()`: Opens a random YouTube video in the default web browser.
- Error Handling: Validates input and ensures robustness.
- `tkinter`: GUI components, including dynamic buttons and labels.
- `tkinter.after()`:Schedules tasks (e.g., updating the live clock, triggering the alarm) without blocking the GUI.
- random.choice(): Picks a random video from videos.txt

---

## Challenges Encountered and Solutions 🧩

1. Freezing GUI with sleep()
- Problem: Using time.sleep() froze the GUI.
- Solution: Used after() for all scheduled events, ensuring the UI remained responsive.

2. Repeat Daily Logic

- Problem: Rearming the alarm at exactly the same time 24 hours later.
- Solution: Used after() with 24h delay in milliseconds and status messaging to confirm repeat.

3. Snooze Integration

- Problem: Needed to delay alarm and manage snooze toggle visibility.
- Solution: Scheduled a 5-minute delay and hid/showed the snooze button dynamically.

4. Invalid or Missing videos.txt

- Problem: If file was missing or empty, the alarm failed silently.
- Solution: Validated video list and surfaced errors clearly in both versions.

---

## What I Learned 👨‍🎓

- Structured datetime logic for real-world task scheduling
- tkinter layout, event binding, and widget visibility handling
- Thread-safe GUI practices using after()
- Clean UX thinking: auto-focus, user messaging, and graceful recovery
- Iterative development from CLI prototype → GUI version

---

## Notes for Learners 🧾

The terminal version shows my foundational understanding of logic and flow control.
The GUI version expands that into a feature-complete app using modern Python tools.
I’ve heavily commented the code so you can learn from it — especially around GUI timing.
This is also a practical example of repurposing Python scripts into user-friendly tools.

---

## Could This Be a Real App? 💻

Yes — with adaptation, this could work on desktops or even Android (via kivy, beeWare, or converting to APK). Most mobile alarms use local audio — waking up to a random video is a fun, refreshing twist. Definitely a conversation starter, and a potential UX differentiator.

That idea is what inspired me to build it in the first place.

---

## Conclusion 📝

This is more than an alarm clock — it’s a learning milestone. It represents:
- Real functionality.
- A playful concept.
- Clean implementation.
- Solid problem-solving.
- And most of all, growth.

I built it piece by piece, improved it, and documented it so others can follow the same learning path.

Thanks for reading — and I hope this project both wakes you up and sparks some inspiration.
