from PyQt6.QtWidgets import QTabWidget, QVBoxLayout, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTimer
from hardware_widget import HardwareWidget
from stats_log.log_viewer import LogViewer
from style.hw_ui import get_stylesheet

class HardwareMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.tabs = QTabWidget()

        self.hardware_widget = HardwareWidget()

        self.log_viewer = LogViewer()
        self.log_viewer.load_log_file()  

        self.tabs.addTab(self.hardware_widget, "Hardware Monitor")
        self.tabs.addTab(self.log_viewer, "Log Viewer")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

        self.setStyleSheet(get_stylesheet())

        self.setWindowIcon(QIcon("tray_icon.png"))

        self.setWindowTitle("Hardware Monitor")
        self.resize(600, 500)

        self.timer = QTimer()
        self.timer.timeout.connect(self.hardware_widget.update_data)
        self.timer.start(1000)

        self.logging_timer = QTimer()
        self.logging_timer.timeout.connect(self.log_data)
        self.logging_timer.start(500000)

    def log_data(self):
        """Log the current system data to the log file."""
        cpu_info = self.hardware_widget.get_cpu_info()
        ram_usage = self.hardware_widget.ram_label_value.text()
        disk_usage = self.hardware_widget.disk_label_value.text()

        from utils.logger_utils import log_data
        log_data(cpu_info, ram_usage, disk_usage)

    def closeEvent(self, event):
        """Override the close event to minimize to the system tray."""
        event.ignore()  
        self.hide()  
        print("App minimized to system tray.")  