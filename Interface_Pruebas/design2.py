from PyQt5 import QtCore, QtGui, QtWidgets

#----------------------------------------------------------------------------------------------------------------------------------------------------------
class Ui_PDFtoCSV(object):
    def setupUi(self, PDFtoCSV):
        PDFtoCSV.setObjectName("PDFtoCSV")
        PDFtoCSV.resize(490, 155)
        self.centralwidget = QtWidgets.QWidget(PDFtoCSV)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 70, 361, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.comenzar = QtWidgets.QPushButton(self.centralwidget)
        self.comenzar.setGeometry(QtCore.QRect(400, 70, 75, 31))
        self.comenzar.setObjectName("comenzar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 451, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 171, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.folder = QtWidgets.QTextEdit(self.centralwidget)
        self.folder.setGeometry(QtCore.QRect(20, 30, 451, 31))
        self.folder.setObjectName("folder")
        PDFtoCSV.setCentralWidget(self.centralwidget)

        self.retranslateUi(PDFtoCSV)
        QtCore.QMetaObject.connectSlotsByName(PDFtoCSV)

    def retranslateUi(self, PDFtoCSV):
        _translate = QtCore.QCoreApplication.translate
        PDFtoCSV.setWindowTitle(_translate("PDFtoCSV", "PDF to CSV "))
        self.label.setText(_translate("PDFtoCSV", "Path del directorio:"))
        self.comenzar.setText(_translate("PDFtoCSV", "Comenzar"))
        self.label_3.setText(_translate("PDFtoCSV", "© Eliaz Bobadilla 2021"))
        self.label_4.setText(_translate("PDFtoCSV", " Archivos Procesados"))
        self.folder.setHtml(_translate("PDFtoCSV", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Borra esto y escribe el PATH aqui</span></p></body></html>"))
#----------------------------------------------------------------------------------------------------------------------------------------------------------
def run():
        self.gui = Ui_PDFtoCSV()


if __name__ == "__main__":
    run()