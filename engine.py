#engine fiel contains the code for the object detection model

from ultralytics import YOLO
import cv2
import cvzone
import math,os
import time
import numpy as np
import json
from scripts import videoinput as vi
from scripts import videotomp4 as vtm




videofiles = vi.inputFiles()
print("done")

mp4videos = vtm.convertToMp4(videofiles)# [result_folder,[mp4videos,1,2,3]]
print("done")


 # For Video


model = YOLO("./model/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

prev_frame_time = 0
new_frame_time = 0
people=[]

 

for i in videofiles[1]:
  cap = cv2.VideoCapture(os.path.join(videofiles[0], i))
  while True:
      new_frame_time = time.time()
      success, img = cap.read()
      results = model(img, stream=True)
      detections = np.empty((0, 5))
      for r in results:
          boxes = r.boxes
          for box in boxes:
              # Bounding Box
              x1, y1, x2, y2 = box.xyxy[0]
              x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
              # cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
              w, h = x2 - x1, y2 - y1
              
              # Confidence
              conf = math.ceil((box.conf[0] * 100)) / 100
              # Class Name
              cls = int(box.cls[0])
              currentClass = classNames[cls]
              if currentClass == "person" and conf > 0.3:
                  cvzone.cornerRect(img, (x1, y1, w, h))
                  cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                                    scale=2, thickness=2, offset=6)
                  cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5)
                  currentArray = np.array([x1, y1, x2, y2, conf])
                  detections = np.vstack((detections, currentArray))
                  
                  x, y, w, h = box.xywh[0]

                  person = {
                      'name': 'Unknown',
                      'age': 0,
                      'gender': 'Unknown',
                      'video': 1,
                      'frames': [{'frame': cap.get(cv2.CAP_PROP_POS_FRAMES), 'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)}]
                  }


                  if person not in people:
                      people.append(person)
                  else:

                      index = people.index(person)
                      people[index]['frames'].append(
                          {'frame': cap.get(cv2.CAP_PROP_POS_FRAMES), 'x': int(x), 'y': int(y), 'w': int(w), 'h': int(h)})

              #cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)

      fps = 1 / (new_frame_time - prev_frame_time)
      prev_frame_time = new_frame_time
      print(fps)
      

      cv2.imshow("Image", img)
      cv2.waitKey(1)
      print(people)
      with open('out/metadata.json', 'w') as f:
        json.dump(people, f)
    
   
 

