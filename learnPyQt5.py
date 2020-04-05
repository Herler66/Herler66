#1
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
# import sys

# def main():
#     app = QApplication(sys.argv)
#     win = QMainWindow()
#     win.setGeometry(200,200,300,300) 
#     win.setWindowTitle("My first window!") 
    
#     label = QLabel(win)
#     label.setText("my first label")
#     label.move(50, 50)  

#     win.show()
#     sys.exit(app.exec_())

# main()  # make sure to call the functions
#2
# from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# import sys


# class MyWindow(QMainWindow):
#     def __init__(self):
#         super(MyWindow,self).__init__()
#         self.initUI()

#     def button_clicked(self):
#         self.label.setText("you pressed the button")
#         self.update()

#     def initUI(self):
#         self.setGeometry(200, 200, 300, 300)
#         self.setWindowTitle("Tech With Tim")

#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("my first label!")
#         self.label.move(50,50)

#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("click me!")
#         self.b1.clicked.connect(self.button_clicked)

#     def update(self):
#         self.label.adjustSize()


# def window():
#     app = QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())

# window()

#3
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(240, 50, 321, 121))
#         font = QtGui.QFont()
#         font.setPointSize(36)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
#         self.menubar.setObjectName("menubar")
#         self.menuFile = QtWidgets.QMenu(self.menubar)
#         self.menuFile.setObjectName("menuFile")
#         self.menuEdit = QtWidgets.QMenu(self.menubar)
#         self.menuEdit.setObjectName("menuEdit")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)
#         self.actionCopy = QtWidgets.QAction(MainWindow)
#         self.actionCopy.setObjectName("actionCopy")
#         self.actionPaste = QtWidgets.QAction(MainWindow)
#         self.actionPaste.setObjectName("actionPaste")
#         self.actionSave = QtWidgets.QAction(MainWindow)
#         self.actionSave.setObjectName("actionSave")
#         self.actionNew = QtWidgets.QAction(MainWindow)
#         self.actionNew.setObjectName("actionNew")
#         self.menuFile.addAction(self.actionNew)
#         self.menuFile.addAction(self.actionSave)
#         self.menuEdit.addAction(self.actionCopy)
#         self.menuEdit.addAction(self.actionPaste)
#         self.menubar.addAction(self.menuFile.menuAction())
#         self.menubar.addAction(self.menuEdit.menuAction())

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#         self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
#         self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
#         self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
#         self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))
        
#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.label.setText(_translate("MainWindow", "TextLabel"))
#         self.menuFile.setTitle(_translate("MainWindow", "File"))
#         self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
#         self.actionCopy.setText(_translate("MainWindow", "Copy"))
#         self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
#         self.actionPaste.setText(_translate("MainWindow", "Paste"))
#         self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
#         self.actionSave.setText(_translate("MainWindow", "Save"))
#         self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
#         self.actionNew.setText(_translate("MainWindow", "New"))
#         self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))

#     def clicked(self, text):
#         self.label.setText(text)
#         self.label.adjustSize()

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

#4
# from PyQt5 import QtCore, QtGui, QtWidgets

# class Ui_MainWindow(object):
#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(800, 600)
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setObjectName("centralwidget")
#         self.photo = QtWidgets.QLabel(self.centralwidget)
#         self.photo.setGeometry(QtCore.QRect(0, 0, 841, 511))
#         self.photo.setText("")
#         self.photo.setPixmap(QtGui.QPixmap("cat.jpg"))
#         self.photo.setScaledContents(True)
#         self.photo.setObjectName("photo")
#         self.cat = QtWidgets.QPushButton(self.centralwidget)
#         self.cat.setGeometry(QtCore.QRect(0, 510, 411, 41))
#         self.cat.setObjectName("cat")
#         self.dog = QtWidgets.QPushButton(self.centralwidget)
#         self.dog.setGeometry(QtCore.QRect(410, 510, 391, 41))
#         self.dog.setObjectName("dog")
#         MainWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QtWidgets.QMenuBar(MainWindow)
#         self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
#         self.menubar.setObjectName("menubar")
#         MainWindow.setMenuBar(self.menubar)
#         self.statusbar = QtWidgets.QStatusBar(MainWindow)
#         self.statusbar.setObjectName("statusbar")
#         MainWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(MainWindow)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#         self.dog.clicked.connect(self.show_dog)
#         self.cat.clicked.connect(self.show_cat)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
#         self.cat.setText(_translate("MainWindow", "CAT"))
#         self.dog.setText(_translate("MainWindow", "DOG"))

#     def show_dog(self):
#         self.photo.setPixmap(QtGui.QPixmap("imgs/dog.jpg"))

#     def show_cat(self):
#         self.photo.setPixmap(QtGui.QPixmap("imgs/cat.jpg"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())



#5
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QMessageBox

# class Ui_MainWindow(object):
# 	...
# 	def show_popup(self):
# 		msg = QMessageBox()
# 		msg.setWindowTitle("Tutorial on PyQt5")
# 		msg.setText("This is the main text!")
# 		msg.setIcon(QMessageBox.Question)
# 		msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Retry|QMessageBox.Ignore)
#         msg.setDefaultButton(QMessageBox.Retry)
#         msg.setInformativeText("informative text, ya!")

# 		msg.setDetailedText("details")

# 		msg.buttonClicked.connect(self.popup_button)

# 	def popup_button(self, i):
# 		print(i.text() )


#6
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboX = QtWidgets.QComboBox(self.centralwidget)
        self.comboX.setGeometry(QtCore.QRect(50, 120, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.comboX.setFont(font)
        self.comboX.setObjectName("comboX")
        self.comboX.addItem("")
        self.comboX.addItem("")
        self.comboY = QtWidgets.QComboBox(self.centralwidget)
        self.comboY.setGeometry(QtCore.QRect(470, 120, 231, 121))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.comboY.setFont(font)
        self.comboY.setObjectName("comboY")
        self.comboY.addItem("")
        self.comboY.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(290, 420, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 290, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboX.setItemText(0, _translate("MainWindow", "0"))
        self.comboX.setItemText(1, _translate("MainWindow", "1"))
        self.comboY.setItemText(0, _translate("MainWindow", "0"))
        self.comboY.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X XOR Y ="))

    def pressed(self):
        x = int(self.comboX.currentText())
        y = int(self.comboY.currentText())
        xor = (x and not y) or (not x and y)
        if xor == True:
            xor = 1
        else:
            xor = 0

        self.label.setText("X XOR Y =  " + str(xor))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())