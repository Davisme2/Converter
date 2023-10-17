# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QTableWidget, QStackedWidget, QMessageBox, QWidget, QProgressBar
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")
        self.resize(1254, 888)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet("background-color: rgb(40, 40, 42);")

        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)  # Définir centralwidget pour la fenêtre principale

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-50, 680, 1401, 161))
        self.frame.setStyleSheet("border: 60 px solid;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(720, 90, 241, 71))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "font: 63 18pt \"Montserrat SemiBold\";\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 20px solid;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.open_file_dialog)

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(1020, 90, 171, 71))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "font: 63 18pt \"Montserrat SemiBold\";\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 20px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_second_window)

        self.setWindowTitle("MyFactory")

        self.stacked_widget = QStackedWidget(self.centralwidget)  # Utilisez centralwidget comme parent de QStackedWidget

        self.first_window = QWidget()
        self.second_window = QWidget()
        self.third_window = QWidget()

        self.stacked_widget.addWidget(self.first_window)
        self.stacked_widget.addWidget(self.second_window)
        self.stacked_widget.addWidget(self.third_window)

        self.init_first_window()
        self.init_second_window()
        self.init_third_window()

        self.stacked_widget.setCurrentIndex(0)

        self.selected_videos = []  # Liste pour stocker les vidéos sélectionnées

    def init_first_window(self):
        layout = QVBoxLayout()

        select_video_button = QPushButton("Sélectionner une vidéo")
        select_video_button.clicked.connect(self.open_file_dialog)

        layout.addWidget(select_video_button)

        self.first_window.setLayout(layout)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        video_files, _ = QFileDialog.getOpenFileNames(self, "Sélectionner des vidéos", "",
                                                      "Fichiers Vidéo (*.mp4 *.avi *.mkv);;Tous les fichiers (*)",
                                                      options=options)

        if video_files:
            self.selected_videos = video_files
            print("Vidéos sélectionnées :", self.selected_videos)
            self.open_second_window()
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez sélectionner une ou plusieurs vidéos s'il vous plaît.",
                                QMessageBox.Ok)

    def open_second_window(self):
        if self.selected_videos:
            self.stacked_widget.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Avertissement", "Veuillez sélectionner une ou plusieurs vidéos s'il vous plaît.",
                                QMessageBox.Ok)

    def init_second_window(self):
        layout = QVBoxLayout()

        video_table = QTableWidget()
        video_table.setColumnCount(4)
        video_table.setHorizontalHeaderLabels(["n°", "Fichier sélectionné", "Format", ""])

        # Ajoutez des lignes à la table ici en fonction du nombre de fichiers sélectionnés

        next_button = QPushButton("Suivant")
        next_button.clicked.connect(self.open_conversion_window)

        layout.addWidget(video_table)
        layout.addWidget(next_button)

        self.second_window.setLayout(layout)

    def open_conversion_window(self):
        self.stacked_widget.setCurrentIndex(2)  # Passer à la troisième fenêtre

    def init_third_window(self):
        layout = QVBoxLayout()

        self.progress_bars = []

        for i in range(3):  # Exemple avec trois barres de progression
            progress_bar = QProgressBar()
            self.progress_bars.append(progress_bar)
            layout.addWidget(progress_bar)

        done_button = QPushButton("Terminé")
        done_button.clicked.connect(self.return_to_main_window)

        layout.addWidget(done_button)

        self.third_window.setLayout(layout)

    def return_to_main_window(self):
        self.stacked_widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
