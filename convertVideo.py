# main.py

import sys
import ffmpeg
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QWidget, QVBoxLayout, QTableWidget, \
    QTableWidgetItem, QProgressBar


class ConversionWindow(QMainWindow):
    def __init__(self, selected_videos, selected_formats):
        super().__init__()
        self.setWindowTitle("Conversion en cours")
        self.selected_videos = selected_videos
        self.selected_formats = selected_formats
        self.completed_videos = 0

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.progress_bars = []

        for video, format in zip(self.selected_videos, self.selected_formats):
            progress_bar = QProgressBar(self)
            progress_bar.setMaximum(100)
            self.progress_bars.append(progress_bar)
            self.layout.addWidget(progress_bar)

            self.convert_video(video, format, progress_bar)

        self.done_button = QPushButton("Terminé", self)
        self.done_button.setDisabled(True)  # Le bouton est désactivé initialement
        self.done_button.clicked.connect(self.return_to_main_window)

        self.layout.addWidget(self.done_button)

        self.central_widget.setLayout(self.layout)

    def convert_video(self, input_file, output_format, progress_bar):
        try:
            input_file_ext = input_file.split('.')[-1]
            output_file = f"output.{output_format}"

            ffmpeg.input(input_file).output(output_file, **{'c:v': 'libx264', 'c:a': 'aac'}).run(overwrite_output=True,
                                                                                                 cmd='ffmpeg')

            for i in range(101):
                time.sleep(0.1)
                progress_bar.setValue(i)

            self.completed_videos += 1

            if self.completed_videos == len(self.selected_videos):
                self.done_button.setEnabled(True)

        except Exception as e:
            print(f"Erreur de conversion : {str(e)}")

    def return_to_main_window(self):
        self.hide()
        main_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
