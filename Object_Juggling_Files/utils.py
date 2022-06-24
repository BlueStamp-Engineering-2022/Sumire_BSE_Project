import numpy as np
#from keras.backend.tensorflow_backend import set_session (original)
from keras.backend import set_session
import tensorflow as tf

def getDistance(x1,y1,x2,y2):
    return np.sqrt((x1-x2)**2 + (y1-y2)**2)


def handleTensorflowSession(memoryLimit):
    config = tf.compat.v1.ConfigProto()
    config.gpu_options.per_process_gpu_memory_fraction = memoryLimit
    config.gpu_options.visible_device_list = "0"
    config.intra_op_parallelism_threads = 1
    config.inter_op_parallelism_threads = 1
    tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))