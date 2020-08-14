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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btnHoursGraph = QtWidgets.QPushButton(self.groupBox_2)
        self.btnHoursGraph.setObjectName("btnHoursGraph")
        self.verticalLayout_3.addWidget(self.btnHoursGraph)
        self.btnDayGraph = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDayGraph.setObjectName("btnDayGraph")
        self.verticalLayout_3.addWidget(self.btnDayGraph)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.btnSettings = QtWidgets.QPushButton(self.dockWidgetContents_2)
        self.btnSettings.setObjectName("btnSettings")
        self.verticalLayout_4.addWidget(self.btnSettings)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.groupBox = QtWidgets.QGroupBox(self.dockWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labInfo = QtWidgets.QLabel(self.groupBox)
        self.labInfo.setWordWrap(True)
        self.labInfo.setObjectName("labInfo")
        self.verticalLayout_2.addWidget(self.labInfo)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Monitor zanieczysczeń"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Wykresy"))
        self.btnHoursGraph.setText(_translate("MainWindow", "Wykresy godzinowy"))
        self.btnDayGraph.setText(_translate("MainWindow", "Wykres  dzienny"))
        self.btnSettings.setText(_translate("MainWindow", "Ustawienia"))
        self.groupBox.setTitle(_translate("MainWindow", "Informacje"))
        self.labInfo.setText(_translate("MainWindow", "Łączenie z czujnikiem"))

