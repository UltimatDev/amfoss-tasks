import sys
from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QApplication, QWidget, QLabel,QLineEdit,QPushButton


class disp(QWidget):
    def __init__(self, parent: QWidget | None = ..., f: WindowType = ...) -> None:
        super().__init__()

        self.w=None
        