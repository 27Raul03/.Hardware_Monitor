from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from utils.system_utils import get_cpu_info, get_ram_info, get_disk_info
from utils.gpu_utils import get_gpu_info
from utils.graph_utils import update_graphs
from utils.logger_utils import log_data
from style.hw_ui import get_stylesheet

class HardwareWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        # Labels
        self.cpu_label_text = QLabel("CPU Usage:")
        self.cpu_label_value = QLabel()

        self.cpu_freq_label_text = QLabel("CPU Frequency:")
        self.cpu_freq_label_value = QLabel()

        self.cpu_cores_label_text = QLabel("CPU Cores Used:")
        self.cpu_cores_label_value = QLabel()

        self.ram_label_text = QLabel("RAM Usage:")
        self.ram_label_value = QLabel()

        self.disk_label_text = QLabel("Disk Usage:")
        self.disk_label_value = QLabel()

        self.gpu_label_text = QLabel("GPU Info:")
        self.gpu_label_value = QLabel()

        # Matplotlib Graphs
        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvas(self.figure)
        self.cpu_usage_history = []
        self.ram_usage_history = []

        # Refresh Button
        self.refresh_button = QPushButton("Refresh Data")
        self.refresh_button.clicked.connect(self.update_data)

        # Grid layout widgets
        layout.addWidget(self.cpu_label_text, 0, 0)
        layout.addWidget(self.cpu_label_value, 0, 1)

        layout.addWidget(self.cpu_freq_label_text, 1, 0)
        layout.addWidget(self.cpu_freq_label_value, 1, 1)

        layout.addWidget(self.cpu_cores_label_text, 2, 0)
        layout.addWidget(self.cpu_cores_label_value, 2, 1)

        layout.addWidget(self.ram_label_text, 3, 0)
        layout.addWidget(self.ram_label_value, 3, 1)

        layout.addWidget(self.disk_label_text, 4, 0)
        layout.addWidget(self.disk_label_value, 4, 1)

        layout.addWidget(self.gpu_label_text, 5, 0)
        layout.addWidget(self.gpu_label_value, 5, 1)

        layout.addWidget(self.refresh_button, 6, 0, 1, 2)
        layout.addWidget(self.canvas, 7, 0, 1, 2)

        self.setLayout(layout)
        self.setStyleSheet(get_stylesheet())

    def update_data(self):
        """Fetch and update system stats."""
        cpu_info = get_cpu_info()
        self.cpu_label_value.setText(cpu_info["cpu_usage"])
        self.cpu_freq_label_value.setText(cpu_info["cpu_freq"])
        self.cpu_cores_label_value.setText(cpu_info["cpu_cores"])

        self.ram_label_value.setText(get_ram_info())
        self.disk_label_value.setText(get_disk_info())
        self.gpu_label_value.setText(get_gpu_info())

        update_graphs(self.ax, self.canvas, self.cpu_usage_history, self.ram_usage_history)

    def get_cpu_info(self):
        """Return the current CPU info as a dictionary."""
        return {
            "cpu_usage": self.cpu_label_value.text(),
            "cpu_freq": self.cpu_freq_label_value.text(),
            "cpu_cores": self.cpu_cores_label_value.text(),
        }