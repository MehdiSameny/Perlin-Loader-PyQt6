# ///////////////////////////////////////////////////////////////
# Developer: Mehdi Sameni
# Designer: Mehdi Sameni
# PyQt6
# Python 3.10
# other module : perlin_noise
# ///////////////////////////////////////////////////////////////



from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QFrame, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QColor
from Perlin_Loader import PerlinLoader


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        layout = QVBoxLayout(self)
        frame = QFrame(self)
        layoutF = QVBoxLayout(frame)
        layout.addWidget(frame)
        loader = PerlinLoader(frame,message="LOADING ...",
                              fontSize=22,
                              circleColor1=QColor("#ff2e63"),
                              circleColor2=QColor("#082e63"),
                              circleColor3=QColor(57, 115, 171, 100)
                              )
        layoutF.addWidget(loader)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
