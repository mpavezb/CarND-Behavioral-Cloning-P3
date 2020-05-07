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
    data_dir = "data/"
    data_dir = "/home/mpavezb/data/"

    def __init__(self):
        this_dir = os.path.dirname(os.path.realpath(__file__))
        self.project_path = os.path.realpath(this_dir + "/..")
        self.blacklist_fname = os.path.join(self.project_path, "blacklist.txt")

        print("=" * 80)
        print("Parameters:")
        print("=" * 80)
        print(" - Project Path: {}".format(self.project_path))
        print(" - Blacklist file: {}".format(self.blacklist_fname))
        print(" - Data Dir: {}".format(self.data_dir))
        print("")
