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
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.l_header_widget = QWidget(self.centralwidget)
        self.l_header_widget.setObjectName(u"l_header_widget")
        self.horizontalLayout = QHBoxLayout(self.l_header_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.set_position = QPushButton(self.l_header_widget)
        self.set_position.setObjectName(u"set_position")

        self.horizontalLayout.addWidget(self.set_position)

        self.set_pages = QPushButton(self.l_header_widget)
        self.set_pages.setObjectName(u"set_pages")

        self.horizontalLayout.addWidget(self.set_pages)

        self.pushButton = QPushButton(self.l_header_widget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.execution = QPushButton(self.l_header_widget)
        self.execution.setObjectName(u"execution")

        self.horizontalLayout.addWidget(self.execution)


        self.verticalLayout_2.addWidget(self.l_header_widget, 0, Qt.AlignLeft)

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


        self.verticalLayout_2.addWidget(self.content_widget)

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


        self.verticalLayout_2.addWidget(self.footer_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.set_position.setText(QCoreApplication.translate("MainWindow", u"\uc88c\ud45c \uc124\uc815\ud558\uae30(F1)", None))
        self.set_pages.setText(QCoreApplication.translate("MainWindow", u"\ucabd\uc218 \uc124\uc815(F2)", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5 \uc704\uce58 \uc124\uc815(F3)", None))
        self.execution.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589(F4)", None))
    # retranslateUi

