import psutil

def get_cpu_info():
    """Fetch CPU information."""
    return {
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "cpu_freq": f"{psutil.cpu_freq().current:.2f} MHz",
        "cpu_cores": f"{psutil.cpu_count(logical=True)} cores"
    }

def get_ram_info():
    """Fetch RAM information."""
    return f"{psutil.virtual_memory().percent}%"

def get_disk_info():
    """Fetch disk usage information."""
    return f"{psutil.disk_usage('/').percent}%"