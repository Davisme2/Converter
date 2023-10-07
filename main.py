# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyFactory")

        self.select_video_button = QPushButton("Sélectionner une vidéo", self)
        self.select_video_button.clicked.connect(self.open_file_dialog)

        self.next_button = QPushButton("Suivant", self)
        self.next_button.clicked.connect(self.open_second_window)
    
    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        video_files, _ = QFileDialog.getOpenFileNames(self, "Sélectionner une ou plusieurs vidéos", "",
                                                      "Fichiers Vidéo (*.mp4 *.avi *.mkv);;Tous les fichiers (*)",
                                                      options=options)
        if video_files:
            print("Vidéos sélectionnées :", video_files)

    def open_second_window(self):
        self.second_window = SecondWindow(self)
        self.hide()
        self.second_window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
