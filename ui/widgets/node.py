from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QPen
from PySide6.QtWidgets import QGraphicsEllipseItem


class GuiNode(QGraphicsEllipseItem):
    def __init__(self):
        super().__init__()
        self.setRect(0,0,100,100)
        pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(2)
        brush = QBrush(Qt.GlobalColor.blue)
        self.setPen(pen) 
        self.setBrush(brush)
        self.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)
    
