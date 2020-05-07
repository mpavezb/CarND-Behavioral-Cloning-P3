from keras.models import Sequential
from keras.layers import Flatten, Dense

from data_loader import load_dataset, load_datasets
import numpy as np

datasets = [
    "track1_forward",
    "track1_curves",
    "track1_recovery",
    "track1_reverse",
    "track2_forward",
    "track2_reverse",
]
data_dir = "data/"


if __name__ == "__main__":

    images, measurements = load_datasets(data_dir, datasets, limit=500, debug=False)

    X_train = np.array(images)
    y_train = np.array(measurements)

    model = Sequential()
    model.add(Flatten(input_shape=(160, 320, 3)))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam")
    model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=20)
    model.save("model.h5")
