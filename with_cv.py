#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import random
#from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer)
#from PyQt5.QtGui import (QBrush, QColor, QPainter, QIntValidator, QPixmap, QTransform)
#from PyQt5.QtWidgets import (QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             #QGridLayout, QVBoxLayout, QHBoxLayout, QGraphicsPixmapItem,
                             #QLabel, QLineEdit, QPushButton, QFileDialog)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
import cv2
import subprocess
#from test import PIC


class graphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(graphicsScene, self).__init__(parent)

    def mousePressEvent(self, event):
        position = QPointF(event.scenePos())
        MainWindow.start_x = position.x()
        MainWindow.start_y = position.y()

    def mouseMoveEvent(self, event):
        position = QPointF(event.scenePos())

    def mouseReleaseEvent(self, event):
        position = QPointF(event.scenePos())
        MainWindow.end_x = position.x() - MainWindow.start_x
        MainWindow.end_y = position.y() - MainWindow.start_y

        self.addItem(QGraphicsRectItem(MainWindow.start_x, MainWindow.start_y, MainWindow.end_x, MainWindow.end_y))
        MainWindow.opentext()
        #self.update()


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.__imageItem = None
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.filename = ""

        self.graphicsView = QGraphicsView()
        self.scene = graphicsScene()
        self.scene.setSceneRect(0, 0, 500, 500)
        self.graphicsView.setScene(self.scene)

        self.fileButton = QPushButton("&Open")
        self.fileButton.clicked.connect(self.openfile)
        self.windowButton = QPushButton("&Next")
        self.windowButton.clicked.connect(self.openwindow)
        self.exportButton = QPushButton("&Export")
        self.exportButton.clicked.connect(self.exportfile)
        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.fileButton)
        buttonLayout.addWidget(self.windowButton)
        buttonLayout.addWidget(self.exportButton)

        propertyLayout = QVBoxLayout()
        propertyLayout.setAlignment(Qt.AlignTop)
        propertyLayout.addLayout(buttonLayout)

        self.mainLayout = QHBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignTop)
        self.mainLayout.addWidget(self.graphicsView)
        self.mainLayout.addLayout(propertyLayout)

        self.setLayout(self.mainLayout)
        self.setWindowTitle("Annotate Image")
        self.updating_rule = False
        self.timer = None

    def openfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            #self.celluarAutomaton.addpic(fname[0])
            self.filename = fname[0]
            pixmap = QPixmap(fname[0])

            # 既にシーンにPixmapアイテムがある場合は削除する。
            #if self.scene.__imageItem:
                #self.scene.removeItem(self.scene.__imageItem)

            # 与えられたイメージをPixmapアイテムとしてシーンに追加する。-----------
            item = QGraphicsPixmapItem(pixmap)
            # アイテムを移動可能アイテムとして設定。
            self.scene.addItem(item)
            self.scene.__imageItem = item
            self.scene.update()
            # ---------------------------------------------------------------------

            self.fitImage()
            #PIC.open_pic(fname[0])
            #cv2.setMouseCallback('image', PIC.draw_circle)

    def openwindow(self):
        cmd = '/Users/royroy55/Annotationtool/with_cv.py'
        returncode = subprocess.Popen(cmd)

    def exportfile(self):
        print "yeah!"

    def fitImage(self):
        # イメージをシーンのサイズに合わせてフィットするためのメソッド。
        # アスペクト比によって縦にフィットするか横にフィットするかを自動的に
        # 決定する。
        #if not self.scene.__imageItem():
            #return

        # イメージの元の大きさを持つRectオブジェクト。
        boundingRect = self.scene.__imageItem.boundingRect()
        # シーンの現在の大きさを持つRectオブジェクト。
        sceneRect = self.scene.sceneRect()

        itemAspectRatio = boundingRect.width() / boundingRect.height()
        sceneAspectRatio = sceneRect.width() / sceneRect.height()

        # 最終的にイメージのアイテムに適応するためのTransformオブジェクト。
        transform = QTransform()

        if itemAspectRatio >= sceneAspectRatio:
            # 横幅に合わせてフィット。
            scaleRatio = sceneRect.width() / boundingRect.width()
        else:
            # 縦の高さに合わせてフィット。.
            scaleRatio = sceneRect.height() / boundingRect.height()

        # アスペクト比からスケール比を割り出しTransformオブジェクトに適応。
        transform.scale(scaleRatio, scaleRatio)
        # 変換されたTransformオブジェクトをイメージアイテムに適応。
        self.scene.__imageItem.setTransform(transform)

    def opentext(self):
        subWindow = SubWindow(self)
        subWindow.show()

    def reservelabel(self):
        print "yeah!"

class SubWindow:
    def __init__(self, parent=None):
        self.w = QDialog(parent)
        self.parent = parent

        label = QLabel()
        label.setText('Sub Window')

        self.textbox = QLineEdit()
        self.reserveButton = QPushButton("&Reserve")
        self.reserveButton.clicked.connect(self.reservelabel)
        self.subLayout = QHBoxLayout()
        self.subLayout.addWidget(self.textbox)
        self.subLayout.addWidget(self.reserveButton)

        self.w.setLayout(subLayout)

    def reservelabel(self):
        print "yeah!"

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
