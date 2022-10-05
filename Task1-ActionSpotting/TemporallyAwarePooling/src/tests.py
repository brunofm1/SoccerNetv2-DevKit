import numpy as np
import matplotlib.pyplot as plt
import random


if __name__=="__main__":
    image_size = 64
    DATA_DIR = 'data/england_epl/2014-2015/2015-02-21 - 18-00 Chelsea 1 - 1 Burnley/2_ResNET_TF2.npy'
    X_train = np.load(DATA_DIR)
    # 45x60X2?
    print(45*60*2)
    print(f"Shape of training data: {X_train.shape}")
    print(f"Data type: {type(X_train)}")

    