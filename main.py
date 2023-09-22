import sys
import cv2
import math
from ultralytics import YOLO
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from object_classes import classNames

class CameraFeedWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Camera Feed")
        self.setGeometry(100, 100, 640, 480)
        self.model = YOLO("yolo-Weights/yolov8n.pt")

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel(self.central_widget)
        self.layout.addWidget(self.label)

        self.camera = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_camera)
        self.timer.start(1000 // 30)  # Update every 30 milliseconds (30 FPS)

    def update_camera(self):
        ret, frame = self.camera.read()
        result = self.model(frame, stream=True)
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            q_image = QImage(frame.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            pixmap = QPixmap.fromImage(q_image)
            self.label.setPixmap(pixmap)
        
        # coordinates
        for r in result:
            boxes = r.boxes

            for box in boxes:
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                #cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                # confidence
                confidence = math.ceil((box.conf[0]*100))/100
                print("Confidence --->",confidence)

                # class name
                cls = int(box.cls[0])
                print("Class name -->", classNames[cls])

                # object details
                # org = [x1, y1]
                # font = cv2.FONT_HERSHEY_SIMPLEX
                # fontScale = 1
                # color = (255, 0, 0)
                # thickness = 2


    def closeEvent(self, event):
        self.camera.release()
        event.accept()

def main():
    app = QApplication(sys.argv)
    window = CameraFeedWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
