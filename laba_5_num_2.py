from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QTableView, QLineEdit, QPushButton, QLabel,
                               QFormLayout, QMessageBox)


class Product:
    def __init__(self, name, quantity, weight_per_unit):
        self.name = name
        self.quantity = quantity
        self.weight_per_unit = weight_per_unit

    def total_weight(self):
        return self.quantity * self.weight_per_unit


class ProductModel(QAbstractTableModel):
    def __init__(self, products=None):
        super().__init__()
        self.products = products or []

    def rowCount(self, parent=None):
        return len(self.products)

    def columnCount(self, parent=None):
        return 4  # Название, Количество, Вес единицы, Общий вес

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            product = self.products[index.row()]
            if index.column() == 0:
                return product.name
            elif index.column() == 1:
                return str(product.quantity)
            elif index.column() == 2:
                return f"{product.weight_per_unit} кг"
            elif index.column() == 3:
                return f"{product.total_weight()} кг"
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return ["Название", "Количество", "Вес единицы", "Общий вес"][section]
        return None

    def add_product(self, product):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.products.append(product)
        self.endInsertRows()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учёт продуктов")
        self.setGeometry(100, 100, 600, 400)

        # Основной layout
        layout = QVBoxLayout()

        # Форма для ввода данных
        self.form_layout = QFormLayout()

        self.name_input = QLineEdit(self)
        self.form_layout.addRow("Название продукта:", self.name_input)

        self.quantity_input = QLineEdit(self)
        self.form_layout.addRow("Количество:", self.quantity_input)

        self.weight_input = QLineEdit(self)
        self.form_layout.addRow("Вес единицы (кг):", self.weight_input)

        layout.addLayout(self.form_layout)

        # Кнопка добавления продукта
        self.add_button = QPushButton("Добавить продукт", self)
        self.add_button.clicked.connect(self.on_add)
        layout.addWidget(self.add_button)

        # Таблица для отображения продуктов
        self.table_view = QTableView(self)
        self.model = ProductModel()
        self.table_view.setModel(self.model)
        layout.addWidget(self.table_view)

        # Метка для отображения общего веса
        self.total_weight_label = QLabel("Общий вес: 0 кг", self)
        layout.addWidget(self.total_weight_label)

        self.setLayout(layout)

    def on_add(self):
        """Обработчик нажатия на кнопку 'Добавить продукт'."""
        name = self.name_input.text().strip()
        quantity = self.quantity_input.text().strip()
        weight = self.weight_input.text().strip()

        # Проверка ввода
        if not name or not quantity or not weight:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return

        try:
            quantity = int(quantity)
            weight = float(weight)
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Количество и вес должны быть числами!")
            return

        # Добавление продукта
        product = Product(name, quantity, weight)
        self.model.add_product(product)

        # Очистка полей ввода
        self.name_input.clear()
        self.quantity_input.clear()
        self.weight_input.clear()

        # Пересчёт общего веса
        self.update_total_weight()

    def update_total_weight(self):
        """Пересчитывает и обновляет общий вес продуктов."""
        total_weight = sum(product.total_weight() for product in self.model.products)
        self.total_weight_label.setText(f"Общий вес: {total_weight} кг")


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec_()
