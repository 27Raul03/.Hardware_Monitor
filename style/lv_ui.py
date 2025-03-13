def get_stylesheet():
    """Returns the dark theme stylesheet for the LogViewer."""
    return """
        QWidget {
            background-color: #2b2b2b;
            color: #ffffff;
            font-size: 14px;
        }
        QTableWidget {
            background-color: #3a3a3a;
            border: 1px solid #555;
            gridline-color: #555;
            font-size: 12px;
            color: white;  /* Ensure text is white by default */
        }
        QTableWidget::item {
            padding: 5px;
            background-color: #3a3a3a;  /* Default background for items */
            color: white;  /* Ensure text is white */
        }
        QTableWidget::item:alternate {
            background-color: #444;  /* Alternate row color */
            color: white;  /* Ensure text is white */
        }
        QTableWidget::item:selected {
            background-color: #555;  /* Selected item background */
            color: white;  /* Ensure text is white */
        }
        QHeaderView::section {
            background-color: #3a3a3a;
            padding: 5px;
            border: 1px solid #555;
            font-size: 12px;
            font-weight: bold;
            color: white;  /* Ensure header text is white */
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
    """