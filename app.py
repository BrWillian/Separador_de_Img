import classify_1
import classify_2
import classify_3
import classify_4
import list_dir
import sys
import os
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

class Separador(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.caminho = ''
        self.pushButton_2.clicked.connect(self.abrir_imagem)
        self.pushButton.clicked.connect(self.processar)

    def abrir_imagem(self):
        self.caminho = QFileDialog.getExistingDirectory(
            self.centralwidget,
            'Selecione caminho das imagens',
            rf'{os.getcwd()}'
        )
        self.lineEdit.setText(self.caminho)

    def processar(self):
        if self.caminho == '':
            self.MessageBox.warning(None, 'Separador', 'Selecione um diretorio')
            return
        try:
            list_dir.list_dir(self.caminho)
            self.progressBar.setValue(20)
            classify_1.func_filter_dir(self.caminho)
            self.progressBar.setValue(40)
            classify_2.func_filter_dir(self.caminho)
            self.progressBar.setValue(60)
            classify_3.func_filter_dir(self.caminho)
            self.progressBar.setValue(80)
            classify_4.func_filter_dir(self.caminho)
            self.progressBar.setValue(100)
            os.removedirs(self.caminho + '/cache/')
            self.MessageBox.setText('Finalizado!')
            clicked = self.MessageBox.exec()
            if clicked == QMessageBox.Ok:
                self.progressBar.setValue(0)
                self.lineEdit.setText('')
        except:
            self.MessageBox.warning(None, 'Separador', 'Diretorio Invalido')
            self.progressBar.setValue(0)
            return

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    separador = Separador()
    separador.show()
    qt.exec_()
