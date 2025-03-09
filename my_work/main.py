from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QVBoxLayout, QWidget, \
    QPushButton, QLabel, QLineEdit

from Circle import Circle
from Line import Line
from Point import Point

PATH = "./DataFile.txt"


class GeometryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Геометрические построения")
        self.setGeometry(100, 100, 1000, 1000)

        # Создаем сцену и виджет для отображения
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setSceneRect(-200, -200, 400, 400)

        # Основной виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Добавляем виджет сцены
        self.layout.addWidget(self.view)

        # Создаем элементы управления
        self.create_controls()

        # Хранение объектов
        self.objects = []

        # Загрузка примеров из файла
        self.load_data()

    def create_controls(self):
        # Кнопка для добавления точки
        self.add_point_button = QPushButton("Добавить точку")
        self.add_point_button.clicked.connect(self.add_point)

        # Поля для ввода координат точки
        self.point_x_input = QLineEdit()
        self.point_y_input = QLineEdit()
        self.layout.addWidget(QLabel("Координаты точки (x, y):"))
        self.layout.addWidget(self.point_x_input)
        self.layout.addWidget(self.point_y_input)
        self.layout.addWidget(self.add_point_button)

        # Кнопка для добавления линии
        self.add_line_button = QPushButton("Добавить линию")
        self.add_line_button.clicked.connect(self.add_line)

        # Поля для ввода координат двух точек линии
        self.line_x1_input = QLineEdit()
        self.line_y1_input = QLineEdit()
        self.line_x2_input = QLineEdit()
        self.line_y2_input = QLineEdit()
        self.layout.addWidget(QLabel("Координаты двух точек линии (x1, y1, x2, y2):"))
        self.layout.addWidget(self.line_x1_input)
        self.layout.addWidget(self.line_y1_input)
        self.layout.addWidget(self.line_x2_input)
        self.layout.addWidget(self.line_y2_input)
        self.layout.addWidget(self.add_line_button)

        # Кнопка для добавления окружности
        self.add_circle_button = QPushButton("Добавить окружность")
        self.add_circle_button.clicked.connect(self.add_circle)

        # Поля для ввода центра и радиуса окружности
        self.circle_x_input = QLineEdit()
        self.circle_y_input = QLineEdit()
        self.circle_radius_input = QLineEdit()
        self.layout.addWidget(QLabel("Центр окружности (x, y) и радиус:"))
        self.layout.addWidget(self.circle_x_input)
        self.layout.addWidget(self.circle_y_input)
        self.layout.addWidget(self.circle_radius_input)
        self.layout.addWidget(self.add_circle_button)

    @staticmethod
    def validate_input(text) -> None | float:
        try:
            return float(text)
        except ValueError:
            return None

    def add_object(self, shape_type, *params) -> None:
        if shape_type == "point":
            obj = Point(*params)
            obj.add_to_scene(self.scene)
            self.objects.append(obj)
        elif shape_type == "line":
            obj = Line(*params)
            obj.add_to_scene(self.scene)
            self.objects.append(obj)
        elif shape_type == "circle":
            obj = Circle(*params)
            obj.add_to_scene(self.scene)
            self.objects.append(obj)

    def add_point(self) -> None:
        x = self.validate_input(self.point_x_input.text())
        y = self.validate_input(self.point_y_input.text())
        if x is None or y is None:
            print("Ошибка: Введите корректные координаты точки.")
            return
        self.add_object("point", x, y)

    def add_line(self) -> None:
        x1 = self.validate_input(self.line_x1_input.text())
        y1 = self.validate_input(self.line_y1_input.text())
        x2 = self.validate_input(self.line_x2_input.text())
        y2 = self.validate_input(self.line_y2_input.text())
        if None in [x1, y1, x2, y2]:
            print("Ошибка: Введите корректные координаты точек линии.")
            return
        self.add_object("line", x1, y1, x2, y2)

    def add_circle(self) -> None:
        x = self.validate_input(self.circle_x_input.text())
        y = self.validate_input(self.circle_y_input.text())
        radius = self.validate_input(self.circle_radius_input.text())
        if None in [x, y, radius]:
            print("Ошибка: Введите корректные координаты центра и радиус окружности.")
            return
        self.add_object("circle", x, y, radius)

    def load_data(self):
        try:
            with open(PATH, 'r') as file:
                for line in file:
                    line = line.strip()
                    # Проверка на пустые строки или строки с неверным форматом
                    if not line or not ":" in line:
                        continue

                    parts = line.split(":")
                    if len(parts) != 2:
                        print(f"Неверный формат строки: {line}")
                        continue

                    shape_type, values = parts
                    values = values.strip()

                    # Обработка точек
                    if shape_type == "point":
                        try:
                            x, y = map(float, values.split(","))
                            self.add_object("point", x, y)
                        except ValueError:
                            print(f"Неверный формат координат для точки: {values}")
                            continue

                    # Обработка линий
                    elif shape_type == "line":
                        try:
                            x1, y1, x2, y2 = map(float, values.split(","))
                            self.add_object("line", x1, y1, x2, y2)
                        except ValueError:
                            print(f"Неверный формат координат для линии: {values}")
                            continue

                    # Обработка окружностей
                    elif shape_type == "circle":
                        try:
                            x, y, radius = map(float, values.split(","))
                            self.add_object("circle", x, y, radius)
                        except ValueError:
                            print(f"Неверный формат данных для окружности: {values}")
                            continue
                    else:
                        print(f"Неизвестный тип объекта: {shape_type}")
        except FileNotFoundError:
            print(f"Файл {PATH} не найден.")


def main():
    app = QApplication([])
    window = GeometryApp()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
