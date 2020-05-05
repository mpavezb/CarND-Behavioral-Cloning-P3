from data_loader import load_dataset
import numpy as np

datasets = [
    "track1_forward",
    "track1_curves",
    "track1_recovery",
    "track1_reverse",
    "track2_forward",
    "track2_reverse",
]
data_dir = "../data"


if __name__ == "__main__":
    images, measurements = load_dataset("../data/", "track1_forward", limit=100)

    X_train = np.array(images)
    Y_train = np.array(measurements)

    from keras.models import Sequential
    from keras.layers import Flatten, Dense

    model = Sequential()
    model.add(Flatten(input_shape=(160, 320, 3)))
    model.add(Dense(1))
    model.compile(loss="mse", optimizer="adam")
    model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=7)
    model.save("model.h5")
