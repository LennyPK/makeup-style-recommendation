from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap, QPainter, QImage, QBrush
from PyQt5.QtCore import Qt

class CircularImageWidget(QWidget):
    def __init__(self, image_path):
        super().__init__()

        self.image_path = image_path
        self.setMinimumSize(100, 100)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Load the image
        original_image = QPixmap(self.image_path).scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        scaled_image = original_image.scaledToHeight(100)
        image = QImage(scaled_image)

        # Create a mask and set it as the painter's clip region
        mask = QImage(self.size(), QImage.Format_ARGB32)
        mask.fill(Qt.transparent)
        painter.setClipRegion(QRegion(mask))

        # Draw the image with a circular clip
        painter.setBrush(QBrush(image))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(self.rect())