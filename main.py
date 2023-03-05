import cv2
import os
import face_recognition
import pickle
import numpy as np
import cvzone
import firebase_admin
from datetime import datetime

from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


#  IMPORTING OUR FIREBASE DATABASE 
cred = credentials.Certificate("project/realtimefaceattendence-87692-firebase-adminsdk-rkz7t-4f8a26e0ff.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimefaceattendence-87692-default-rtdb.firebaseio.com/",
    'storageBucket': "realtimefaceattendence-87692.appspot.com"
})

bucket = storage.bucket()


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


# IMPORTIN THE MODE IMAGES INTO THE LIST
imgBackground = cv2.imread("project/Resources/background.png")

folderModePath = 'C:/series/Image Processing/project/Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# print(len(imgModeList))

# LOAD THE ENCODED FILE
print("Loading encode file....")
file = open('EncodeFile.p', 'rb')
encodeList_Known_with_IDs = pickle.load(file)
file.close()

# EXTRACTING FROM THE LOADED FILE
encodeList_Known, student_IDs = encodeList_Known_with_IDs
# print(student_IDs)
print("Encode file loaded")


modeType = 0
counter = 0
id = -1
imgStudent = []


while True:
    success, img = cap.read()

    imgsmall = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgsmall = cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)

    faceCur_frame = face_recognition.face_locations(imgsmall)
    encodeCur_frame = face_recognition.face_encodings(imgsmall, faceCur_frame)

    imgBackground[162:162 + 480, 55:55 + 640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    # MATCHING THE FACES

    if faceCur_frame:
        for encodeFace, faceloc in zip(encodeCur_frame, faceCur_frame):
            matches = face_recognition.compare_faces(encodeList_Known, encodeFace)
            face_distance = face_recognition.face_distance(encodeList_Known, encodeFace)
            # print("matches: ", matches)
            # print("face distace: ", face_distance)

            # THIS IS WILL THE VALUES OF MATCHES AND THE INDEX WITH LEAST VALUE IS OUR MATCH
            matcheIndex = np.argmin(face_distance)
            # print("Matched Index: ", matcheIndex)

            if matches[matcheIndex]:
                # print("Known face Detected")
                # print(student_IDs[matcheIndex])

                # CREATING A RECTANGLE THAT WILL SHOW IT IS RECOGNIZING THE FACE
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                bbox = 55+x1, 162+y1, x2-x1, y2-y1
                cvzone.cornerRect(imgBackground, bbox, rt=0)

                id = student_IDs[matcheIndex]
                print(id)

                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading...", (275, 400))
                    cv2.imshow("Face Attendence", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1


        if counter != 0:

            if counter == 1:
                # GET THE DATA
                students_info = db.reference(f'Students/{id}').get()
                print(students_info)

                # GET THE IMAGE FROM THE DATABASE
                blob = bucket.get_blob(f'project/Images/{id}.jpg')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)


                # UPDATE DATA OF ATTENDENCE
                datetimeObject = datetime.strptime(students_info['last_attendance_time'], "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (datetime.now() - datetimeObject).total_seconds()
                print(secondsElapsed)

                if secondsElapsed > 30:
                    ref = db.reference(f'Students/{id}')
                    students_info['total_attendence'] += 1
                    ref.child('total_attendence').set(students_info['total_attendence'])
                    ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                else:
                    modeType = 3
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

            if modeType != 3:
                
                if 10 < counter < 20:
                    modeType = 2
                    
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if counter <= 10:
                    cv2.putText(imgBackground, str(students_info['total_attendence']), (861, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(students_info['major']), (950, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(students_info['standing']), (910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(students_info['year']), (1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(students_info['starting_year']), (1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    (w, h),_ = cv2.getTextSize(students_info['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414 - w) // 2
                    cv2.putText(imgBackground, str(students_info['name']), (808 + offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (55, 55, 55), 1)
                    imgBackground[175:175+216,909:909+216] = imgStudent

            counter += 1

            if counter >= 20:
                counter = 0
                modeType = 0
                students_info = []
                imgStudent = []
                imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendence", imgBackground)
    cv2.waitKey(1)

