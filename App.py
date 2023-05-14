from ui import Ui_MainWindow
from PyQt5 import QtWidgets
from NewtonFractal import NewtonFractal


class App(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buld_fractal_btn.clicked.connect(self.build_fractal)
        self.fractal = NewtonFractal()

    def build_fractal(self, ) -> None:
        a = self.ui.real_edit.text()
        a = 0 if len(a) == 0 else float(a)
        b = self.ui.image_edit.text()
        b = 0 if len(b) == 0 else float(b)
        C = complex(a, b)
        R = self.ui.r_edit.text()
        R = 1e-10 if len(R) == 0 else float(R)
        # print(C, R)
        px = self.ui.doubleSpinBox.text()
        px = px.replace(',', '.')
        px = float(px)
        self.fractal.plot_fractal(c=C, r=R, px=px)
