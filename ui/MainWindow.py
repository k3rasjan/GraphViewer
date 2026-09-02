from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow
from PySide6.QtCore import Qt

from ui.widgets.node import GuiNode


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.scene: QGraphicsScene = QGraphicsScene()
        self.scene.setBackgroundBrush(Qt.GlobalColor.transparent)

        self.node: GuiNode = GuiNode()
        self.scene.addItem(self.node)

        self.node2: GuiNode = GuiNode()
        self.node2.setPos(50, 0)
        self.scene.addItem(self.node2)

        self.view: QGraphicsView = QGraphicsView(self.scene)
        self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.view.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.view.setStyleSheet("background: transparent; border: none;")

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setCentralWidget(self.view)
