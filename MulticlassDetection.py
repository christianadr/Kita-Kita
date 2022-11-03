import torch
import cv2
import numpy as np

def prediction(model):

    vid = cv2.VideoCapture(0)

    while(True):
        _, frame = vid.read()
        
        # Make detections
        results = model(frame)
        
        cv2.imshow('Detection using YOLOv5', np.squeeze(results.render()))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s6')
    prediction(model)