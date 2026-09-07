from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem, QGraphicsTextItem


class GuiNode(QGraphicsEllipseItem):
    def __init__(self, text: str = "0"):
        super().__init__()

        # Styles
        brush = QBrush(Qt.GlobalColor.gray)

        self.setBrush(brush)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)

        # Initialize properties
        self.radius: int = 10
        self.margin: int = 5

        self.x_axis_force: float = 0
        self.y_axis_force: float = 0

        self.y_axis_velocity: float = 0.0
        self.x_axis_velocity: float = 0.0

        # Set personal rect with the position relative to the center of the ellipse
        rect = QRect(-self.radius, -self.radius, 2 * self.radius, 2 * self.radius)
        self.setRect(rect)

        self.text: QGraphicsTextItem = QGraphicsTextItem(self)
        self.text.setDefaultTextColor(Qt.GlobalColor.white)
        self.set_text(text)

        # Set defaults
        self.setPos(0, 0)

    def set_text(self, text: str):
        self.text.setPlainText(text)
        self.text.setPos(
            -(self.text.boundingRect().width() / 2), self.radius + self.margin
        )
