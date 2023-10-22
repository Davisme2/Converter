import os
import threading
import time

from PyQt5.QtCore import QTimer
from moviepy.editor import VideoFileClip
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QTableWidget, \
    QStackedWidget, QMessageBox, QWidget, QProgressBar, QComboBox
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1254, 888)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setStyleSheet("background-color: rgb(40, 40, 42);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 770, 171, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 15pt \"Roboto\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file_dialog)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 770, 161, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "font: 15pt \"Roboto\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.file_converter)

        # TABLE BUILDING
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 50, 1141, 595))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setColumnWidth(0, 582)
        self.tableWidget.setColumnWidth(1, 107)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 150)

        # Supprimer la numérotation des lignes
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        # Rendre toutes les cellules non sélectionnables après avoir configuré la table
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 660, 831, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "font: 19pt \"Roboto\";")
        self.lineEdit.setObjectName("lineEdit")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 660, 191, 31))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "font: 15pt \"Roboto\";")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1120, 660, 51, 41))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(11, 69, 95);\n"
                                        "font: 15pt \"Roboto\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.open_folder_output_dialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 26))
        self.menubar.setObjectName("menubar")
        self.menuFICHIER = QtWidgets.QMenu(self.menubar)
        self.menuFICHIER.setObjectName("menuFICHIER")
        self.menuAIDE = QtWidgets.QMenu(self.menubar)
        self.menuAIDE.setObjectName("menuAIDE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFICHIER.menuAction())
        self.menubar.addAction(self.menuAIDE.menuAction())

        # Générer les 14 premières lignes vides
        for i in range(0, 16):
            self.tableWidget.insertRow(i)

        # Définir la couleur de fond pour les cellules "Nom du fichier", "format", "Taille", "Statut", "Temps restant"
        cell_background_color = QtGui.QBrush(QtGui.QColor("#bcdcf4"))

        # Colonne 0 : "Nom du fichier"
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("Nom du fichier"))
        self.tableWidget.item(0, 0).setBackground(cell_background_color)
        self.tableWidget.item(0, 0).setTextAlignment(QtCore.Qt.AlignCenter)

        # Colonne 1 : "format"
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("format"))
        self.tableWidget.item(0, 1).setBackground(cell_background_color)
        self.tableWidget.item(0, 1).setTextAlignment(QtCore.Qt.AlignCenter)

        # Colonne 2 : "Taille"
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem("Taille"))
        self.tableWidget.item(0, 2).setBackground(cell_background_color)
        self.tableWidget.item(0, 2).setTextAlignment(QtCore.Qt.AlignCenter)

        # Colonne 3 : "Statut"
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem("Statut"))
        self.tableWidget.item(0, 3).setBackground(cell_background_color)
        self.tableWidget.item(0, 3).setTextAlignment(QtCore.Qt.AlignCenter)

        # Colonne 4 : "Temps restant"
        self.tableWidget.setItem(0, 4, QtWidgets.QTableWidgetItem("Temps restant"))
        self.tableWidget.item(0, 4).setBackground(cell_background_color)
        self.tableWidget.item(0, 4).setTextAlignment(QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1254, 26))
        self.menubar.setObjectName("menubar")
        self.menuFICHIER = QtWidgets.QMenu(self.menubar)
        self.menuFICHIER.setObjectName("menuFICHIER")
        self.menuAIDE = QtWidgets.QMenu(self.menubar)
        self.menuAIDE.setObjectName("menuAIDE")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFICHIER.menuAction())
        self.menubar.addAction(self.menuAIDE.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_status(self, row, percentage, remaining_time):
        if percentage < 100:
            status = f"{percentage}% ({remaining_time} restants)"
        else:
            status = "Converti"

        status_item = QtWidgets.QTableWidgetItem(status)
        self.tableWidget.setItem(row, 3, status_item)

    def open_file_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ReadOnly

        file_dialog = QtWidgets.QFileDialog()
        video_files, _ = file_dialog.getOpenFileNames(None, "Sélectionner des fichiers média", "",
                                                      "Fichiers Média (*.mp4 *.avi *.mkv *.mp3 *.wav *.mov);;Tous les fichiers (*)",
                                                      options=options)

        if video_files:
            self.selected_files = video_files

            # Ajoutez une nouvelle ligne pour chaque fichier sélectionné
            # for i, file_path in enumerate(self.selected_files):

            # Recherche de la première ligne vide (i + 1, car la première ligne est déjà occupée)
            current_row = 1
            while self.tableWidget.item(current_row, 0) is not None:
                current_row += 1

            for file_path in self.selected_files:
                if current_row >= self.tableWidget.rowCount():
                    # Vous pouvez ajouter du code ici pour gérer la situation si toutes les lignes sont déjà occupées.
                    self.tableWidget.insertRow(current_row)
                    # Par exemple, afficher un message d'erreur ou augmenter la taille de la table.
                    # Pour l'instant, nous supposons que vous gérez le cas où toutes les lignes sont occupées.

                file_name = os.path.basename(file_path)

                # Colonne 1 : Noms des fichiers
                item = QtWidgets.QTableWidgetItem(file_name)
                # item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable(False))
                self.tableWidget.setItem(current_row, 0, item)

                # Colonne 2 : Format de fichier à convertir
                # Créez une liste de formats multimédias
                multimedia_formats = ["*.mp4", "*.avi", "*.mkv", "*.mp3", "*.wav", "*.mov"]
                # Ajoutez d'autres formats si nécessaire
                # Créez un QComboBox et ajoutez les formats multimédias à l'intérieur
                format_combobox = QtWidgets.QComboBox()
                format_combobox.addItems(multimedia_formats)
                # Insérez le QComboBox dans la cellule de la deuxième ligne de la colonne "format"
                self.tableWidget.setCellWidget(current_row, 1, format_combobox)

                # Colonne : Taille des fichiers
                file_size = os.path.getsize(file_path)
                item = QtWidgets.QTableWidgetItem(str(file_size))
                # Convertir la taille en méga-octets (Mo) ou giga-octets (Go)
                if file_size >= 1024 ** 3:  # Si la taille est supérieure ou égale à 1 Go
                    size_str = f"{file_size / (1024 ** 3):.2f} Go"
                else:  # Sinon, convertir en Mo
                    size_str = f"{file_size / (1024 ** 2):.2f} Mo"
                item = QtWidgets.QTableWidgetItem(size_str)
                # item.setFlags(item.flags() & ~QtCore.Qt.ItemIsSelectable(False))
                self.tableWidget.setItem(current_row, 2, item)
                self.tableWidget.item(current_row, 2).setTextAlignment(QtCore.Qt.AlignCenter)

                # Colonne : Statut
                # afficher au départ dans la cellule de la colonne status "Convertir"
                self.tableWidget.setItem(current_row, 3, QtWidgets.QTableWidgetItem("Convertir ..."))
                self.tableWidget.item(current_row, 3).setTextAlignment(QtCore.Qt.AlignCenter)

                # Colonne : Temps restant
                # Afficher au départ dans la cellule de la colonne status "Démarrer"
                self.tableWidget.setItem(current_row, 4, QtWidgets.QTableWidgetItem("Démarrer"))
                self.tableWidget.item(current_row, 4).setTextAlignment(QtCore.Qt.AlignCenter)
                # Calculez la ligne courante en fonction de la position du fichier dans la liste
                # current_row = self.selected_files.index(file_path) + 1

                # Appelez file_converter pour convertir chaque fichier
                self.file_converter(file_path, current_row, 4)

                current_row += 1  # Passe à la prochaine ligne libre pour le prochain fichier

            print("Vidéos sélectionnées :", self.selected_files)

    """
    def open_folder_dialog(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, "Sélectionner un dossier de destination", "", QtWidgets.QFileDialog.ShowDirsOnly)

        if folder_path:
            # Le chemin du dossier sélectionné par l'utilisateur est stocké dans la variable "folder_path"
            print("Dossier de destination sélectionné :", folder_path)
    """

    def open_folder_output_dialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.ShowDirsOnly

        folder_dialog = QtWidgets.QFileDialog()
        folder_path = folder_dialog.getExistingDirectory(None, "Sélectionner le dossier de destination",
                                                         options=options)

        if folder_path:
            # Mettez à jour le champ de saisie pour afficher le chemin du dossier sélectionné
            self.lineEdit.setText(folder_path)
            # Le chemin du dossier sélectionné par l'utilisateur est stocké dans la variable "folder_path"
            print("Dossier de destination sélectionné :", folder_path)

    """
    def file_converter(self):
        # Obtenez le dossier de destination à partir du champ de saisie
        folder_path = self.lineEdit.text()

        # Vérifiez que le dossier de destination est spécifié
        if not folder_path:
            QtWidgets.QMessageBox.critical(None, "Erreur", "Veuillez sélectionner un dossier de destination.")
            return

        # Recherchez les fichiers sélectionnés dans la table
        for row in range(1, self.tableWidget.rowCount()):  # Commencez depuis la ligne 1

            # Vérifiez si la colonne "Statut" contient "En cours ..." pour éviter de reconvertir
            status_item = self.tableWidget.item(row, 3)
            if status_item and status_item.text() == "En cours ...":
                continue

            # Obtenez le chemin du fichier à partir de la colonne "Nom du fichier"
            file_name_item = self.tableWidget.item(row, 0)
            if file_name_item:
                input_file = file_name_item.text()

                # Continuez seulement si l'extension est valide, vous devez remplacer ".extension_actuelle" par le vrai format
                if input_file.endswith(".extension_actuelle"):
                    # Récupérez le format sélectionné dans la colonne "format" (ici, nous utilisons "format_selection" pour illustrer)
                    format_selection = "mp4"  # Remplacez ceci par le vrai format choisi

                    # Formatez le chemin de sortie avec le dossier de destination
                    output_file = os.path.join(folder_path,
                                               f"{input_file.replace('.extension_actuelle', f'.{format_selection}')}")

                    try:
                        # Charger la vidéo d'entrée
                        video = VideoFileClip(input_file)

                        # Calculer la durée de la vidéo en secondes
                        video_duration = video.duration

                        # Convertir la vidéo dans le format de sortie choisi
                        video.write_videofile(output_file, codec="libx264", progress_bar=False)

                        # Mettez à jour la colonne "Statut" pour afficher "En cours ..." dès le début
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("En cours ..."))

                        # Mettez à jour la cellule de statut avec "Converti" lorsque la conversion est terminée
                        status_item = QtWidgets.QTableWidgetItem("Converti")
                        self.tableWidget.setItem(row, 3, status_item)
                        # self.update_status(row, 100, "0:00")  # 100% indique que la conversion est terminée

                        print(f"Conversion réussie : {input_file} -> {output_file}")

                    except Exception as e:
                        # En cas d'erreur, affichez un message d'erreur dans la colonne "Statut"
                        status_item = QtWidgets.QTableWidgetItem(f"Erreur: {str(e)}")
                        self.tableWidget.setItem(row, 3, status_item)
                        print(f"Erreur de conversion : {input_file} -> {output_file}, {str(e)}")

                    finally:
                        # Réinitialisez le pourcentage à 0% une fois la conversion terminée
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("100%"))


        # Créez un thread pour effectuer la conversion
        conversion_thread = threading.Thread(target=convert_video)
        conversion_thread.start()

        # Démarrez le chronomètre pour mesurer le temps écoulé
        start_time = time.time()

        # Attendez la fin de la conversion
        conversion_thread.join()

        # Calculez le temps écoulé en secondes
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Calculez le temps restant
        remaining_time = video_duration - elapsed_time

        # Mettez à jour la cellule de statut avec le temps restant
        self.update_status(row, 100, f"{int(remaining_time // 60)}:{int(remaining_time % 60):02d}")

    """

    def file_converter(self, input_file, row, column):
        # Obtenez le dossier de destination à partir du champ de saisie
        folder_path = self.lineEdit.text()

        # Vérifiez que le dossier de destination est spécifié
        if not folder_path:
            QtWidgets.QMessageBox.critical(None, "Erreur", "Veuillez sélectionner un dossier de destination.")
            return

        # Récupérez le format sélectionné dans la colonne "format" (remplacez "format_selection" par le vrai format
        # choisi)
        format_combobox = self.tableWidget.cellWidget(row, 1)
        format_selection = format_combobox.currentText()

        # Formatez le chemin de sortie avec le dossier de destination
        output_file = os.path.join(folder_path,
                                   os.path.splitext(os.path.basename(input_file))[0] + '.' + format_selection)

        # Créez un thread pour effectuer la conversion
        conversion_thread = threading.Thread(target=self.convert_video, args=(input_file, output_file, row))
        conversion_thread.start()

        self.tableWidget.setItem(row, column, QtWidgets.QTableWidgetItem("Démarrer"))
        self.tableWidget.item(row, column).setTextAlignment(QtCore.Qt.AlignCenter)

    def convert_video(self, input_file, output_file, row):
        try:
            video = VideoFileClip(input_file)
            video_duration = video.duration

            # Mettez à jour la colonne "Statut" pour afficher "En cours ..." dès le début
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("En cours ..."))

            # Initialisez le minuteur pour mettre à jour le temps restant
            timer = QTimer(self)
            timer.timeout.connect(lambda: self.update_remaining_time(row, video_duration))
            timer.start(1000)  # Mise à jour toutes les 1 seconde

            video.write_videofile(output_file, codec="libx264", progress_bar=False)

            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem("Converti"))

        except Exception as e:
            status_item = QtWidgets.QTableWidgetItem(f"Erreur: {str(e)}")
            self.tableWidget.setItem(row, 3, status_item)
            print(f"Erreur de conversion : {input_file} -> {output_file}, {str(e)}")

    def update_remaining_time(self, row, video_duration):
        # Calculez le temps restant
        current_time = time.time()
        start_time = self.start_times.get(row, current_time)
        self.start_times[row] = start_time

        elapsed_time = current_time - start_time
        remaining_time = video_duration - elapsed_time

        # Mettez à jour la colonne "Temps restant"
        remaining_time_str = f"{int(remaining_time // 60)}:{int(remaining_time % 60):02d}"
        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(remaining_time_str))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "sélectionner"))
        self.pushButton_2.setText(_translate("MainWindow", "convertir"))
        self.label.setText(_translate("MainWindow", "Enregistrer sous"))
        self.pushButton_3.setText(_translate("MainWindow", "..."))
        self.menuFICHIER.setTitle(_translate("MainWindow", "FICHIER"))
        self.menuAIDE.setTitle(_translate("MainWindow", "AIDE"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())