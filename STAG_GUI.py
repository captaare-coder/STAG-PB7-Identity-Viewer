import tkinter as tk
from pathlib import Path
import json
import subprocess
import sys


def run_module(module):

    base = Path(__file__).parent
    program = base / module

    if program.exists():
        subprocess.Popen(
            [sys.executable, str(program)]
        )


def get_identity():

    archive = Path("archive.json")

    if archive.exists():

        try:
            data = json.loads(
                archive.read_text(
                    encoding="utf-8"
                )
            )

            records = data["STAG_PB7_ARCHIVE"]["RECORDS"]

            if records:

                r = records[-1]

                return f"""
SYSTEM:
🟢 ONLINE

ARCHIVE:
🟢 CONNECTED

CERTIFICATES:
{len(records)}

SUBJECT:
{r["subject"]}

CLEARANCE:
{r["clearance"]}

CERTIFICATE:
{r["certificate_id"]}

STATUS:
{r["status"]}
"""

        except:
            return "DATABASE ERROR"

    return "NO ARCHIVE"


def load_events():

    log_box.delete(
        "1.0",
        tk.END
    )

    try:

        with open(
            "events.log",
            "r",
            encoding="utf-8"
        ) as file:

            log_box.insert(
                tk.END,
                file.read()
            )

    except:

        log_box.insert(
            tk.END,
            "NO EVENTS FOUND"
        )


window = tk.Tk()

window.title(
    "STAG PB7 COMMAND CENTER"
)

window.geometry(
    "700x650"
)


# -----------------------------
# Scrollable Interface
# -----------------------------

canvas = tk.Canvas(window)

scrollbar = tk.Scrollbar(
    window,
    orient="vertical",
    command=canvas.yview
)

scroll_frame = tk.Frame(canvas)


scroll_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)


canvas.create_window(
    (0, 0),
    window=scroll_frame,
    anchor="nw"
)


canvas.configure(
    yscrollcommand=scrollbar.set
)


canvas.pack(
    side="left",
    fill="both",
    expand=True
)

scrollbar.pack(
    side="right",
    fill="y"
)


# -----------------------------
# STAG HEADER
# -----------------------------

title = tk.Label(
    scroll_frame,
    text="STAG PB7 COMMAND CENTER\nLEVEL 7 NODE",
    font=("Arial",18,"bold")
)

title.pack(pady=15)


# -----------------------------
# Identity Dashboard
# -----------------------------

identity = tk.Label(
    scroll_frame,
    text=get_identity(),
    font=("Consolas",12),
    justify="left"
)

identity.pack(pady=10)


# -----------------------------
# Event Log
# -----------------------------

log_title = tk.Label(
    scroll_frame,
    text="LIVE EVENT LOG",
    font=("Arial",14,"bold")
)

log_title.pack()


log_box = tk.Text(
    scroll_frame,
    height=6,
    width=70,
    font=("Consolas",10)
)

log_box.pack(
    pady=10
)


load_events()


# -----------------------------
# STAG MODULE BUTTONS
# -----------------------------

for name, module in [

    ("GENERATE CERTIFICATE","generator.py"),
    ("VIEW CERTIFICATE","viewer.py"),
    ("VERIFY INTEGRITY","verify_panel.py"),
    ("ARCHIVE SEARCH","archive_search.py"),
    ("CERTIFICATE VIEWER","certificate_viewer.py"),
    ("TRUST CHAIN","trust_chain.py"),
    ("TRUST CHAIN","trust_chain.py"),
    ("IDENTITY CHECK","identity_check.py")

]:

    tk.Button(
        scroll_frame,
        text=name,
        width=35,
        height=2,
        command=lambda m=module: run_module(m)

    ).pack(pady=5)



tk.Button(
    scroll_frame,
    text="REFRESH LOG",
    width=35,
    command=load_events

).pack(pady=10)



tk.Button(
    scroll_frame,
    text="CLOSE NODE",
    width=35,
    command=window.destroy

).pack(pady=10)



window.mainloop()
window.mainloop()