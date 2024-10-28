import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from tensorflow.keras import datasets, layers, models

#this image classifier program uses tensorflows already existing dataset
(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
training_images, testing_images = training_images /255, testing_images / 255

class_names = ['Plane', 'Car', 'Bird', 'Cat','Deer','Dog','Frog','Horse','Ship','Truck']

training_images = training_images[:20000]
training_labels = training_labels [:20000]
testing_images = testing_images[:4000]
testing_labels= testing_labels[:4000]

model = models.load_model('image_classifier.keras')
root = tk.Tk()
root.geometry("200x100")
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())
label = tk.Label(root, text="enter image address")
label.pack()
entry = tk.Entry(root)
entry.pack()
def get_input():
    user_input = entry.get()
    print("User input:", user_input)
    img= cv.imread(f'{user_input}')
    img = cv.resize(img, (32, 32))
    img= cv.cvtColor(img,cv.COLOR_BGR2RGB)
    plt.imshow(img, cmap=plt.cm.binary)
    prediction = model.predict(np.array([img]) / 255)
    index = np.argmax(prediction)
    window = tk.Tk()
    window.eval('tk::PlaceWindow %s center' % window.winfo_toplevel())
    window.withdraw()
    messagebox.showinfo('question',f'the subject of the image is {class_names[index]}')
    window.deiconify()
    window.destroy()
    window.quit()
    print(f'prediction is {class_names[index]}')

button = tk.Button(root, text="get input", command=get_input)
button.pack()
root.mainloop()
plt.show()
