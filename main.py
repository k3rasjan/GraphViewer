from PySide6.QtWidgets import QApplication
from ui.MainWindow import MainWindow


def main():
    app = QApplication([])

    window = MainWindow()
    window.show()

    _ = app.exec()


if __name__ == "__main__":
    main()
