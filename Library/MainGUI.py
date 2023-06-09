# Form implementation generated from reading ui file 'MainGUI.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalWidget = QtWidgets.QWidget(self.tab)
        self.horizontalWidget.setStyleSheet("QWidget {\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_bookid = QtWidgets.QLineEdit(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_bookid.setFont(font)
        self.lineEdit_bookid.setObjectName("lineEdit_bookid")
        self.horizontalLayout_4.addWidget(self.lineEdit_bookid)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_bookname = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_bookname.setFont(font)
        self.label_bookname.setObjectName("label_bookname")
        self.verticalLayout_2.addWidget(self.label_bookname)
        self.label_bookauthor = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_bookauthor.setFont(font)
        self.label_bookauthor.setObjectName("label_bookauthor")
        self.verticalLayout_2.addWidget(self.label_bookauthor)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_5.addWidget(self.horizontalWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.tab)
        self.horizontalWidget_2.setStyleSheet("QWidget {\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.lineEdit_memberid = QtWidgets.QLineEdit(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_memberid.setFont(font)
        self.lineEdit_memberid.setObjectName("lineEdit_memberid")
        self.horizontalLayout_5.addWidget(self.lineEdit_memberid)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_membername = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_membername.setFont(font)
        self.label_membername.setObjectName("label_membername")
        self.verticalLayout_4.addWidget(self.label_membername)
        self.label_contactinfo = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_contactinfo.setFont(font)
        self.label_contactinfo.setObjectName("label_contactinfo")
        self.verticalLayout_4.addWidget(self.label_contactinfo)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.toolButton_issue = QtWidgets.QToolButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_issue.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/issuebook.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_issue.setIcon(icon)
        self.toolButton_issue.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_issue.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_issue.setObjectName("toolButton_issue")
        self.horizontalLayout_6.addWidget(self.toolButton_issue)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_submission = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_submission.setFont(font)
        self.lineEdit_submission.setStyleSheet("QLineEdit {\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.lineEdit_submission.setObjectName("lineEdit_submission")
        self.verticalLayout_6.addWidget(self.lineEdit_submission)
        self.tableWidget_bookinfo = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget_bookinfo.setFont(font)
        self.tableWidget_bookinfo.setStyleSheet("QTableWidget {\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.tableWidget_bookinfo.setObjectName("tableWidget_bookinfo")
        self.tableWidget_bookinfo.setColumnCount(4)
        self.tableWidget_bookinfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_bookinfo.setHorizontalHeaderItem(3, item)
        self.tableWidget_bookinfo.horizontalHeader().setDefaultSectionSize(185)
        self.verticalLayout_6.addWidget(self.tableWidget_bookinfo)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.toolButton_renew = QtWidgets.QToolButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_renew.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/renew.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_renew.setIcon(icon1)
        self.toolButton_renew.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_renew.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_renew.setObjectName("toolButton_renew")
        self.horizontalLayout_7.addWidget(self.toolButton_renew)
        self.toolButton_submit = QtWidgets.QToolButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_submit.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/submission.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_submit.setIcon(icon2)
        self.toolButton_submit.setIconSize(QtCore.QSize(36, 36))
        self.toolButton_submit.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_submit.setObjectName("toolButton_submit")
        self.horizontalLayout_7.addWidget(self.toolButton_submit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton_addbook = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_addbook.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_addbook.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/addbook.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_addbook.setIcon(icon3)
        self.toolButton_addbook.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_addbook.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_addbook.setObjectName("toolButton_addbook")
        self.verticalLayout.addWidget(self.toolButton_addbook)
        self.toolButton_addmember = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_addmember.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_addmember.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/addmember.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_addmember.setIcon(icon4)
        self.toolButton_addmember.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_addmember.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_addmember.setObjectName("toolButton_addmember")
        self.verticalLayout.addWidget(self.toolButton_addmember)
        self.toolButton_viewbook = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_viewbook.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_viewbook.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/viewbook .png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_viewbook.setIcon(icon5)
        self.toolButton_viewbook.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_viewbook.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_viewbook.setObjectName("toolButton_viewbook")
        self.verticalLayout.addWidget(self.toolButton_viewbook)
        self.toolButton_viewmember = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_viewmember.setMaximumSize(QtCore.QSize(145, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_viewmember.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/viewmembers.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.toolButton_viewmember.setIcon(icon6)
        self.toolButton_viewmember.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_viewmember.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_viewmember.setObjectName("toolButton_viewmember")
        self.verticalLayout.addWidget(self.toolButton_viewmember)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Managment System"))
        self.lineEdit_bookid.setPlaceholderText(_translate("MainWindow", "Please Enter Book ID"))
        self.label_bookname.setText(_translate("MainWindow", "Book Name"))
        self.label_bookauthor.setText(_translate("MainWindow", "Book Author"))
        self.lineEdit_memberid.setPlaceholderText(_translate("MainWindow", "Please Enter Member ID"))
        self.label_membername.setText(_translate("MainWindow", "Member Name"))
        self.label_contactinfo.setText(_translate("MainWindow", "Contact Info"))
        self.toolButton_issue.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Search"))
        self.lineEdit_submission.setPlaceholderText(_translate("MainWindow", "Please Enter Book ID"))
        item = self.tableWidget_bookinfo.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "BookID"))
        item = self.tableWidget_bookinfo.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MemberID"))
        item = self.tableWidget_bookinfo.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "IssueTime"))
        item = self.tableWidget_bookinfo.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "RenewCount"))
        self.toolButton_renew.setText(_translate("MainWindow", "Renew Book"))
        self.toolButton_submit.setText(_translate("MainWindow", "Submit Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Renew/Submission Book"))
        self.toolButton_addbook.setText(_translate("MainWindow", "Add Book"))
        self.toolButton_addmember.setText(_translate("MainWindow", "Add Member"))
        self.toolButton_viewbook.setText(_translate("MainWindow", "View Books"))
        self.toolButton_viewmember.setText(_translate("MainWindow", "View Members"))

