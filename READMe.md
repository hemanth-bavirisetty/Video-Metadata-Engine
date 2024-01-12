
##  Person Detection in Realtime and generating metadata  using YOLOv8 model.

### Requirements <br>
- ultralytics<br>
- cv2<br>
- cvzone<br>
- math<br>
- time<br>
- numpy<br>
- json<br>



### Description


The project contains an implementation of object detection using the YOLO (You Only Look Once) model. YOLO is a state-of-the-art real-time object detection system that uses a single convolutional neural network to simultaneously predict multiple objects in an image.

The project uses the YOLO model implemented in the ultralytics package.
This model takes a video file as input and performs person detection on each frame of the video. The detected objects are then labeled and displayed on the frame. The detected objects are also stored in a metadata file in JSON format.

The code uses a list called "people" to keep track of the people detected in the video. Each person is represented as a dictionary with information such as their name, age, gender, and the frames in which they were detected. If a person is detected multiple times in the video, their information is updated with the new frame information.

The code also uses the cvzone library to draw rectangles and text on the frame to highlight the detected objects and display their class and confidence score.

Overall, the code provides a simple and efficient way to perform object detection on video files and store metadata about the detected objects. It can be further extended and modified to include additional functionality such as face recognition, tracking, and more.<br>
Task Overview:

Given a large amount of raw HD video footage, generate useful and well-defined metadata for each video file, each distinct moment in each video file, and/or each frame in each video file.

### Project Structure

``videoinput.py`` is used to collect the video files . user can inpout the folder containing videos /directly the video file.<br>
``videotomp5.py`` has functions to convert the given any video format to ``.mp4`` file format.<br>
``engine.py`` calls the video input  and convert to mp4 meathods and then it imports the model and model detects the persons in the each frame of the video and adds the person to the a list named people before adding the person it checks for the presence of the person in people list if perosn not present in list it adds to list else it updates the person <br>
finally it generates the metadata.json file containing person with details of ``name, age, gender and the frame number`` of the person appeared.<br>


    
