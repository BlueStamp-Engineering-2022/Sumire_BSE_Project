# Juggling Detection on Raspberry Pi
The base of this program uses Raspberry Pi to detect various everyday objects using already trained library data. A further modification built off this base enabled the Raspberry Pi camera to just detect juggling balls. By additionally using R, the final project also allows one to get a visualization graph of their juggling.  

| **Engineer** | **School** | **Area of Interest** | **Grade** |
|:--:|:--:|:--:|:--:|
| Sumire T | Homestead High School | Electrical Engineering | Incoming Junior

![Headstone Image](https://lh3.googleusercontent.com/pw/AM-JKLWq4FktByuxDJZc-PB63b8deXDk4yMrnBBAkZ5cyne-A5fpeWznfmMlTt1Nqv6hbowsouhePyEZYcTsd6oMAzrx0oysfLtKP02Bd8vL35Wchb0kXAYSZv5jeTWPy7wvIZhkUs6gSQ0Y97imdH44cpeZ=w1356-h1354-no?authuser=0)

  
# Final Milestone
For my third milestone, I decided to modify my project so that the Raspberry Pi would only detect juggling. I first switched the Raspberry Pi to 64-bit, as the latest version of TensorFlow would not support the 32-bit version that I used for the regular object detection. After successfully switching to 64-bit Raspberry Pi, I restored the environment by enabling the camera and OpenCV once again. I also installed keras, a necessary package for the juggling code. I then compiled all of the source code into the Python IDE that was required for this modification. After successfully running the code, I made a cardboard stand for the camera and installed a radiator on the Raspberry Pi CPU to keep the cpu from overheating. Another change I made was to modify the project so that it utilizes R. I made this change so that every time the code is run, the data taken while running the code is displayed in a graph indicating the positions of the each of the juggling balls. 

[![Final Milestone](https://i3.ytimg.com/vi/qNx0R38yON4/maxresdefault.jpg)](https://youtu.be/qNx0R38yON4 "Final Milestone")

# Final Milestone Demo

[![Final Milestone Demo](http://i3.ytimg.com/vi/WOjv6PGqrOQ/hqdefault.jpg)](https://youtu.be/WOjv6PGqrOQ "Final Milestone Demo")

# Second Milestone
For my second milestone, I focused on finishing setting up the object detection. I first proceeded to download a zip file named "Object_Detection_Files.zip" and unzipped its contents into a directory. This zip file contained the necessary data to match each detected object using already trained library data. For the library, I used a coco.names file which has already been trained to identify various normal everyday objects and animals. After unzipping the library, I then compiled the source code onto the Python IDE. After compiling the source code, I also added an additional feature to the while loop to enable the user to exit the program by pressing the esc key. When finished with this adjustment, I ran the code, and it successfully detected various objects around my surroundings. 

[![Second Milestone](https://i3.ytimg.com/vi/L3Z3zM4a9gw/maxresdefault.jpg)](https://youtu.be/L3Z3zM4a9gw "Second Milestone")


# First Milestone
For my first milestone, I first setup the camera, or the hardware for this project. I connected the camera using the application libcamera-hello. I was able to check that the camera was working and was capturing photos using the Raspberry Pi by inputting this code onto the terminal. Next, I set up OpenCV, or the software for this project. I set up OpenCV, and the monitor displayed a still image saved as a jpg on the monitor, which showed that it was successfully running on python. However, although the camera and OpenCV worked individually, when combining the two elements together to complete the setup, they did not successfully capture an image. To solve this problem, I changed the configuration file of the Raspberry Pi by adding the functions, "startx=1" and "gpu_mem=128" and also removed the function "camera_auto_detect=1" by making it a comment. 

[![First Milestone](https://i3.ytimg.com/vi/GYPcAjikLI8/maxresdefault.jpg)](https://youtu.be/GYPcAjikLI8 "First Milestone")


# Starter Project
My project name is the Useless Machine, which is a device that turns itself off when switched on. When no movement or pressure is applied to the switch, the machine is in its "starting position". Inside this box, there is a snap switch on the bottom of the PCB which holds the arm in place, restricting its movement. However, when one flicks the switch to the right, the motor moves counterclockwise, causing the arm to also move counterclockwise, lifting the lid as it goes towards the switch. The motor moves counterclockwise because in the circuit, the positive area of the battery goes to the positive area of the motor, and the vice versa for the negative charges. However, soon, the contact from the arm to the switch pushes the switch to its "starting position", as the positive area of the battery goes to the negative area of the motor, and the negative area of the battery goes to the positive area of the motor. Since both the positive and negative areas of the battery each pair with its opposite charges, the motor turns clockwise. This can be seen as the arm also goes back under the surface of the box.

[![Starter Project](https://i3.ytimg.com/vi/4tdAprhGD8g/maxresdefault.jpg)](https://youtu.be/4tdAprhGD8g "Starter Project")
