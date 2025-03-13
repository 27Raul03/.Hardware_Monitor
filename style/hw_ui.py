def get_stylesheet():
    """Returns the dark theme stylesheet."""
    return """
        QWidget {
            background-color: #2b2b2b;
            color: #ffffff;
            font-size: 14px;
        }
        QLabel {
            padding: 5px;
        }
        QPushButton {
            background-color: #3a3a3a;
            border: 1px solid #555;
            padding: 8px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        QPushButton:hover {
            background-color: #444;
        }
        QPushButton:pressed {
            background-color: #555;
        }
         QTabWidget::pane {
            border: 1px solid #555;
            background-color: #2b2b2b;
        }
        QTabBar::tab {
            background-color: #3a3a3a;
            color: white;
            padding: 8px;
            border: 1px solid #555;
            border-bottom: none;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
        }
        QTabBar::tab:selected {
            background-color: #555;
            border-color: #555;
        }
        QTabBar::tab:hover {
            background-color: #444;
        }
    """