import os


def get_this_dir():
    return os.path.dirname(os.path.realpath(__file__))


def get_project_path():
    return os.path.realpath(get_this_dir() + "/..")


class Parameters:

    # datasets
    # ------------------------------------------------------
    DATA_DIR = os.path.join(get_project_path(), "data/")
    BLACKLIST_FNAME = os.path.join(get_project_path(), "blacklist.txt")
    DATASETS = [
        "track1_forward",
        "track1_curves",
        "track1_recovery",
        "track1_reverse",
        "track2_forward",
        "track2_reverse",
    ]
    IMAGE_LIMIT_PER_SET = 100

    BASE_IMAGE_WIDTH = 320
    BASE_IMAGE_HEIGHT = 160

    # preprocessing
    # ------------------------------------------------------
    IMAGE_CROP_TOP = 70
    IMAGE_CROP_BOTTOM = 25
    IMAGE_HEIGHT = BASE_IMAGE_HEIGHT - IMAGE_CROP_TOP - IMAGE_CROP_BOTTOM
    IMAGE_WIDTH = BASE_IMAGE_WIDTH

    # ------------------------------------------------------
    # augmentation
    MULTICAM_STEERING_CORRECTION = 0.2

    # training
    # ------------------------------------------------------
    N_EPOCHS = 3
    BATCH_SIZE = 32

    # Share of the db to be used for testing
    DB_TEST_SPLIT_SIZE = 0.2
