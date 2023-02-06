from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtGui import QShortcut, QKeySequence
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    screen_position = []

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
        from pynput.mouse import Button, Controller
               
        mouse = Controller()
        
        start = mouse.press(Button.left)
        end = mouse.release(Button.left)
        print(start, end)

    def set_page_number(self):
        print('page Click')

    def set_save_dir(self):
        print('save_dir Click')

    def set_tesseract_dir(self):
        print("TESSERACT!")

    def excute(self):
        print('excute CLick')
