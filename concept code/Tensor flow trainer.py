from tensorflow.keras import datasets, layers, models
(training_images, training_labels), (testing_images, testing_labels) = datasets.cifar10.load_data()
training_images, testing_images = training_images /255, testing_images / 255

class_names = ['Plane', 'Car', 'Bird', 'Cat','Deer','Dog','Frog','Horse','Ship','Truck']

training_images = training_images[:20000]
training_labels = training_labels [:20000]
testing_images = testing_images[:4000]
testing_labels= testing_labels[:4000]

