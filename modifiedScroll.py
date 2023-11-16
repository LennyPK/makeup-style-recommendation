from PyQt5.QtWidgets import QScrollBar
from PyQt5 import QtCore

class MinimalScrollBar(QScrollBar):
    def __init__(self, orientation, *args, **kwargs):
        super(MinimalScrollBar, self).__init__(orientation, *args, **kwargs)
        if orientation == QtCore.Qt.Vertical:
            self.setStyleSheet("""
                QScrollBar:vertical {
                    border: none;
                    background: transparent;
                    width: 8px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:vertical {
                    background: #888888;
                    min-height: 20px;
                    border-radius: 4px;
                }
                QScrollBar::add-line:vertical {
                    height: 0px;
                    subcontrol-position: bottom;
                    subcontrol-origin: margin;
                }
                QScrollBar::sub-line:vertical {
                    height: 0px;
                    subcontrol-position: top;
                    subcontrol-origin: margin;
                }
                QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                    height: 0px;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
            """)
        elif orientation == QtCore.Qt.Horizontal:
            self.setStyleSheet("""
                QScrollBar:horizontal {
                    border: none;
                    background: transparent;
                    height: 8px;
                    margin: 0px 0px 0px 0px;
                }
                QScrollBar::handle:horizontal {
                    background: #888888;
                    min-width: 20px;
                    border-radius: 4px;
                }
                QScrollBar::add-line:horizontal {
                    width: 0px;
                    subcontrol-position: right;
                    subcontrol-origin: margin;
                }
                QScrollBar::sub-line:horizontal {
                    width: 0px;
                    subcontrol-position: left;
                    subcontrol-origin: margin;
                }
                QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
                    width: 0px;
                }
                QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                    background: none;
                }
            """)
