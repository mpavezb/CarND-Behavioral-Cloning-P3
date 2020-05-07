from keras.models import Sequential
from keras.layers import Flatten, Dense
import numpy as np

from data_loader import load_dataset, load_datasets
from parameters import Parameters


if __name__ == "__main__":
    parameters = Parameters()

    images, measurements = load_datasets(parameters, limit=500, debug=False)

    X_train = np.array(images)
    y_train = np.array(measurements)

    model = Sequential()
    model.add(Flatten(input_shape=(160, 320, 3)))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam")
    model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=20)
    model.save("model.h5")
