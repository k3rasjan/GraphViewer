from PySide6.QtWidgets import QApplication
from ui.MainWindow import MainWindow

app = QApplication([])

window = MainWindow()
window.show()

_ = app.exec()

