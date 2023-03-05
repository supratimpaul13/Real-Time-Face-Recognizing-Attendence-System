import cv2
import face_recognition
import pickle
import os
import firebase_admin

from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


#  IMPORTING OUR FIREBASE DATABASE 
cred = credentials.Certificate("project/realtimefaceattendence-87692-firebase-adminsdk-rkz7t-4f8a26e0ff.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimefaceattendence-87692-default-rtdb.firebaseio.com/",
    'storageBucket': "realtimefaceattendence-87692.appspot.com"
})


#IMPORTING THE STUDENT IMAGES
folderPath = 'project/Images'
PathList = os.listdir(folderPath)

# print(PathList)
imgList = []
student_IDs = []

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # print(path)
    # print(os.path.splitext(path)[0])
    student_IDs.append(os.path.splitext(path)[0])

    # UPLOADING THE IMAGES IN OUR DATABASE
    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)

print(student_IDs)




# WE WILL LOOP THROURH EVERY IMAGE ANF ENCODE EACH IMAGE
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        # WE NEED THE IMAGES IN THE COLOR FORMAT (COLOR SPACE)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        # print(encode)
        encodeList.append(encode)

    return encodeList




print("Encoding started.....")
encodeList_Known = findEncodings(imgList)
encodeList_Known_with_IDs = [encodeList_Known, student_IDs]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeList_Known_with_IDs, file)
file.close()
print("File Saved")

