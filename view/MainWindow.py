from os import getlogin

from PySide6.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QShortcut, QKeySequence
from ui.ui_main import Ui_MainWindow
from view.PosDialog import PosDialog
from view.SetPageNumberDialog import SetPageNumberDialog


class MainWindow(QMainWindow, Ui_MainWindow):
    screen_position = []
    page_number = []
    save_dir = ''
    tesseract_dir = ''

    def __init__(self, *args, object=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.connect_event()
        self.connect_shortcut()

    def connect_event(self) -> None:
        self.set_position_btn.clicked.connect(self.set_pos)
        self.set_pages_btn.clicked.connect(self.set_page_number)
        self.set_save_dir_btn.clicked.connect(lambda: self.select_dir())
        self.execution_btn.clicked.connect(self.excute)
        self.set_tesseract_dir_btn.clicked.connect(lambda: self.select_dir("tesseract"))

    def connect_shortcut(self) -> None:
        QShortcut(QKeySequence('F1'), self.set_position_btn, self.set_pos)
        QShortcut(QKeySequence('F2'), self.set_pages_btn, self.set_page_number)
        QShortcut(QKeySequence('F3'), self.set_save_dir_btn, lambda: self.select_dir())
        QShortcut(QKeySequence('F4'), self.execution_btn, self.excute)
        QShortcut(QKeySequence(QKeySequence.StandardKey.Close), self, self.close)

    def set_pos(self):
        dialog = PosDialog()
        if not dialog.exec():
            self.write_status('캡쳐 좌표 설정 취소', -2)
            return

        self.screen_position = dialog.get_pos()

        if len(self.screen_position) == 4:
            self.write_status('캡쳐 좌표 설정 성공', -1)
        else:
            self.write_status('캡쳐 좌표 설정 실패', -2)
            self.screen_position.clear()

    def set_page_number(self):
        dialog = SetPageNumberDialog()

        if dialog.exec():
            self.page_number = dialog.get_page_number()

    def select_dir(self, select_type: str = ''):
        selected_dir = QFileDialog.getExistingDirectory(self, '저장 위치 설정', 'C:/Users/{}/Desktop'.format(getlogin()))

        if not selected_dir:
            return

        if "tesseract" == select_type:
            self.tesseract_dir = selected_dir
        else:
            self.save_dir = selected_dir

    def excute(self):
        print('excute CLick')

    def write_status(self, txt: str = '', types: int = -1):
        if not txt:
            return

        if types == -1:
            txt = f"[성공] {txt}"
        elif types == -2:
            txt = f"[실패] {txt}"

        status_text = self.status_text.toPlainText()
        self.status_text.setPlainText(f"{status_text}{txt}\n")
