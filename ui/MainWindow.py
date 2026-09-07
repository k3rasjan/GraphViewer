from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from ui.graph_view import GraphView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.view: GraphView = GraphView()
        self.setCentralWidget(self.view)
