import numpy as np
import cv2
import time
from utils import handleTensorflowSession
from drawingutils import drawBallsAndHands
from keras.models import load_model
from gridmodel import GridModel
from frameratechecker import FramerateChecker

handleTensorflowSession(memoryLimit=0.2)

gridModel = GridModel("/home/stakeya/Desktop/BSE/Object_Juggling_Files/grid_models/grid_model_submovavg_64x64.h5")
patternModel = load_model("/home/stakeya/Desktop/BSE/Object_Juggling_Files/pattern_models/3b_pattern_model.h5")
cap = cv2.VideoCapture(0)
history = []
framerateChecker = FramerateChecker(expected_fps=30)
f = open('/tmp/data.csv', 'w')
f.write("x0,y0,x1,y1,x2,y2\n")
while(True):
    framerateChecker.check()
    ret, original_img = cap.read()
    if not ret:
        print ("Couldn't get frame from camera.")
        break
    else:
        height, width, channels = original_img.shape
        tocrop = int((width - height) / 2)
        original_img = original_img[:,tocrop:-tocrop]
        ballsAndHands = gridModel.predict(original_img.copy())
        coordinates = []
        coordinates.extend(ballsAndHands["rhand"])
        coordinates.extend(ballsAndHands["lhand"])
        coordinates.extend(ballsAndHands["balls"].flatten())
        history.append(coordinates)
        
        if len(history) > 30:
            del history[0]

        else:
            continue
        
        pattern = np.array(history)
        pattern[:,::2] = pattern[:,::2] - np.mean(pattern[:,::2])
        pattern[:,1::2] = pattern[:,1::2] - np.mean(pattern[:,1::2])
        pattern = pattern / pattern.std()
        pattern = np.expand_dims(pattern, axis=0)
        pattern_activations = patternModel.predict(pattern)[0]
        
        img = np.zeros((256,256,3), dtype=np.uint8)
            
        font = cv2.FONT_HERSHEY_PLAIN
        img = cv2.resize(original_img, (256,256), cv2.INTER_CUBIC)
        drawBallsAndHands(img, ballsAndHands)
        f.write('{},{},{},{},{},{}\n'.format(ballsAndHands["balls"][0, 0], ballsAndHands["balls"][0, 1],
                                             ballsAndHands["balls"][1, 0], ballsAndHands["balls"][1, 1],
                                             ballsAndHands["balls"][2, 0], ballsAndHands["balls"][2, 1]))
        img = cv2.resize(img, (768,768), cv2.INTER_CUBIC)

            
        cv2.imshow('Webcam', img)
        key = cv2.waitKey(1)
        
        if key == 27:
            break
f.close()        
cap.release()
cv2.destroyAllWindows()
             