from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsView

from ui.graph_scene import GraphScene


class GraphView(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.setScene(GraphScene())

        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setStyleSheet("background: transparent; border: none;")
