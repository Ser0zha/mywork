from PySide6.QtCore import Qt, QAbstractListModel, QModelIndex
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QListView, QMessageBox


class MyModel(QAbstractListModel):
    def __init__(self, notee=None):
        super().__init__()
        self.notee = notee or list()

    def rowCount(self, parent=QModelIndex) -> int:
        return len(self.notee)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole) -> list[int] | None:
        # Можно было использовать и
        # Qt. DisplayRole, но компилятор
        # начинает ныть

        if 0 <= index.row() < self.rowCount() and role == Qt.ItemDataRole.DisplayRole:
            return self.notee[index.row()]
        else:
            return None

    def add_note(self, note):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self.notee.append(note)
        self.endInsertRows()

    def remove_note(self, index) -> None:
        if 0 <= index.row() < self.rowCount():
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())

            del self.notee[index.row()]

            self.endRemoveRows()


class WindowAccount(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Мои заметки")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()

        self.note_for_input = QLineEdit()
        self.note_for_input.setPlaceholderText("Напиши заметку")
        layout.addWidget(self.note_for_input)

        self.button_add = QPushButton("Добавить", self)
        self.button_add.clicked.connect(self.add_button_note)
        layout.addWidget(self.button_add)

        self.note_list = QListView(self)
        self.model = MyModel()
        self.note_list.setModel(self.model)
        layout.addWidget(self.note_list)

        self.del_button = QPushButton("Удалить", self)
        self.del_button.clicked.connect(self.del_button_note)
        layout.addWidget(self.del_button)

        self.setLayout(layout)

    def add_button_note(self):
        note = self.note_for_input.text().strip()

        if note:
            self.model.add_note(note)
            self.note_for_input.clear()
        else:
            QMessageBox.warning(self, "Ошибка", "Пустая заметка")

    def del_button_note(self):
        index = self.note_list.currentIndex()

        if index.isValid():
            self.model.remove_note(index)
        else:
            QMessageBox.warning(self, "Ошибка", "Не выбрана заметка для удаления")


def main() -> None:
    app = QApplication([])
    window = WindowAccount()
    window.show()   
    app.exec()


if __name__ == "__main__":
    main()
