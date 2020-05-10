import os.path
import csv

from src.parameters import Parameters
from src.processing import Sample


class Blacklist:
    def __init__(self, fname):
        self.fname = fname
        self.blacklist = self.load()
        self.not_valid_count = 0

    def load(self):
        print(" - Loading blacklist from file: {}:".format(self.fname))
        blacklist = []
        with open(self.fname) as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                line_str = "".join(line)
                if len(line) == 0 or line_str[0] == "#":
                    continue
                blacklist.append(line)
        return blacklist

    def is_valid(self, fname):
        strip_name = fname.split("/")[-1]
        strip_name = strip_name.split(".")[0]
        strip_name = strip_name.replace("center_", "")
        for entry in self.blacklist:
            start_name = entry[0]
            end_name = entry[1]
            if start_name <= strip_name and strip_name <= end_name:
                self.not_valid_count += 1
                return False
        return True


class LogEntry:
    def __init__(self, line, img_directory):
        self.fname_center = os.path.join(img_directory, line[0].split("/")[-1])
        self.fname_left = os.path.join(img_directory, line[1].split("/")[-1])
        self.fname_right = os.path.join(img_directory, line[2].split("/")[-1])
        self.steering_center = float(line[3])
        self.throttle = float(line[4])
        self.break_value = float(line[5])
        self.speed = float(line[6])


class DBLogReader:
    def __init__(self, dataset_directory):
        self.img_directory = os.path.join(dataset_directory, "IMG")
        self.log_fname = os.path.join(dataset_directory, "driving_log.csv")
        self.entries = []

    def load(self):
        print(" - Loading entries from log file: {}:".format(self.log_fname))
        entries = []
        try:
            with open(self.log_fname) as csvfile:
                reader = csv.reader(csvfile)
                for line in reader:
                    entries.append(LogEntry(line, self.img_directory))
        except IOError as e:
            print(" - !! Could not load csv: {}".format(self.fname))
        self.entries = entries

    def get_entries(self):
        if not self.entries:
            self.load()
        return self.entries


def get_dataset_samples(dataset_directory):
    print("Loading dataset from path: {}:".format(dataset_directory))

    # blacklist
    blacklist = Blacklist(Parameters.BLACKLIST_FNAME)

    # csv
    log_reader = DBLogReader(dataset_directory)
    entries = log_reader.get_entries()

    # load valid samples
    samples = []
    for entry in entries:
        # skip blacklisted samples
        if not blacklist.is_valid(entry.fname_center):
            continue

        # create adjusted steering measurements for the side camera images
        steering_left = entry.steering_center + Parameters.MULTICAM_STEERING_CORRECTION
        steering_right = entry.steering_center - Parameters.MULTICAM_STEERING_CORRECTION

        # create samples
        samples.append(Sample(entry.fname_center, entry.steering_center))
        samples.append(Sample(entry.fname_left, steering_left))
        samples.append(Sample(entry.fname_right, steering_right))

        # limit samples
        limit = Parameters.IMAGE_LIMIT_PER_SET
        if limit and len(samples) >= limit:
            break

    print(" - Found #{} images.".format(len(entries)))
    print(" - Will consider #{} of them.".format(len(samples)))
    print(" - #{} are blacklisted.".format(blacklist.not_valid_count * 3))
    print("")
    return samples


def load_datasets():
    print("=" * 80)
    print("Loading Datasets ...")
    print("=" * 80)
    all_samples = []
    for dataset_name in Parameters.DATASETS:
        dataset_directory = os.path.join(Parameters.DATA_DIR, dataset_name)
        samples = get_dataset_samples(dataset_directory)
        all_samples.extend(samples)

    print(
        "Using #{} images from #{} datasets.".format(
            len(all_samples), len(Parameters.DATASETS)
        )
    )
    print("")
    return all_samples
