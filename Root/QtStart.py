import sys, os
import wx
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt,QEvent

from PyQt5.QtMultimedia import QSound
from playsound import playsound
import multiprocessing


# App 관련 Class 생성
class AppForm(QtWidgets.QWidget):
    # 기본 스크린 사이즈
    sc_width = 1920
    sc_height = 1080
    m_process = multiprocessing.Process(target=playsound, args=['musics/space.mp3'])

    def playBackgroundSound(self):
        AppForm.m_process.start()

    def stopBackgroundSound(self):
        AppForm.m_process.terminate()

    # 클래스 중 가장 먼저 실행되는 함수
    def __init__(self):
        super().__init__()
        self.init_ui()

    # UI 초기화 함수 (기본 UI 설정)

    def init_ui(self):
        #set title

        self.setWindowTitle("Ai Application Demo with pyQt5")

        if os.name == 'nt':
            self.setWindowIcon(QIcon('app_icon.png'))

        # set Defalut Screen Size
        #set Defalut Screen Size - 1. get Screen Size on each platform from wxPython
        wxApp = wx.App(False)
        sc_width, sc_height = wx.GetDisplaySize()
        # set Defalut Screen Size - 2. resize app screen size of your desktop screen size (About 1/4 size)
        self.resize(int(sc_width/2) ,int(sc_height/2))

        # Quit action

        quit = QtWidgets.QAction("Quit", self)

        quit.triggered.connect(self.close)

        # set main btn
        self.vision_btn = QtWidgets.QPushButton('비전', self)
        self.qt_practice_btn = QtWidgets.QPushButton('QT 예제', self)

        # set btn font
        self.vision_btn.setFont(QFont('Arial',20))
        self.qt_practice_btn.setFont(QFont('Arial',20))

        self.vision_btn.setMaximumHeight(80)
        self.qt_practice_btn.setMaximumHeight(80)

        # set widget connect with signal
        self.vision_btn.clicked.connect(self.vision_btn_function)
        self.qt_practice_btn.clicked.connect(self.qt_practice_btn_function)

        self.vision_btn.installEventFilter(self)
        self.qt_practice_btn.installEventFilter(self)

        self.vision_btn.setStyleSheet('QPushButton::hover'
                                      '{'
                                      'background-color : #64b5f6'
                                      '}'
                                      )

        self.qt_practice_btn.setStyleSheet('QPushButton::hover'
                                      '{'
                                      'background-color : #64b5f6'
                                      '}'
                                      )

        #set text


        title_text = QtWidgets.QLabel('Vision Project with PyQt5')
        title_text.setStyleSheet('color : white')
        title_text.setFont(QFont('Arial',35))
        title_text.setAlignment(Qt.AlignCenter)

        copyright_text = QtWidgets.QLabel('Copylight : easyJin')
        copyright_text.setStyleSheet('color : white')
        copyright_text.setAlignment(Qt.AlignCenter)

        # set grid layout
        grid = QtWidgets.QGridLayout()


        self.setLayout(grid)
        grid.cellRect(5,5)
        grid.setColumnStretch(0,1)
        grid.setColumnStretch(1,1)
        grid.setColumnStretch(2,1)

        grid.setRowStretch(0,1)
        grid.setRowStretch(1,1)
        grid.setRowStretch(2,1)
        grid.setRowStretch(3,1)

        grid.addWidget(title_text,0,1)
        grid.addWidget(copyright_text,5,1)

        grid.addWidget(self.vision_btn,1,1)
        grid.addWidget(self.qt_practice_btn,2,1)

    def vision_btn_function(self):
        print('qt_practice_btn_function page')
        reply = QtWidgets.QMessageBox.question(self, 'Message', '준비중입니다 : (',
                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)


    def qt_practice_btn_function(self):
        print('qt_practice_btn_function page')
        reply = QtWidgets.QMessageBox.question(self, 'Message', '준비중입니다 : (',
                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

    # set background img

    def paintEvent(self, a0: QPaintEvent):
        painter = QPainter(self)
        painter.setOpacity(0.7)
        painter.drawRect(self.rect())
        pix = QPixmap("./imgs/ui/background-img.png")  # Change to the relative path of your own image
        painter.drawPixmap(self.rect(), pix)


    # app close event
    def closeEvent(self, a0: QCloseEvent):
        self.stopBackgroundSound()

    def eventFilter(self, obj, event):

        if obj == self.qt_practice_btn and event.type() == QEvent.HoverEnter:
            self.onHovered()
        elif obj == self.vision_btn and event.type() == QEvent.HoverEnter:
            self.onHovered()

        return super(AppForm, self).eventFilter(obj, event)

    def onHovered(self):
        QSound.play('musics/button_hover.wav')
#        playsound('musics/button_hover.wav')

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


# python main code(실행 메인 스크립트)
if __name__ == '__main__':

    # QApplication 함수 호출을 통해 app 생성 (모든 QT Application은 어플리케이션 객체를 생성해야한다. doc 참조.
    app = QtWidgets.QApplication(sys.argv)

    # AppForm 인스턴스 생성 및 창 실행

    form = AppForm()
    form.paintEngine()
    form.show()

    stack = StackedWidget()
    stack.addWidget(form)


    form.playBackgroundSound()
    # App 호출, pyqt4와의 호환성을 위해 sys.exit(app.exec_())로 쓰기도

    sys.exit(app.exec_())
