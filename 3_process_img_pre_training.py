import numpy as np
import matplotlib.pyplot as plt
import os 
import cv2
from tqdm import tqdm
import pickle

DATADIR ="samples\Categories"
numlist=list(range(1,39))
CATEGORIES = list(map(str,numlist))

training_data = []

def create_training_data():
    for category in CATEGORIES:

        path = os.path.join(DATADIR,category)  # create path to images
        class_num = CATEGORIES.index(category)  # get the classification  (1 to 38)

        for img in tqdm(os.listdir(path)):  # iterate over each image
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                training_data.append([img_array, class_num])  # add this to our training_data
            except Exception as e:
                pass

create_training_data()

import random

random.shuffle(training_data)
print("Check whether well suffled")
for sample in training_data[:10]:
    print(sample[1])
print("Boom...!")

X = []
Y = []
IMG_SIZE = 20
for features,label in training_data:
    X.append(features)
    Y.append(label)

#print(X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

pickle_out = open("X.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("Y.pickle","wb")
pickle.dump(Y, pickle_out)
pickle_out.close()