#!/usr/bin/env python
# coding: utf-8

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

def main():
    app = QApplication(sys.argv)

    #window = QWidget()
    #button = QPushButton('button', window) # ボタンを埋め込み
    #window.show()

    qbtn = QPushButton('Open')

    label = QLabel()
    label.setPixmap(QPixmap("/Users/royroy55/Desktop/a.png"))
    label.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
