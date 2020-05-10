from math import ceil

from keras.layers import Convolution2D
from keras.layers import Cropping2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Lambda
from keras.layers import MaxPooling2D
from keras.models import Sequential


from src.parameters import Parameters
from src.data_loader import load_datasets
from src.processing import split_samples, augment_samples, sample_generator


if __name__ == "__main__":
    # load and augment dataset
    samples = load_datasets()
    samples = augment_samples(samples)

    # split and create batch generators for train and validation
    train_samples, validation_samples = split_samples(samples)
    train_generator = sample_generator(train_samples, Parameters.BATCH_SIZE)
    validation_generator = sample_generator(validation_samples, Parameters.BATCH_SIZE)

    # model definition
    model = Sequential()
    model.add(
        Lambda(
            lambda x: (x / 255.0) - 0.5,
            input_shape=(Parameters.IMAGE_HEIGHT, Parameters.IMAGE_WIDTH, 3),
        )
    )

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

    # train
    model.compile(loss="mse", optimizer="adam")
    model.fit_generator(
        train_generator,
        validation_data=validation_generator,
        steps_per_epoch=ceil(len(train_samples) / Parameters.BATCH_SIZE),
        validation_steps=ceil(len(validation_samples) / Parameters.BATCH_SIZE),
        epochs=Parameters.N_EPOCHS,
        verbose=1,
    )

    # save
    model.save("model.h5")
