# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'find_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_find(object):
    def setupUi(self, find):
        if not find.objectName():
            find.setObjectName(u"find")
        find.setEnabled(True)
        find.resize(442, 200)
        find.setSizeGripEnabled(True)
        self.direction_groupBox = QGroupBox(find)
        self.direction_groupBox.setObjectName(u"direction_groupBox")
        self.direction_groupBox.setGeometry(QRect(160, 90, 171, 50))
        self.formLayout_2 = QFormLayout(self.direction_groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.radioButton_up = QRadioButton(self.direction_groupBox)
        self.radioButton_up.setObjectName(u"radioButton_up")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.radioButton_up)

        self.radioButton_down = QRadioButton(self.direction_groupBox)
        self.radioButton_down.setObjectName(u"radioButton_down")
        self.radioButton_down.setChecked(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.radioButton_down)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.formLayout)

        self.gridLayoutWidget = QWidget(find)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 10, 442, 68))
        self.gridlayout = QGridLayout(self.gridLayoutWidget)
        self.gridlayout.setObjectName(u"gridlayout")
        self.gridlayout.setContentsMargins(10, 0, 10, 0)
        self.next_button = QPushButton(self.gridLayoutWidget)
        self.next_button.setObjectName(u"next_button")
        self.next_button.setEnabled(False)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        self.next_button.setMinimumSize(QSize(80, 26))
        self.next_button.setMaximumSize(QSize(90, 16777215))

        self.gridlayout.addWidget(self.next_button, 0, 2, 1, 1)

        self.find_text = QLabel(self.gridLayoutWidget)
        self.find_text.setObjectName(u"find_text")
        self.find_text.setMinimumSize(QSize(80, 20))
        self.find_text.setMaximumSize(QSize(80, 20))
        self.find_text.setMargin(0)
        self.find_text.setIndent(-1)

        self.gridlayout.addWidget(self.find_text, 0, 0, 1, 1)

        self.line_edit = QLineEdit(self.gridLayoutWidget)
        self.line_edit.setObjectName(u"line_edit")
        self.line_edit.setMinimumSize(QSize(230, 0))
        self.line_edit.setMaximumSize(QSize(230, 16777215))
        self.line_edit.setCursorPosition(0)

        self.gridlayout.addWidget(self.line_edit, 0, 1, 1, 1, Qt.AlignLeft)

        self.cancel_button = QPushButton(self.gridLayoutWidget)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(90, 26))
        self.cancel_button.setMaximumSize(QSize(90, 16777215))

        self.gridlayout.addWidget(self.cancel_button, 1, 2, 1, 1, Qt.AlignTop)

        self.verticalLayoutWidget = QWidget(find)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 100, 126, 91))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_upnlow = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_upnlow.setObjectName(u"checkBox_upnlow")

        self.verticalLayout.addWidget(self.checkBox_upnlow)

        self.checkBox_replace = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_replace.setObjectName(u"checkBox_replace")

        self.verticalLayout.addWidget(self.checkBox_replace)


        self.retranslateUi(find)
        self.line_edit.textChanged.connect(self.next_button.show)

        QMetaObject.connectSlotsByName(find)
    # setupUi

    def retranslateUi(self, find):
        find.setWindowTitle(QCoreApplication.translate("find", u"\ucc3e\uae30", None))
        self.direction_groupBox.setTitle(QCoreApplication.translate("find", u"\ubc29\ud5a5", None))
        self.radioButton_up.setText(QCoreApplication.translate("find", u"\uc704\ub85c(&U)", None))
        self.radioButton_down.setText(QCoreApplication.translate("find", u"\uc544\ub798\ub85c(&D)", None))
        self.next_button.setText(QCoreApplication.translate("find", u"\ub2e4\uc74c \ucc3e\uae30(F)", None))
#if QT_CONFIG(shortcut)
        self.next_button.setShortcut(QCoreApplication.translate("find", u"F", None))
#endif // QT_CONFIG(shortcut)
        self.find_text.setText(QCoreApplication.translate("find", u"\ucc3e\uc744 \ub0b4\uc6a9(N):", None))
        self.cancel_button.setText(QCoreApplication.translate("find", u"\ucde8\uc18c", None))
        self.checkBox_upnlow.setText(QCoreApplication.translate("find", u"\ub300/\uc18c\ubb38\uc790 \uad6c\ubd84(&C)", None))
#if QT_CONFIG(shortcut)
        self.checkBox_upnlow.setShortcut(QCoreApplication.translate("find", u"C", None))
#endif // QT_CONFIG(shortcut)
        self.checkBox_replace.setText(QCoreApplication.translate("find", u"\uc8fc\uc704\uc5d0 \ubc30\uce58(&R)", None))
#if QT_CONFIG(shortcut)
        self.checkBox_replace.setShortcut(QCoreApplication.translate("find", u"R", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

