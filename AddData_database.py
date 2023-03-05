import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# IMPORTING OUR FIREBASE DATABASE 
cred = credentials.Certificate("project/realtimefaceattendence-87692-firebase-adminsdk-rkz7t-4f8a26e0ff.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://realtimefaceattendence-87692-default-rtdb.firebaseio.com/"
})

# THIS WILL CREATE A DIRECTORY FOR THE STUDENTS IN THE FIREBASE REALTIME DATABASE
ref = db.reference('Students')

# CREATING DATA
data = {

    "101":
        {
            # "KEY" : "VALUE"
            "name":"Supratim Paul",
            "major" : "Comitetive programmer",
            "starting_year" : 2020,
            "total_attendence": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time" : "2022-12-06 00:54:34"
        },

    "102":
        {
            # "KEY" : "VALUE"
            "name":"Elon Musk",
            "major" : "Physics",
            "starting_year" : 2020,
            "total_attendence": 0,
            "standing": "G",
            "year": 2,
            "last_attendance_time" : "2022-12-06 00:54:34"
        },

    "103":
        {
            # "KEY" : "VALUE"
            "name":"Ana De Armas",
            "major" : "Actor",
            "starting_year" : 2021,
            "total_attendence": 0,
            "standing": "G",
            "year": 1,
            "last_attendance_time" : "2022-12-06 00:54:34"
        },

    "104":
        {
            # "KEY" : "VALUE"
            "name":"Deep Senchowa",
            "major" : "Comitetive programmer",
            "starting_year" : 2020,
            "total_attendence": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time" : "2022-12-06 00:54:34"
        },

    "105":
        {
            # "KEY" : "VALUE"
            "name":"Sundar Pichai",
            "major" : "Google Ceo",
            "starting_year" : 2020,
            "total_attendence": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time" : "2022-12-06 00:54:34"
        },

    "106":
        {
            # "KEY" : "VALUE"
            "name":"Bidagddha Konwar",
            "major" : "Electronic Engineering",
            "starting_year" : 2020,
            "total_attendence": 0,
            "standing": "B",
            "year": 4,
            "last_attendance_time" : "2022-12-06 00:54:34"
        },


}

# SENDING THE DATA TO OUR REALTIME DATABASE
for key,value in data.items():
    ref.child(key).set(value)