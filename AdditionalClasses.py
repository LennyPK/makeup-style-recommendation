'''
Additional classes used in quizApp
'''

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtWidgets import QScrollBar, QGraphicsScene, QGraphicsPixmapItem, QGraphicsEllipseItem
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath, QImage, QColor

# Custom Minimal Scroll Bar for vertical and horizontal orientation
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

# Circle Crop Images which returns a QPixmap object
class CircularImageCutter:
    def __init__(self, image_path, diameter):
        self.image_path = image_path
        self.diameter = diameter

    def create_circular_pixmap(self):
        # Load the image
        original_pixmap = QPixmap(self.image_path)

        # Create a new QPixmap with an alpha channel
        circular_image = QPixmap(self.diameter, self.diameter)
        circular_image.fill(Qt.transparent)

        # Create a QPainter to paint on the new QPixmap
        painter = QPainter(circular_image)
        painter.setRenderHint(QPainter.Antialiasing)

        # Create a QPainterPath to define the clipping region as a circle
        clip_path = QPainterPath()
        clip_path.addEllipse(0, 0, self.diameter, self.diameter)

        # Set the clipping region to ensure the image is drawn only inside the circle
        painter.setClipPath(clip_path)

        # Scale and draw the original image onto the circular QPixmap
        painter.drawPixmap(0, 0, self.diameter, self.diameter, original_pixmap)

        # End painting
        painter.end()

        return circular_image