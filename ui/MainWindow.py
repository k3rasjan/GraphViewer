from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QMainWindow
from PySide6.QtCore import QTimer, Qt

from ui.widgets.node import GuiNode


REPULSION_FORCE = 3000
DAMPING = 0.8


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

        self.timer: QTimer = QTimer()
        _ = self.timer.timeout.connect(self.updateNodes)
        self.timer.start(16)

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setCentralWidget(self.view)

    def updateNodes(self):
        deltaX = self.node.x() - self.node2.x()
        deltaY = self.node.y() - self.node2.y()

        distance = (deltaX**2 + deltaY**2) ** 0.5

        if distance < 0.1:
            distance = 0.1

        force = REPULSION_FORCE / (distance**2)
        force_x = (deltaX / distance) * force
        force_y = (deltaY / distance) * force

        self.node.x_axis_velocity += force_x
        self.node.y_axis_velocity += force_y
        self.node2.x_axis_velocity -= force_x
        self.node2.y_axis_velocity -= force_y

        # Apply Damping
        self.node.x_axis_velocity *= DAMPING
        self.node.y_axis_velocity *= DAMPING
        self.node2.x_axis_velocity *= DAMPING
        self.node2.y_axis_velocity *= DAMPING

        self.node.setPos(
            self.node.x() + self.node.x_axis_velocity,
            self.node.y() + self.node.y_axis_velocity,
        )

        self.node2.setPos(
            self.node2.x() + self.node2.x_axis_velocity,
            self.node2.y() + self.node2.y_axis_velocity,
        )
