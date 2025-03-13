import sys
from PyQt6.QtWidgets import QApplication, QSystemTrayIcon, QMenu
from PyQt6.QtGui import QIcon
from hardware_monitor import HardwareMonitor
from style.hw_ui import get_stylesheet

class AppWithTray(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setQuitOnLastWindowClosed(False)  

        self.tray_icon = QSystemTrayIcon()
        self.tray_icon.setIcon(QIcon("tray_icon.png"))  

        self.tray_menu = QMenu()
        self.restore_action = self.tray_menu.addAction("Restore")
        self.exit_action = self.tray_menu.addAction("Exit")

        self.restore_action.triggered.connect(self.restore_app)
        self.exit_action.triggered.connect(self.quit)

        self.tray_icon.setContextMenu(self.tray_menu)

        self.tray_icon.show()

        self.main_window = HardwareMonitor()
        self.main_window.show()

    def restore_app(self):
        """Restore the app window."""
        if self.main_window.isHidden():
            self.main_window.show()
            self.main_window.activateWindow()
        else:
            self.main_window.activateWindow()

if __name__ == "__main__":
    app = AppWithTray(sys.argv)
    app.setStyleSheet(get_stylesheet()) 
    sys.exit(app.exec())