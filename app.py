from flask import Flask
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import json

app = Flask(__name__)

@app.route('/')
def main():
    # model = load_model('food101_classifier.h5')
    # with open('monch-backend/food_nums.json', 'r') as f:
    #     food_nums = json.load(f)

    # img_path = '../imgs/hotdog.jpg' # replace with database query or something
    # img = image.load_img(img_path, target_size=(128, 128))
    # img_array = image.img_to_array(img) 
    # img_array = np.expand_dims(img_array, axis=0) 
    # img_array = img_array * (1 / 255.0) 

    # prediction = model.predict(img_array)
    # predicted_class = np.argmax(prediction)
    # print(food_nums[str(predicted_class)])
    return 'Hello, World!'
