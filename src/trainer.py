import cv2
import numpy as np

from keras.layers import Convolution2D
from keras.layers import Cropping2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Lambda
from keras.layers import MaxPooling2D
from keras.models import Sequential


from data_loader import load_dataset, load_datasets
from parameters import Parameters

if __name__ == "__main__":
    parameters = Parameters()

    images, measurements = load_datasets(parameters)

    # duplicate the data
    # create balanced data set
    augmented_images, augmented_measurements = [], []
    for image, measurement in zip(images, measurements):
        augmented_images.append(image)
        augmented_measurements.append(measurement)

        augmented_images.append(cv2.flip(image, 1))
        augmented_measurements.append(measurement * -1.0)

    X_train = np.array(augmented_images)
    y_train = np.array(augmented_measurements)

    model = Sequential()
    model.add(Lambda(lambda x: (x / 255.0) - 0.5, input_shape=(160, 320, 3)))
    model.add(Cropping2D(cropping=((70, 25), (0, 0))))

    MODEL_TYPE = "nvidia"

    # LeNet
    if MODEL_TYPE == "lenet":
        model.add(Convolution2D(6, (5, 5), activation="relu"))
        model.add(MaxPooling2D())
        model.add(Convolution2D(6, (5, 5), activation="relu"))
        model.add(MaxPooling2D())
        model.add(Flatten())
        model.add(Dense(120))
        model.add(Dense(84))
        model.add(Dense(1))
    elif MODEL_TYPE == "nvidia":
        model.add(Convolution2D(24, (5, 5), strides=(2, 2), activation="relu"))
        model.add(Convolution2D(36, (5, 5), strides=(2, 2), activation="relu"))
        model.add(Convolution2D(48, (5, 5), strides=(2, 2), activation="relu"))
        model.add(Convolution2D(64, (3, 3), activation="relu"))
        model.add(Convolution2D(64, (3, 3), activation="relu"))
        model.add(Flatten())
        model.add(Dense(100))
        model.add(Dense(50))
        model.add(Dense(10))
        model.add(Dense(1))

    model.compile(loss="mse", optimizer="adam")
    model.fit(
        X_train, y_train, validation_split=0.2, shuffle=True, epochs=parameters.N_EPOCHS
    )
    model.save("model.h5")
