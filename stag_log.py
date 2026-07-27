from datetime import datetime
from pathlib import Path


LOG_FILE = Path("events.log")


def log_event(message):

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    entry = f"[{timestamp}] {message}\n"

    with open(
        LOG_FILE,
        "a",
        encoding="utf-8"
    ) as file:
        file.write(entry)