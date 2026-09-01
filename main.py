from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtWidgets import QApplication, QGraphicsEllipseItem, QGraphicsScene, QGraphicsView, QMainWindow

app = QApplication([])


scene = QGraphicsScene()
scene.setBackgroundBrush(Qt.GlobalColor.transparent)

pen = QPen(Qt.GlobalColor.black)        # Border color
pen.setWidth(2)             # Border thickness
brush = QBrush(QColor("lightblue"))  # Fill color

circle = scene.addEllipse(0,0,100,100, pen, brush)
circle.setFlag(QGraphicsEllipseItem.GraphicsItemFlag.ItemIsMovable)

view = QGraphicsView(scene)
view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
view.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
view.setStyleSheet("background: transparent; border: none;")

window = QMainWindow()
window.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
window.setCentralWidget(view)
window.show()

_ = app.exec()

