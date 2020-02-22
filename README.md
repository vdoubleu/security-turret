# Security Turret

A prototype for a small home, industrial or military safety setup. Uses face recognition to determine the identity of anyone who enters a region. If the intruder does not leave, force will be applied. Created by Victor Wang, Patrick Wang, Willard Ma and Kevin Gu.

The pySerial library(python) was used to interface between python and the Arduino serial. The Servo library(Arduino) was used to communicate with the servo motors. All of this was done in real time.

All image processing was done using the [opencv library](https://opencv.org/) in conjunction with the [face_recognition](https://github.com/ageitgey/face_recognition) library. 

Face recognition is a multi-step process that involved the use of the HOG (Histogram of Oriented Gradients) algorithm to first detect faces by analysing gradient changes in an image and comparing these with existing examples. We can then calculate an "encoding" for a face by taking 128 predeterined measurements of a face according to a neural network. We can then take these measurements and compare them with the measurements of pre-existing individuals. If the measurements are similar enough, the program considors it a match and idtentifies the individual. If the measurements are not similar to an existing individuals measurements, the program considors that person as an intruder and labels them accordingly. 

# Adding Valid Users
The measurements of valid users is stored in a MongoDB database for quick and easy access. Additional users can easily be added to the system through the setup.py file. 

All you need to do is change the file path to an image of the user and then give that user a name. You will also need to modify the mongoDB client key so that it works with your own setup.

Once that is done, you can simply run the script to add the user to the database. 

# Detect and Identifying Users
Most of the processing is done within get\_frame\_info function in the detect.py file. It grabs the encodings of all the users from the database then utilises the face\_recognition library to perform the necessary calculations. Once the calculations have been completed and the measurements compared, the function returns the location of the user and their identity. 

# Turret Control
The mathematics required to control the turret based on the position of the individual is done within turr-cont.py file. This file also acts as the driving code behind the entire program. It calls upon all the other functions in the program and then sends results to arduino through the Pyserial library to control the motors and turret accordingly. This file also has a visual output so that a controller could watchover the system incase of any mishaps. Human-in-the-loop is the standard for current-day autonomous defense systems and so it would make sense for our system to work in a similar fashion. Graphical manipulation for information output and ease of use is all done through the dispBox.py file which is called within turr-cont.py.

[](turret.jpg)
Our final result


