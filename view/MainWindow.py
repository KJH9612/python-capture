from PySide6.QtWidgets import QMainWindow, QMessageBox
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
        self.set_save_dir_btn.clicked.connect(self.set_save_dir)
        self.execution_btn.clicked.connect(self.excute)
        self.set_tesseract_dir_btn.clicked.connect(self.set_tesseract_dir)

    def connect_shortcut(self) -> None:
        QShortcut(QKeySequence('F1'), self.set_position_btn, self.set_pos)
        QShortcut(QKeySequence('F2'), self.set_pages_btn, self.set_page_number)
        QShortcut(QKeySequence('F3'), self.set_save_dir_btn, self.set_save_dir)
        QShortcut(QKeySequence('F4'), self.execution_btn, self.excute)
        QShortcut(QKeySequence(QKeySequence.StandardKey.Close), self, self.close)

    def set_pos(self):
        dialog = PosDialog()
        if dialog.exec():
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

    def set_save_dir(self):
        print('save_dir Click')

    def set_tesseract_dir(self):
        print("TESSERACT!")

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
