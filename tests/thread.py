from PySide6.QtWidgets import QApplication, QPushButton, QHBoxLayout, QWidget
from PySide6.QtCore import QThread, QThreadPool, QRunnable

import sys
import time

class HelloWorldTask(QRunnable):
    def run(self):
        print("Hello world from thread", QThread.currentThread())
        time.sleep(5)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        QThreadPool.globalInstance().setMaxThreadCount(100)

        self.btn1 = QPushButton("btn1")
        self.btn1.clicked.connect(self.btn1_clicked)
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.btn1)

        self.setLayout(self.layout)
        self.show()
    
    def btn1_clicked(self):
        hello = HelloWorldTask()
        # QThreadPool takes ownership and deletes 'hello' automatically
        QThreadPool.globalInstance().start(hello)

        print("활성 쓰레드 개수:", QThreadPool.globalInstance().activeThreadCount())

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()