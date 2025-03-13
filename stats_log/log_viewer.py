from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout, QMessageBox, QApplication
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QEvent
import os
import subprocess
from style.lv_ui import get_stylesheet

class LogViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.log_table = QTableWidget()
        self.log_table.setColumnCount(6)  
        self.log_table.setHorizontalHeaderLabels([
            "Timestamp", "CPU Usage (%)", "CPU Frequency (MHz)", 
            "CPU Cores", "RAM Usage (%)", "Disk Usage (%)"
        ])
        self.log_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)  
        self.log_table.setAlternatingRowColors(True)  

        layout.addWidget(self.log_table)

        button_layout = QHBoxLayout()

        self.refresh_button = QPushButton("Refresh Log Viewer")
        self.refresh_button.clicked.connect(self.load_log_file)  # Connect to load_log_file
        button_layout.addWidget(self.refresh_button)

        self.open_log_button = QPushButton("Open Log File")
        self.open_log_button.clicked.connect(self.open_log_file)
        button_layout.addWidget(self.open_log_button)

        self.delete_button = QPushButton("Delete Log File")
        self.delete_button.clicked.connect(self.delete_log_file)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        self.setStyleSheet(get_stylesheet())

    def load_log_file(self):
        """Load the log file and display its contents in the QTableWidget."""
        log_path = os.path.abspath("logs/hardware_log.csv")
        if os.path.exists(log_path):
            with open(log_path, 'r') as log_file:
                lines = log_file.readlines()
                self.log_table.setRowCount(len(lines))  

                for row, line in enumerate(lines):
                    data = line.strip().split(',')
                    for col, value in enumerate(data):
                        item = QTableWidgetItem(value)
                        item.setForeground(QColor("white"))  
                        self.log_table.setItem(row, col, item)
        else:
            self.log_table.setRowCount(1)
            item = QTableWidgetItem("Log file not found.")
            item.setForeground(QColor("white"))  
            self.log_table.setItem(0, 0, item)

    def delete_log_file(self):
        """Delete the log file and clear the table."""
        log_path = os.path.abspath("logs/hardware_log.csv")

        reply = QMessageBox.question(
            self,
            "Press the delete button",
            "Are you sure you wanna delete the log files?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:

            if os.path.exists(log_path):
                try:
                    os.remove(log_path)  
                    self.log_table.setRowCount(0)  
                    print("Log file deleted successfully.")
                except Exception as e:
                    print(f"Failed to delete log file: {e}")
            else:
                print("Log file does not exist.")

    def open_log_file(self):
        """Open the log file using the default CSV viewer (Excel, Notepad, etc.)."""
        log_path = os.path.abspath("logs/hardware_log.csv")
        
        reply = QMessageBox.question(
            self,
            "Open CSV File",
            "An external application (e.g., Excel) will open, and this app will close. Do you want to continue?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            QApplication.quit()

            if os.name == 'nt':  # Windows
                try:
                    os.startfile(log_path)
                except Exception as e:
                    print(f"Failed to open log file: {e}")
            elif os.name == 'posix':  # Linux, MacOS
                try:
                    subprocess.Popen(['xdg-open', log_path])
                except Exception as e:
                    print(f"Failed to open log file: {e}")
            else:
                print(f"Please open manually: {log_path}")

    def showEvent(self, event: QEvent):
        """Override showEvent to refresh the log viewer when the tab is shown."""
        super().showEvent(event)
        self.load_log_file()  