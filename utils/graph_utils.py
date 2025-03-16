import psutil
import matplotlib.pyplot as plt

def update_graphs(ax, canvas, cpu_usage_history, ram_usage_history):
    """Update Matplotlib graphs with new CPU and RAM usage data."""
    cpu_usage_history.append(psutil.cpu_percent())
    ram_usage_history.append(psutil.virtual_memory().percent)

    if len(cpu_usage_history) > 50:
        cpu_usage_history.pop(0)
        ram_usage_history.pop(0)

    ax.clear()
    ax.plot(cpu_usage_history, label="CPU Usage (%)", color="red")
    ax.plot(ram_usage_history, label="RAM Usage (%)", color="blue")

    ax.set_ylim(0, 100)
    ax.set_title("CPU & RAM Usage Over Time")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Usage (%)")
    ax.legend()

    ax.set_frame_on(True)
    ax.grid(True)

    plt.tight_layout()

    canvas.draw()