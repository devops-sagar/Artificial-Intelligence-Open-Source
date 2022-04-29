import socket
import sys
import tensorflow as tf
from keras.preprocessing import image
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

d = socket.socket()
print("Socket successfully created")

port = 6500

d.bind(('localhost', port))

d.listen()

a, addr = d.accept()
file = open("server_images.jpg", "wb")
image_chunk = a.recv(2048)
while image_chunk:

    file.write(image_chunk)
    image_chunk = a.recv(2048)

model = tf.keras.models.load_model("rps.h5")
print("sdjflsfk")
i = image.load_img("server_images.jpg", target_size=(150, 150))
x = image.img_to_array(i)
x = np.expand_dims(x, axis=0)
images = np.vstack([x])
classes = model.predict(images, batch_size=10)
print(classes)
ans = "Image cant be classified"
print("hiiiiiii")
if str(classes) == '[[1. 0. 0.]]':
    ans = "\n The image you've submitted is classified as a: paper"

elif str(classes) == '[[0. 1. 0.]]':
    ans = "\n The image you've submitted is classified as a: rock"

else:
    ans = "\n The image you've submitted is classified as a: scissors"

print(ans)

file.close()
print(" Shutting down server.")
d.close()
