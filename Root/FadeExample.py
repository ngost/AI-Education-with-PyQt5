import sys
from PyQt5.QtCore import QTimeLine
from PyQt5.QtGui import *
from PyQt5 import QtWidgets



class FaderWidget(QtWidgets.QWidget):

    def __init__(self, old_widget, new_widget):
        QtWidgets.QWidget.__init__(self, new_widget)

        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0

        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(333)
        self.timeline.start()

        self.resize(new_widget.size())
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()

    def animate(self, value):
        self.pixmap_opacity = 1.0 - value
        self.repaint()


class StackedWidget(QtWidgets.QStackedWidget):

    def __init__(self, parent=None):
        QtWidgets.QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
        QtWidgets.QStackedWidget.setCurrentIndex(self, index)

    def setPage1(self):
        self.setCurrentIndex(0)

    def setPage2(self):
        self.setCurrentIndex(1)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = QtWidgets.QWidget()

    stack = StackedWidget()
    stack.addWidget(QtWidgets.QCalendarWidget())
    editor = QtWidgets.QTextEdit()
    editor.setPlainText("Hello world! " * 100)
    stack.addWidget(editor)

    page1Button = QtWidgets.QPushButton("Page 1")
    page2Button = QtWidgets.QPushButton("Page 2")
    page1Button.clicked.connect(stack.setPage1)
    page2Button.clicked.connect(stack.setPage2)

    layout = QtWidgets.QGridLayout(window)
    layout.addWidget(stack, 0, 0, 1, 2)
    layout.addWidget(page1Button, 1, 0)
    layout.addWidget(page2Button, 1, 1)

    window.show()

    sys.exit(app.exec_())