import cv2
import pandas as pd
import numpy as np
import tensorflow as tf

treeNames =pd.read_csv("TreeNames.csv")
CATEGORIES =treeNames["Name"]


def prepare(filepath):
    IMG_SIZE = 20
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    return img_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("Trees-CNN.model")

prediction = model.predict([prepare('samples/Categories/13/13_tr38_35_b_1.tif')])
#print(prediction)  # will be a list in a list.
result = np.where(prediction == 1)
result[1][0]
print(CATEGORIES[result[1][0]])