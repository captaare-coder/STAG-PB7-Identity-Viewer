import tkinter as tk
import json
from pathlib import Path


def load_certificate():

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
╔══════════════════════════════════╗
       STAG PB7 CERTIFICATE
             VIEWER
╠══════════════════════════════════╣

CERTIFICATE ID:

{r["certificate_id"]}


SUBJECT:

{r["subject"]}


FIELD:

{r["field"]}


CLEARANCE:

{r["clearance"]}


CREATED:

{r["created"]}


FINGERPRINT:

{r["fingerprint"]}


STATUS:

{r["status"]}

╚══════════════════════════════════╝
"""

        except:
            return "DATABASE ERROR"

    return "NO CERTIFICATE FOUND"



window = tk.Tk()

window.title(
    "STAG PB7 CERTIFICATE VIEWER"
)

window.geometry(
    "650x550"
)


display = tk.Label(
    window,
    text=load_certificate(),
    font=("Consolas",11),
    justify="left"
)

display.pack(
    pady=30
)


tk.Button(
    window,
    text="REFRESH CERTIFICATE",
    width=30,
    command=lambda:
    display.config(
        text=load_certificate()
    )
).pack(pady=10)


tk.Button(
    window,
    text="CLOSE",
    width=30,
    command=window.destroy
).pack()


window.mainloop()