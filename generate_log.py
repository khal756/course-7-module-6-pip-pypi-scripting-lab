# lib/generate_log.py
from datetime import datetime

def generate_log(entries):
    if not isinstance(entries, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as f:
        for line in entries:
            f.write(f"{line}\n")

    print(f"Log file created: {filename}")
    return filename