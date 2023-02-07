from PySide6.QtWidgets import QDialog
from ui.set_page_number import Ui_Dialog as set_page_number_dialog


class SetPageNumberDialog(QDialog, set_page_number_dialog):
    def __init__(self):
        super(SetPageNumberDialog, self).__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.page_number_check)

    def get_page_number(self):
        return [int(self.start_page.text()), int(self.end_page.text())]

    def page_number_check(self):
        if not self.start_page.text() or not self.end_page.text():
            self.reject()
        else:
            self.accept()
