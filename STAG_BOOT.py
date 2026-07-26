from stag_log import log_event
import tkinter as tk
import time
from pathlib import Path
import subprocess
import sys


messages = [
    "INITIALIZING STAG PB7 CORE...",
    "LOADING ARCHIVE DATABASE...",
    "CHECKING CERTIFICATE ENGINE...",
    "VERIFYING SEARCH MODULE...",
    "CONNECTING VISUAL NODE...",
    "LEVEL 7 ACCESS READY"
]


window = tk.Tk()

window.title("STAG PB7 SECURITY LAYER")
window.geometry("600x350")


title = tk.Label(
    window,
    text="STAG PB7 INITIALIZATION",
    font=("Arial", 18, "bold")
)

title.pack(pady=30)


status = tk.Label(
    window,
    text="",
    font=("Consolas", 12)
)

status.pack(pady=20)


progress = tk.Label(
    window,
    text="[....................] 0%",
    font=("Consolas", 12)
)

progress.pack()


def boot():

    for i, msg in enumerate(messages):

        status.config(text=msg)
        
        log_event(msg)

        percent = int(((i + 1) / len(messages)) * 100)

        bars = int(percent / 5)

        progress.config(
            text="[" + "█" * bars + "." * (20-bars) + f"] {percent}%"
        )

        window.update()

        time.sleep(1)

    status.config(
        text="ACCESS GRANTED\nLEVEL 7 NODE ACTIVE"
    )

    progress.config(
        text="[████████████████████] 100%"
    )

    window.update()

    time.sleep(2)

    window.destroy()

    subprocess.Popen(
        [sys.executable, "STAG_GUI.py"]
    )


window.after(500, boot)

window.mainloop()