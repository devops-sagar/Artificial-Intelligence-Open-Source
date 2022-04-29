import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/name", methods=["POST"])
def setName():
    if request.method == 'POST':
        posted_data = request.get_json()
        data = posted_data['data']
        var = str(data)
        print(var)
        model = load_model('model.h5', compile=True)
        p1 = var
        img1 = image.load_img(p1, target_size=(150, 150))
        x = image.img_to_array(img1)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        classes = model.predict(images, batch_size=10)
        classes = str(classes)
        if classes == '[[0. 1. 0.]]':
            classes = 'Rock'
        elif classes == '[[1. 0. 0.]]':
            classes = 'paper'
        elif classes == '[[0. 0. 1.]]':
            classes = 'scissors'
        else:
            classes = 'Wrong image uploaded!!!'

        print(classes)
        return jsonify(str(classes))


#  main thread of execution to start the server
if __name__ == '__main__':
    app.run(debug=True)
