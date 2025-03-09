from PySide6.QtCore import Qt
from PySide6.QtGui import QPen


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.graphic_item = None

    def add_to_scene(self, scene):
        self.graphic_item = scene.addEllipse(self.x - self.radius,
                                             self.y - self.radius,
                                             2 * self.radius,
                                             2 * self.radius,
                                             QPen(Qt.green))
