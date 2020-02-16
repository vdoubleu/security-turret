import face_recognition
import cv2
import numpy as np
from pymongo import MongoClient
import json

face_locations = []
face_encodings = []
face_names = []
   

client = MongoClient("mongodb+srv://vdoubleu:passwordVW12345@makeuot-known-users-gnkvv.mongodb.net/test?retryWrites=true&w=majority")
db = client.makeuotDB
valid_users = db.validUsers

#patrick_image = face_recognition.load_image_file("patrick.jpg")
#patrick_face_encoding = face_recognition.face_encodings(patrick_image)[0]

#face_encodings = face_recognition.face_encodings(patrick_image)

#user_encoding = {"Patrick" : json.dumps(face_encodings[0].tolist())}

#willard_image = face_recognition.load_image_file("willard.jpg")
#willard_face_encoding = face_recognition.face_encodings(willard_image)[0]

#face_encodings = face_recognition.face_encodings(willard_image)

#user_encoding = {"Willard" : json.dumps(face_encodings[0].tolist())}

file_path = "patrick.jpg"
user_name = "Patrick"

user_image = face_recognition.load_image_file(file_path)
user_face_encoding = face_recognition.face_encodings(user_image)[0]

face_encodings = face_recognition.face_encodings(user_image)

user_encoding = {user_name : face_encodings[0].tolist()}

if  valid_users.find_one({"_id":"1"}) is not None:
    valid_users.update_one({"_id":"1"}, {"$push":{"users": user_encoding}})
else:
    valid_users.insert_one({"_id":"1", "users":[user_encoding]})

print(face_encodings)
