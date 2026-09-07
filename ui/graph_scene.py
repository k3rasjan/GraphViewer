import math

from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import QGraphicsScene

from ui.widgets.node import GuiNode


REPULSION_FORCE = 5000
GRAVITY = 0.01
DAMPING = 0.8
RADIUS = 400


class GraphScene(QGraphicsScene):
    def __init__(self):
        super().__init__()

        self.setBackgroundBrush(Qt.GlobalColor.transparent)

        node_list = [
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
            GuiNode(),
        ]

        self.nodes: list[GuiNode] = node_list

        self.spawn_nodes()

        self.timer: QTimer = QTimer()
        _ = self.timer.timeout.connect(self.handle_frame)
        self.timer.start(16)

    def spawn_nodes(self):
        nodes_quantity = len(self.nodes)
        for i in range(nodes_quantity):
            node = self.nodes[i]

            # Calculating initial positions around a circle of set RADIUS
            angle = (2 * math.pi / nodes_quantity) * i
            x = RADIUS * math.cos(angle)
            y = RADIUS * math.sin(angle)

            node.setPos(x, y)
            node.set_text(str(i + 1))

            self.addItem(node)
            self.handle_frame()

    def apply_central_gravity(self):
        nodes_quantity = len(self.nodes)
        for i in range(nodes_quantity):
            node = self.nodes[i]

            node.x_axis_force = 0
            node.y_axis_force = 0

            node.x_axis_force += (-node.x()) * GRAVITY
            node.y_axis_force += (-node.y()) * GRAVITY

    def apply_node_repulsion(self):
        nodes_quantity = len(self.nodes)

        for i in range(nodes_quantity):
            node_a = self.nodes[i]
            for j in range(i + 1, nodes_quantity):
                node_b = self.nodes[j]

                deltaX = node_a.x() - node_b.x()
                deltaY = node_a.y() - node_b.y()

                distance = (deltaX**2 + deltaY**2) ** 0.5

                if distance < 10:
                    distance = 10

                force = REPULSION_FORCE / (distance**2)

                # split force into x and y axis components
                force_x = (deltaX / distance) * force
                force_y = (deltaY / distance) * force

                # set forces to node a
                node_a.x_axis_force += force_x
                node_a.y_axis_force += force_y

                # set a reverse force to the second node based on the third Newtons law
                node_b.x_axis_force -= force_x
                node_b.y_axis_force -= force_y

    def handle_frame(self):

        self.apply_central_gravity()

        self.apply_node_repulsion()

        # apply forces, damping and set positions based on the velocity
        for node in self.nodes:
            node.x_axis_velocity += node.x_axis_force
            node.y_axis_velocity += node.y_axis_force

            node.x_axis_velocity *= DAMPING
            node.y_axis_velocity *= DAMPING

            node.setPos(
                node.x() + node.x_axis_velocity,
                node.y() + node.y_axis_velocity,
            )
