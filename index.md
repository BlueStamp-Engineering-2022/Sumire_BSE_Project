# Object Detection with Machine Learning on Raspberry Pi
This will serve as a brief description of your project. Limit this to three sentences because it can become overly long at that point. This copy should draw the user in and make she/him want to read more.

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Sumire Takeya | Homestead High School | Electrical Engineering | Incoming Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLWq4FktByuxDJZc-PB63b8deXDk4yMrnBBAkZ5cyne-A5fpeWznfmMlTt1Nqv6hbowsouhePyEZYcTsd6oMAzrx0oysfLtKP02Bd8vL35Wchb0kXAYSZv5jeTWPy7wvIZhkUs6gSQ0Y97imdH44cpeZ=w1356-h1354-no?authuser=0)

  
# Final Milestone
(Edit sentences later) For my third milestone, I decided to modify my project so that the raspberry pi would only detect juggling. I decided to focus on juggling detection, as juggling is something that I enjoy and wanted to explore with machine learning. I first switched the raspberry pi to 64 bit, as the latest version of tensorflow would not support the 32 bit version that I used for the regular object detection. After successfully switching to 64 bit raspberry pi, I restored the environment by enabling the camera and OpenCV once again. I was also able to install keras, a necessary package for the juggling code. I then compiled all of the source code into the Python IDE that was required for this modification. After successfully running the code, I made a cardboard stand for the camera and installed a radiator on the Raspberry Pi CPU to keep the cpu from overheating. Another change I made was to modify the project so that it utilizes R, a software environment for statistical computing and graphics. I made this change so that every time the code is run, the data taken while running the code is displayed in a graph. For future modifications, I would like to find a way to run the algorithm faster, as it runs a bit slow, and also print a 3D camera stand for my camera. Lastly, after completing all the milestones for this project, I feel that I was successful in utilizing newly learned knowledge and ultimately integrating it with personal hobbies such as juggling.

[![Final Milestone](https://i3.ytimg.com/vi/qNx0R38yON4/maxresdefault.jpg)](https://youtu.be/qNx0R38yON4 "Final Milestone")

# Final Milestone Demo

[![Final Milestone Demo](http://i3.ytimg.com/vi/WOjv6PGqrOQ/hqdefault.jpg)](https://youtu.be/WOjv6PGqrOQ "Final Milestone Demo")

# Second Milestone
(Edit sentences later) For my second milestone, I proceeded to download a zip file named "Object_Detection_Files.zip" and unzipped its contents into a directory. The zip file contained the necessary data to match each detected object using already trained library data. For the library, I used A Coco names file which has already been trained to identify various normal everyday objects and animals. After unzipping the library containing data, I then compiled the source code that I found online onto the Python IDE. After compiling the code from the source code, I also added an additional feature to the while loop. I added a feature to enable the user to exit the program by pressing the esc key. When finished with this adjustment, I ran the code, and it successfully detected various objects around my surroundings. However, the screen just displayed a number, and it did not show the units. Since object detection is a tool to show how accurate the detected object is to the trained model from the library, I adjusted the code so that the percentage would display. After making this fix, the percentage successfully displayed, and the object detection ran smoothly as well. Furthermore, after successfully detecting numerous objects, I also then changed the code so that the camera only detects one object, which I set it to be scissors. After making this change and running the code, I was able to successfully detect scissors. For my next milestone, I would like to also detect another specific object, just like how I did with the scissors. 

[![Second Milestone](https://i3.ytimg.com/vi/L3Z3zM4a9gw/maxresdefault.jpg)](https://youtu.be/L3Z3zM4a9gw "Second Milestone")


# First Milestone
For my first milestone, I first setup the camera, or the hardware for this project. I connected the camera using the application libcamera-hello. When inputting this code onto the terminal, the camera opened on the monitor, indicating that the camera was working and was capturing photos using the Raspberry Pi. Next, I set up OpenCV, or the software of this project. I set up OpenCV, and it displayed a still image saved as a jpg on the monitor, which showed that it was successfully running on python. Although the camera and OpenCV worked individually, when combining them together to complete the setup, they did not successfully capture an image. To solve this problem, I changed the configuration file of the raspberry pi by adding the function, "startx=1" and "gpu_mem=128" and also removed the function "camera_auto_detect=1" by making it a comment. 

[![First Milestone](https://i3.ytimg.com/vi/GYPcAjikLI8/maxresdefault.jpg)](https://youtu.be/GYPcAjikLI8 "First Milestone")


# Starter Project
My project name is the Useless Machine, which is a device that turns itself off when switched on. When no movement or pressure is applied to the switch, the machine is in its "starting position". Inside this box, there is a snap switch on the bottom of the PCB which holds the arm in place, restricting its movement. However, when one flicks the switch to the right, the motor moves counterclockwise, causing the arm to also move counterclockwis, lifting the lid as it goes towards the switch. The motor moves counterclockwise because in the circuit, the positive area of the battery goes to the the positive areas of the motor, and the vice versa for the negative charges. However, soon, the contact from the arm to the switch pushes the switch to its "starting position". During that transition, the positive area of the battery goes to the negative area of the motor, and the negative area of the battery goes to the positive area of the motor. Since both the positive and negative area of the battery each paired with its opposite charges, the motor turns clockwise. This can be seen as the arm also goes back under the surface of the box.  

[![Starter Project](https://i3.ytimg.com/vi/4tdAprhGD8g/maxresdefault.jpg)](https://youtu.be/4tdAprhGD8g "Starter Project")
