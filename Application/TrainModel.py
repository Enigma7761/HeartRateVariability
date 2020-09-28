from Model import *
import os

model_file = 'Model1.h5'
if os.path.isfile(model_file):
    print("loaded")
    load_model(model_file)

train_model(400, model_file, samples=200000, batch_size=64, learning_rate=0.00004)
