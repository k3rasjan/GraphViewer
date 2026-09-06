from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem


class GuiNode(QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()

        self.y_axis_velocity: float = 0.0
        self.x_axis_velocity: float = 0.0

        rect = QRect(-50, -50, 100, 100)

        self.setRect(rect)
        self.setPos(0, 0)

        pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(2)
        brush = QBrush(Qt.GlobalColor.blue)

        self.setPen(pen)
        self.setBrush(brush)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
