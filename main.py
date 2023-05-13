from PyQt5 import QtWidgets

from App import App
import sys

app = QtWidgets.QApplication([])
application = App()
application.show()

sys.exit(app.exec())
