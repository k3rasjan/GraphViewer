from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem


class GuiNode(QGraphicsEllipseItem):
    def __init__(self, text: str = "0"):
        super().__init__()

        self.radius: int = 10
        self.margin: int = 5

        self.x_axis_force: float = 0
        self.y_axis_force: float = 0

        self.y_axis_velocity: float = 0.0
        self.x_axis_velocity: float = 0.0

        rect = QRect(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)

        self.text: QGraphicsTextItem = QGraphicsTextItem(self)
        self.text.setDefaultTextColor(Qt.GlobalColor.white)
        self.set_text(text)

        self.setRect(rect)
        self.setPos(0, 0)

        pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(2)
        brush = QBrush(Qt.GlobalColor.gray)

        # self.setPen(pen)
        self.setBrush(brush)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)

    def set_text(self, text: str):
        self.text.setPlainText(text)
        self.text.setPos(
            -(self.text.boundingRect().width() / 2), self.radius + self.margin
        )
