
# REAL TIME FACE RECOGNIZING ATTENDENCE SYSTEM

This is a small and interesting project on Real-Time Face Recognizing Attendence System using Python and Firebase.

The module basically detects the persons face and updates the on the database in realtime and moreover it does not mark the persons if is already marked for the current date.


There are 3 python files:

    1. main.py
    2. encode_generetor.py
    3. AddData_database.py

* [main.py](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/main.py) :- contains all the code for importing the files, opening the webcam recognising
* [encode_generetor.py](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/encode_generetor.py) :- contains the code for encoding the images and create data that will be imported by 'main.py' which will be used by face_reconizing module
* [AddData_database.py](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/AddData_database.py) :- contains the code to create the add data to our real time data base in Firebase

* [realtimefaceattendence-87692-firebase-adminsdk-rkz7t-4f8a26e0ff.json](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/realtimefaceattendence-87692-firebase-adminsdk-rkz7t-4f8a26e0ff.json) :- this is file created by the firebase database

# The project can be broken into 9 steps:

    1. Webcam
    2. Graphics
    3. Encode Generator
    4. Face Recognition
    5. Database setup
    6. Add data to database
    7. Add image to data base
    8. Real time data base update
    9. Limit the number of attendence per day
    


# PYTHON VERSION USED

This is the python version I am using.
The latest version python appears to show error with (face_recognition) pakage.

[python-3.8.10](https://www.python.org/ftp/python/3.8.10/python-3.8.10-amd64.exe)



# PYTHON PAKAGES USED

Following pakages are used in my python code

```bash
  import cv2
  import os
  import face_recognition
  import pickle
  import numpy as np
  import cvzone
  import firebase_admin
  from datetime import datetime
```
    
# SCREENSHOTS

* Active (This means it is ready to recognize the persion)

    ![Active](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/screenshot%201.jpg?raw=true)

* Face detected and updated the data base 

    ![Detected](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/screenshot%202.jpg?raw=true)

    ![Detected](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/screenshot%205.jpg?raw=true)

    ![Detected](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/screenshot%204.jpg?raw=true)

* Already Marked (This means the person is aleady marked for his/her attendence for the day)

    ![Marked](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/screenshot%203.jpg?raw=true)

* This is a snapshot of the firebase database

     ![Database](https://github.com/supratimpaul13/Real-Time-Face-Recognizing-Attendence-System/blob/main/screenshot%206.png?raw=true)
## Acknowledgements

 - [Murtaza Hassan](https://github.com/murtazahassan)


