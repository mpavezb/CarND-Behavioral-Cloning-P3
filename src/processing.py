import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

from parameters import Parameters


class Sample:
    def __init__(self, fname, steering_angle):
        self.fname = fname
        self.steering_angle = steering_angle
        self.image = None
        self.is_flipped = False

    def flip_on_read(self):
        self.is_flipped = True

    def load(self):
        self.image = cv2.imread(self.fname)
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        if self.is_flipped:
            self.flip()

    def flip(self):
        self.image = cv2.flip(self.image, 1)
        self.steering_angle = self.steering_angle * -1.0

    def preprocess(self):
        # trim image to only see section with road
        ya = Parameters.IMAGE_CROP_TOP
        yb = ya + Parameters.IMAGE_HEIGHT
        self.image = self.image[ya:yb, :]

    def __str__(self):
        return (
            ""
            + "fname: {}\n".format(self.fname)
            + "flip: {}\n".format(self.flip)
            + "steering_angle: {}\n".format(self.steering_angle)
        )


def split_samples(samples):
    train_samples, validation_samples = train_test_split(
        samples, test_size=Parameters.DB_TEST_SPLIT_SIZE
    )
    return train_samples, validation_samples


def augment_samples(samples):
    augmented_samples = []  # samples
    for sample in samples:
        new_sample = sample
        new_sample.flip_on_read()
        augmented_samples.append(new_sample)
    return augmented_samples


def sample_generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1:  # Loop forever so the generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset : offset + batch_size]

            images = []
            angles = []
            for batch_sample in batch_samples:
                batch_sample.load()
                batch_sample.preprocess()
                images.append(batch_sample.image)
                angles.append(batch_sample.steering_angle)

            X_train = np.array(images)
            y_train = np.array(angles)
            yield shuffle(X_train, y_train)
