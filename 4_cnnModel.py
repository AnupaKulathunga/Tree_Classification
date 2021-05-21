import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation, Flatten
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

pickle_in = open("X.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("Y.pickle","rb")
Y = pickle.load(pickle_in)
Y = np.array(Y)
X = X/255.0
x_test = X[130:]
x_train = X[:130]
y_test = Y[130:]
y_train = Y[:130]

model = tf.keras.models.Sequential()  
model.add(tf.keras.layers.Flatten())  
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))  
model.add(tf.keras.layers.Dense(38, activation=tf.nn.softmax))  

tensorboard = TensorBoard(log_dir=f"logs/Tree_Classification_{int(time.time())}")

model.compile(optimizer='adam',  
              loss='sparse_categorical_crossentropy',  
              metrics=['accuracy'])  # what to track

model.fit(x_train, y_train,
          batch_size=256,
          epochs=254,
          validation_split=0.1,
          callbacks=[tensorboard])

val_loss, val_acc = model.evaluate(x_test, y_test)  # evaluate the out of sample data with model
print(val_loss)  # model's loss (error)
print(val_acc)  # model's accuracy

model.save('Trees-CNN.model')