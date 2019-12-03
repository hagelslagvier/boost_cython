
def run():
    import sys
    from PyQt5.QtWidgets import QApplication

    from gui.DialogMain import DialogMain

    application = QApplication(sys.argv)

    mainDialog = DialogMain()
    mainDialog.show()

    sys.exit(application.exec_())
