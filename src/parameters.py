import os


class Parameters:
    datasets = [
        "track1_forward",
        "track1_curves",
        "track1_recovery",
        "track1_reverse",
        "track2_forward",
        "track2_reverse",
    ]

    multicam_steering_correction = 0.2
    IMAGE_LIMIT_PER_SET = 50
    N_EPOCHS = 2

    def __init__(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.project_path = os.path.realpath(this_dir + "/..")
        self.blacklist_fname = os.path.join(self.project_path, "blacklist.txt")
        self.data_dir = os.path.join(self.project_path, "data/")
        # self.data_dir = "/opt/mpavezb/data/"

        print("=" * 80)
        print("Parameters:")
        print("=" * 80)
        print(" - Project Path: {}".format(self.project_path))
        print(" - Blacklist file: {}".format(self.blacklist_fname))
        print(" - Data Dir: {}".format(self.data_dir))
        print(
            " - Multicam Steering Correction: {}".format(
                self.multicam_steering_correction
            )
        )
        print("")
