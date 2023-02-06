# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.l_header_widget = QWidget(self.centralwidget)
        self.l_header_widget.setObjectName(u"l_header_widget")
        self.horizontalLayout = QHBoxLayout(self.l_header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.set_position_btn = QPushButton(self.l_header_widget)
        self.set_position_btn.setObjectName(u"set_position_btn")

        self.horizontalLayout.addWidget(self.set_position_btn)

        self.set_pages_btn = QPushButton(self.l_header_widget)
        self.set_pages_btn.setObjectName(u"set_pages_btn")

        self.horizontalLayout.addWidget(self.set_pages_btn)

        self.set_save_dir_btn = QPushButton(self.l_header_widget)
        self.set_save_dir_btn.setObjectName(u"set_save_dir_btn")

        self.horizontalLayout.addWidget(self.set_save_dir_btn)

        self.execution_btn = QPushButton(self.l_header_widget)
        self.execution_btn.setObjectName(u"execution_btn")

        self.horizontalLayout.addWidget(self.execution_btn)


        self.horizontalLayout_3.addWidget(self.l_header_widget, 0, Qt.AlignLeft)

        self.r_header_widget = QWidget(self.centralwidget)
        self.r_header_widget.setObjectName(u"r_header_widget")
        self.verticalLayout_2 = QVBoxLayout(self.r_header_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.set_tesseract_dir_btn = QPushButton(self.r_header_widget)
        self.set_tesseract_dir_btn.setObjectName(u"set_tesseract_dir_btn")

        self.verticalLayout_2.addWidget(self.set_tesseract_dir_btn)


        self.horizontalLayout_3.addWidget(self.r_header_widget, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.content_widget = QWidget(self.centralwidget)
        self.content_widget.setObjectName(u"content_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.content_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.status_text = QPlainTextEdit(self.content_widget)
        self.status_text.setObjectName(u"status_text")
        self.status_text.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.status_text)


        self.verticalLayout_3.addWidget(self.content_widget)

        self.footer_widget = QWidget(self.centralwidget)
        self.footer_widget.setObjectName(u"footer_widget")
        self.verticalLayout = QVBoxLayout(self.footer_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.footer_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setTextVisible(True)

        self.verticalLayout.addWidget(self.progressBar)


        self.verticalLayout_3.addWidget(self.footer_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.set_position_btn.setText(QCoreApplication.translate("MainWindow", u"\uc88c\ud45c \uc124\uc815\ud558\uae30(F1)", None))
        self.set_pages_btn.setText(QCoreApplication.translate("MainWindow", u"\ucabd\uc218 \uc124\uc815(F2)", None))
        self.set_save_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \uc704\uce58 \uc124\uc815(F3)", None))
        self.execution_btn.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589(F4)", None))
        self.set_tesseract_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\ud14c\uc11c\ub799\ud2b8 \uacbd\ub85c \ucd94\uac00", None))
    # retranslateUi

