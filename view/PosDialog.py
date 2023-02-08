from PySide6.QtCore import QRunnable, Signal, Slot, QObject
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QShortcut, QKeySequence

from ui.pos_dialog import Ui_Dialog as pos_dialog
from pynput.mouse import Listener

class PosSignal(QObject):
    setPosSignal = Signal(tuple, int)

class PosThread(QRunnable):
    SetPosSignal = PosSignal()
    counter = 0

    def click(self, x, y, btn, pressed):
        if pressed:
            self.SetPosSignal.setPosSignal.emit((x, y), self.counter)
            self.counter += 1

            if self.counter == 2:
                return False

    def listen_mouse_click(self):
        with Listener(on_click=self.click) as listener:
            listener.join()

    def run(self):
        self.listen_mouse_click()

class PosDialog(QDialog, pos_dialog):
    counter = 0
    line_edit_list = []

    def __init__(self):
        super(PosDialog, self).__init__()
        self.setupUi(self)
        self.connect_widget()
        self.connect_shortcut()

    def connect_widget(self):
        self.set_pos_btn.clicked.connect(self.in_pos)

    def connect_shortcut(self) -> None:
        QShortcut(QKeySequence('F1'), self.set_pos_btn, self.in_pos)
        QShortcut(QKeySequence(QKeySequence.StandardKey.Close), self, self.close)

    def in_pos(self):
        self.line_edit_list = [self.l_t_line_edit, self.r_b_line_edit]

        # initialize
        self.clear_pos()

        click_thread = PosThread()
        click_thread.SetPosSignal.setPosSignal.connect(self.set_pos)
        click_thread.run()

    def set_pos(self, pos:tuple, counter: int):
        self.line_edit_list[counter].setText(f"({pos[0]}, {pos[1]})")
        self.counter = counter

    def clear_pos(self):
        self.counter = 0
        self.l_t_line_edit.clear()
        self.r_b_line_edit.clear()

    def get_pos(self):
        l_t_pos = eval(self.l_t_line_edit.text())
        r_b_pos = eval(self.r_b_line_edit.text())
        print(list(l_t_pos + r_b_pos))
        return list(l_t_pos + r_b_pos)
