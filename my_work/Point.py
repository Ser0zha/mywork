from PySide6.QtCore import Qt
from PySide6.QtGui import QPen, QBrush


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.graphic_item = None

    def add_to_scene(self, scene):
        self.graphic_item = scene.addEllipse(self.x - 2,
                                             self.y - 2, 4, 4,
                                             QPen(Qt.black),
                                             QBrush(Qt.red))
