import math
import random

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QGraphicsScene

from ui.widgets.node import GuiNode


REPULSION_FORCE = 3000
DAMPING = 0.8

node_list = [
    GuiNode(),
    GuiNode(),
    GuiNode(),
    GuiNode(),
    GuiNode(),
    GuiNode(),
    GuiNode(),
    GuiNode(),
]


class GraphScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.nodes: list[GuiNode] = node_list

        self.spawn_nodes()

        self.setBackgroundBrush(Qt.GlobalColor.transparent)

        self.timer: QTimer = QTimer()
        _ = self.timer.timeout.connect(self.handle_frame)
        self.timer.start(16)

    def spawn_nodes(self):
        RADIUS = 100
        nodes_quantity = len(self.nodes)
        for i in range(nodes_quantity):
            node = self.nodes[i]

            angle = (2 * math.pi / nodes_quantity) * i
            x = RADIUS * math.cos(angle)
            y = RADIUS * math.sin(angle)

            node.setPos(x, y)

            self.addItem(node)
            self.handle_frame()

    def handle_frame(self):
        nodes_quantity = len(self.nodes)
        for i in range(nodes_quantity):
            node_a = self.nodes[i]
            for j in range(i + 1, nodes_quantity):
                node_b = self.nodes[j]

                deltaX = node_a.x() - node_b.x()
                deltaY = node_a.y() - node_b.y()

                distance = (deltaX**2 + deltaY**2) ** 0.5

                if distance < 0.1:
                    distance = 0.1
                    deltaX = random.uniform(-0.1, 0.1)
                    deltaY = random.uniform(-0.1, 0.1)

                force = REPULSION_FORCE / (distance**2)
                force_x = (deltaX / distance) * force
                force_y = (deltaY / distance) * force

                node_a.x_axis_velocity += force_x
                node_a.y_axis_velocity += force_y
                node_b.x_axis_velocity -= force_x
                node_b.y_axis_velocity -= force_y

                node_a.x_axis_velocity *= DAMPING
                node_a.y_axis_velocity *= DAMPING
                node_b.x_axis_velocity *= DAMPING
                node_b.y_axis_velocity *= DAMPING

        for node in self.nodes:
            node.setPos(
                node.x() + node.x_axis_velocity,
                node.y() + node.y_axis_velocity,
            )
