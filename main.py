import sys
from PyQt6.QtWidgets import QApplication
from hardware_monitor import HardwareMonitor
from style.hw_ui import get_stylesheet


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(get_stylesheet())
    window = HardwareMonitor()
    window.show()
    sys.exit(app.exec())