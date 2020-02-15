import face_recognition
import cv2
import numpy as np

def get_frame_info(frame):
    face_locations = []
    face_encodings = []
    face_names = []
    
    patrick_image = face_recognition.load_image_file("patrick.jpg")
    patrick_face_encoding = face_recognition.face_encodings(patrick_image)[0]

    known_face_encodings = [
            patrick_face_encoding 
    ]

    known_face_names = [
            "Patrick"
    ]

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
    
    #print("names", face_names[0])
    #print("locations", face_locations[0])
    coor = face_locations[0]

    #print(coor[0], coor[1], coor[2], coor[3])
    print(coor[3], coor[0], coor[1], coor[2])

    return coor[3], coor[0], coor[1], coor[2]

    """
    cv2.rectangle(frame, (face_locations[0][3], face_locations[0][0]), (face_locations[0][1], face_locations[0][2]), (0, 0, 255), 2)

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Display the resulting image
    cv2.imshow('Video', small_frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    """
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        print(top, right, bottom, left)
        
        # Draw a box around the face
        #print(frame)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #cv2.rectangle(frame, (100, 100), (200, 200), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Display the resulting image
    cv2.imshow('Video', small_frame)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #return face_names, face_locations
    """

if __name__ == "__main__":
    print("test")
    test_im = cv2.imread("patrick.jpg")
    
    test_im = cv2.resize(test_im, (0, 0), fx=0.25, fy=0.25)

    get_frame_info(test_im)

