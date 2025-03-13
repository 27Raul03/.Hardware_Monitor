import csv
import os
from datetime import datetime

os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/hardware_log.csv"

if not os.path.exists(LOG_FILE) or os.stat(LOG_FILE).st_size == 0: 
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "CPU Usage (%)",
            "CPU Frequency (MHz)",
            "CPU Cores",
            "RAM Usage (%)",
            "Disk Usage (%)",
        ])


def log_data(cpu_info, ram_usage, disk_usage):
    """Append a new row of system info to the log file."""
    with open(LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            cpu_info["cpu_usage"].replace('%', ''),
            cpu_info["cpu_freq"].replace(' MHz', ''),
            cpu_info["cpu_cores"].replace(' cores', ''),
            ram_usage.replace('%', ''),
            disk_usage.replace('%', ''), 
        ])

def reset_log_file():
    """Reset log file by overwriting it and keeping only the headers."""
    with open(LOG_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Timestamp",
            "CPU Usage (%)",
            "CPU Frequency (MHz)",
            "CPU Cores",
            "RAM Usage (%)",
            "Disk Usage (%)",
        ])
