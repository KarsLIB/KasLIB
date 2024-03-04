import cv2
import cvlib as cv
from time import sleep
from cvlib.object_detection import draw_bbox
print('hi katobj starting~')
sleep(1)
labels = []
class kaobjDetect():
    def object_detection():
        print('starting~')
        video = cv2.VideoCapture(0)
        while True:
            ret,frame = video.read()
            bbox, label, conf = cv.object_detection(frame)
            oimage = draw_bbox(frame, bbox, label, conf)
            cv2.imshow('katobjdetect', oimage)
            for item in  labels:
                if item in labels:
                    pass
                else:
                    labels.append(item)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            return labels