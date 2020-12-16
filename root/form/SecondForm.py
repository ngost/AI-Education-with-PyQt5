# -*- coding: utf-8 -*-

# form implementation generated from reading ui file '/Users/ijin-yeong/Desktop/project_list_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import wx
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys, os

import root.form.MovieReviewSentiment as movieSenti

from pathlib import Path

class Second_Form(QtWidgets.QWidget):

    sc_width = 1920
    sc_height = 1080
    root_path = Path(os.path.abspath('')).parent

    app_font = QFont('Arial',24)
    stack = None

    def __init__(self):
        super().__init__()
        self.setupUi()
        # stack = St.StackedWidget()


    def init_StackWidget(self, para):
        self.stack = para

    def paintEvent(self, a0: QPaintEvent):
        painter = QtGui.QPainter(self)
        painter.setOpacity(0.5)
        painter.drawRect(self.rect())


        pix = QtGui.QPixmap()  # Change to the relative path of your own image
        img_path = str(Second_Form.root_path) + '/imgs/ui/background-img.png'
        pix.load(img_path)

        painter.drawPixmap(self.rect(), pix)


    def setupUi(self):

        self.setWindowTitle('Project List')
        self.resize(800,600)

        self.title_label = QtWidgets.QLabel()
        self.title_label.setText('Project List')
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setFont(Second_Form.app_font)
        self.title_label.setStyleSheet('color : black')

        self.back_btn = QtWidgets.QPushButton()
        self.back_btn.setText('Back to Home')
        self.back_btn.setMaximumHeight(50)
        self.back_btn.clicked.connect(self.back_btn_function)

        self.movie_classify_btn = QtWidgets.QPushButton()
        self.movie_classify_btn.setText('Movie Review Classify')
        self.movie_classify_btn.setMaximumHeight(30)

        self.movie_classify_btn.clicked.connect(self.movie_review_ssentiment_btn)

        self.grid_layout = QtWidgets.QGridLayout()
        #그리드 레이아웃 크기 지정
        # self.grid_layout.cellRect(5,3)
        # 그리드 레이아웃 각 행열의 사이즈 계수 1로 고정 ,, 0이 아니라 1부터 시작 주의
        self.grid_layout.setColumnStretch(0,1)
        self.grid_layout.setColumnStretch(1,1)
        self.grid_layout.setColumnStretch(2,1)

        self.grid_layout.setRowStretch(0,1)
        self.grid_layout.setRowStretch(1,1)
        self.grid_layout.setRowStretch(2,1)
        self.grid_layout.setRowStretch(3,1)
        self.grid_layout.setRowStretch(4,1)


        self.setLayout(self.grid_layout)

        #3,4 파라미터는 행은 1개먹고, 열은 2개먹고
        self.grid_layout.addWidget(self.title_label,0,0,1,3)
        self.grid_layout.addWidget(self.movie_classify_btn,2,1,1,1)
        self.grid_layout.addWidget(self.back_btn,4,1,1,1)




    #
    def back_btn_function(self):
        self.stack.setCurrentIndex(self.stack.currentIndex()-1)

    def dialog_iam_ready(self):
        reply = QtWidgets.QMessageBox.question(self, 'Message', '준비중입니다 : (',
                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

    def movie_review_ssentiment_btn(self):
        review_form = movieSenti.MovieReviewForm()
        review_form.init_StackWidget(self.stack)
        self.stack.addWidget(review_form)
        self.stack.setCurrentIndex(self.stack.currentIndex()+1)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    form = Second_Form()
    form.paintEngine()

    form.show()

    sys.exit(app.exec_())