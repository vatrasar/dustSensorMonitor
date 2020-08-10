# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/vatrasar/PycharmProjects/dustSensorMonitor/ui_templates/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(680, 578))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.graphView = QtWidgets.QLabel(self.centralwidget)
        self.graphView.setText("")
        self.graphView.setPixmap(QtGui.QPixmap("../result.svg"))
        self.graphView.setScaledContents(True)
        self.graphView.setObjectName("graphView")
        self.horizontalLayout.addWidget(self.graphView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.formLayout = QtWidgets.QFormLayout(self.dockWidgetContents_2)
        self.formLayout.setObjectName("formLayout")
        self.btnHoursGraph = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnHoursGraph.setObjectName("btnHoursGraph")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btnHoursGraph)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnHoursGraph.setText(_translate("MainWindow", "Wykresy godzinowy"))

