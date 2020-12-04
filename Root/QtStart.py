# 모듈 임포트 sys, PyQt5의 QApplication과 QWidget 모듈, wxPython
import sys
import wx
from PyQt5.QtWidgets import QApplication, QWidget

# App 관련 Class 생성
class AppForm(QWidget):
    # 기본 스크린 사이즈
    sc_width = 1920
    sc_height = 1080

    # 클래스 중 가장 먼저 실행되는 함수
    def __init__(self):
        super().__init__()
        self.init_ui()

    # UI 초기화 함수 (기본 UI 설정)
    def init_ui(self):
        #set title
        self.setWindowTitle("Ai Application Demo with pyQt5")

        # set Defalut Screen Size
        #set Defalut Screen Size - 1. get Screen Size on each platform from wxPython
        wxApp = wx.App(False)
        sc_width, sc_height = wx.GetDisplaySize()

        # set Defalut Screen Size - 2. resize app screen size of your desktop screen size (About 1/4 size)
        self.resize(int(sc_width/2) ,int(sc_height/2))



# python main code(실제 실행되는 스크립트)
if __name__ == '__main__':
    # QApplication 함수 호출을 통해 app 생성 (모든 QT Application은 어플리케이션 객체를 생성해야한다. doc 참조.
    app = QApplication(sys.argv)
    # AppForm 인스턴스 생성 및 창 실행
    form = AppForm()
    form.show()

    # App 호출, pyqt4와의 호환성을 위해 sys.exit(app.exec_())로 쓰기도
    app.exec_()