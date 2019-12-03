from PyQt5.QtWidgets import QDialog

from gui.Ui_DialogMain import Ui_DialogMain


class DialogMain(QDialog, Ui_DialogMain):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.setupUi(self)
        self.__customize()

    def __customize(self):
        self.lineEdit.setText('Hello there')

        self.pushButton.clicked.connect(self.__onPushButtonClicked)

    def __onPushButtonClicked(self):
        self.textEdit.append(self.lineEdit.text())
        self.lineEdit.clear()


if '__main__' == __name__:
    import sys
    from PyQt5.QtWidgets import QApplication

    application = QApplication(sys.argv)

    mainDialog = DialogMain()
    mainDialog.show()

    sys.exit(application.exec_())