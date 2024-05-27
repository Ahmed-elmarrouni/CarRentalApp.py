import sys
from PyQt5 import QtWidgets
from location import Ui_LOCATION_DE_VOITURE
import mysql.connector


class Test(QtWidgets.QMainWindow, Ui_LOCATION_DE_VOITURE):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='auto'
        )
        cursor = connection.cursor()
        voitureQuery = "SELECT * FROM voiture"

        cursor.execute(voitureQuery)
        allVoitures = cursor.fetchall()
        if not allVoitures:
            self.VOITURE_listWidget.addItem("No voiture found")
        else:
            self.VOITURE_listWidget.clear()

        for row in allVoitures:
            # VOITURE TABLE

            VOITURE_ID = row[0]
            VOITURE_MAT = row[1]
            VOITURE_COLOR = row[2]
            VOITURE_MODEL = row[3]
            VOITURE_YEAR = row[4]
            VOITURE_MARQUE = row[5]

            allVoiture_text = f"==>.Voiture ID: {VOITURE_ID} , Voiture Matricule: {VOITURE_MAT} , Voiture Color: {VOITURE_COLOR} ,\n Voiture Model: {VOITURE_MODEL} , Voiture Year : {VOITURE_YEAR} , Voiture Marque : {VOITURE_MARQUE} \n"
            self.VOITURE_listWidget.addItem(allVoiture_text)

        self.VOITURE_listWidget.itemClicked.connect(self.selectedVoitureClick)
        connection.close()

    # Write the selected voiture information
    def selectedVoitureClick(self, item):
        selected_text = item.text()

        mat = selected_text.split(':')[2].split(',')[0].strip()
        self.VOITURE_MAT_input.setText(mat)

        color = selected_text.split(':')[3].split(',')[0].strip()
        self.VOITURE_COLOR_input.setText(color)

        model = selected_text.split(':')[4].split(',')[0].strip()
        self.VOITURE_MODEL_input.setText(model)

        year = selected_text.split(':')[5].split(',')[0].strip()
        self.VOITURE_YEAR_input.setText(year)

        marque = selected_text.split(':')[6].split(',')[0].strip()
        self.VOITURE_MARQUE_input.setText(marque)

        # ----------------------BUTTONS----------------------------------------
        self.Add_btn.clicked.connect(self.add_click)
        self.Delete_btn.clicked.connect(self.delete_click)

    # ADD BUTTON
    def add_click(self):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='auto'
        )

        # INPUTS
        voitureMat = self.VOITURE_MAT_input.text()
        voitureColor = self.VOITURE_COLOR_input.text()
        voitureModel = self.VOITURE_MODEL_input.text()
        voitureYear = self.VOITURE_YEAR_input.text()
        voitureMarque = self.VOITURE_MARQUE_input.text()

        if voitureMat == "" and voitureColor == "" and voitureModel == "" and voitureYear == "" and voitureMarque == "":
            # Show message box if all input empty
            QtWidgets.QMessageBox.warning(
                self, '^_^', 'All input is empty \n Please enter voiture information')
        else:
            m = "INSERT INTO voiture (VOITURE_MAT, VOITURE_COLOR, VOITURE_MODEL, VOITURE_YEAR, VOITURE_MARQUE) VALUES (%s, %s, %s, %s, %s)"
            data = (
                voitureMat,
                voitureColor,
                voitureModel,
                voitureYear,
                voitureMarque,
            )

            cursor = connection.cursor()
            cursor.execute(m, data)
            connection.commit()
            QtWidgets.QMessageBox.information(
                self, 'Success', 'Data has been successfully inserted into the database.'
            )

        connection.close()

    # DELETE BUTTON

    def delete_click(self):

        voitureMatricule = self.VOITURE_MAT_input.text()

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='auto')

        cursor = connection.cursor()
        if voitureMatricule == "":
            QtWidgets.QMessageBox.warning(
                self, 'Input is empty', 'Please enter Matricule de voiture to delete item.')
        else:
            query = "SELECT * FROM voiture WHERE  VOITURE_MAT= %s"
            params = (voitureMatricule,)

            cursor.execute(query, params)
            result = cursor.fetchone()
            if result is not None:
                msg_box = QtWidgets.QMessageBox.question(self, 'Confirmation', 'Are you sure you want to delete this voiture?',
                                                         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
                # If user click on the "Yes" button the item is deleted
                if msg_box == QtWidgets.QMessageBox.Yes:
                    query = "DELETE FROM voiture WHERE VOITURE_MAT = %s"
                    cursor.execute(query, params)
                    connection.commit()
                    QtWidgets.QMessageBox.information(
                        self, 'Success', 'voiture deleted successfully.')

                else:
                    QtWidgets.QMessageBox.warning(
                        self, 'Error', 'thiis matricule not found in the voiture Table.')

        cursor.close()
        connection.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    client = Test()
    client.show()
    sys.exit(app.exec_())
