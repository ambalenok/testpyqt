import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QGridLayout, QApplication, QPushButton, QDateEdit)


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        doc = QLabel('ФИО врача')
        pat = QLabel('ФИО пациента')
        date = QLabel('дата рождения')
        self.docEdit = QLineEdit()
        self.patEdit = QLineEdit()
        self.dateEdit = QDateEdit()
        addDataButton = QPushButton("Показать данные")
        addDataButton.clicked.connect(self.showData)
        grid = QGridLayout()
        grid.setSpacing(1)

        grid.addWidget(doc, 1, 0)
        grid.addWidget(self.docEdit, 1, 1)

        grid.addWidget(pat, 2, 0)
        grid.addWidget(self.patEdit, 2, 1)

        grid.addWidget(date, 3, 0)
        grid.addWidget(self.dateEdit, 3, 1)

        grid.addWidget(addDataButton, 4, 0, 1, 5)

        self.setLayout(grid)

        self.setGeometry(200, 200, 350, 300)
        self.setWindowTitle('Test')
        self.show()

    def showData(self):
        print("ФИО врача - %s\nФИО пациента - %s\nДата рождения: %s" % (
            self.docEdit.text(), self.patEdit.text(), self.dateEdit.text()))

    def keyPressEvent(self, e):  # Вывод в консоль по нажатию клавиши Enter
        if e.key() == Qt.Key_Return:  # What? Return = Enter
            self.showData()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
