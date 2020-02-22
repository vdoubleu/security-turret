import face_recognition
import cv2
import numpy as np
from pymongo import MongoClient
import json

def get_frame_info(frame):
    key = "mongodb+srv://<username>:<password>@makeuot-known-users-gnkvv.mongodb.net/test?retryWrites=true&w=majority" 
    client = MongoClient(key)
    db = client.makeuotDB
    valid_users = db.validUsers

    recieved_data = valid_users.find_one({"_id":"1"})

    val_users = recieved_data["users"]



    face_locations = []
    face_encodings = []
    face_names = []
    
    known_face_encodings = []
    known_face_names = []


    for x in range(len(val_users)):
        for name in val_users[x]:
            known_face_names.append(name)
            known_face_encodings.append(val_users[x][name])
        

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

   
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
   
    if len(face_locations) == 0:
        return 0, 0, 0, 0, "no_face"
    else:
        coor = face_locations[0]
        return coor[3], coor[0], coor[1], coor[2], face_names[0]

