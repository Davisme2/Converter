# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem

class SecondWindow(QMainWindow):
    def __init__(self, selected_videos):
        super().__init__()
        self.setWindowTitle("Deuxième Fenêtre")
        self.selected_videos = selected_videos

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.video_table = QTableWidget()
        self.video_table.setColumnCount(4)
        self.video_table.setHorizontalHeaderLabels(["n°", "Fichier sélectionné", "Format", ""])

        self.populate_video_table()

        self.layout.addWidget(self.video_table)

        self.next_button = QPushButton("Suivant", self)
        self.next_button.clicked.connect(self.open_conversion_window)

        self.layout.addWidget(self.next_button)

        self.central_widget.setLayout(self.layout)

    def populate_video_table(self):
        for i, video in enumerate(self.selected_videos):
            self.video_table.insertRow(i)
            self.video_table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            self.video_table.setItem(i, 1, QTableWidgetItem(video))
            self.video_table.setItem(i, 2, QTableWidgetItem(""))
            select_format_button = QPushButton("Sélectionner")
            select_format_button.clicked.connect(lambda _, row=i: self.open_format_selection_window(row))
            self.video_table.setCellWidget(i, 3, select_format_button)

    def open_format_selection_window(self, row):
        # À implémenter : Ouvrir une fenêtre de sélection de format
        pass

    def open_conversion_window(self):
        self.conversion_window = ConversionWindow(self, self.selected_videos)
        self.hide()
        self.conversion_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = SecondWindow()
    main_window.show()
    sys.exit(app.exec_())
