import os.path
import csv
import cv2


def read_from_csv(fname):
    lines = []
    try:
        with open(fname) as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                lines.append(line)
    except IOError as e:
        print("- !! Could not load csv: {}".format(fname))
    return lines


def read_blacklist(parameters):
    blacklist = []
    fname = parameters.blacklist_fname
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            line_str = "".join(line)
            if len(line) == 0 or line_str[0] == "#":
                continue
            blacklist.append(line)
    return blacklist


def is_in_blacklist(blacklist, fname):
    strip_name = fname.split("/")[-1]
    strip_name = strip_name.split(".")[0]
    strip_name = strip_name.replace("center_", "")
    strip_name = strip_name.replace("right_", "")
    strip_name = strip_name.replace("left_", "")
    # print("fname: {}".format(fname))
    # print("strip_name: {}".format(strip_name))
    for entry in blacklist:
        start_name = entry[0]
        end_name = entry[1]
        if start_name <= strip_name and strip_name <= end_name:
            # print(
            #    " - File {} is blacklisted by rule [{}, {}].".format(
            #        fname, start_name, end_name
            #    )
            # )
            return True
    return False


def load_dataset(parameters, set_name, limit=None, debug=False):
    print("Loading dataset: {}:".format(set_name))

    images = []
    measurements = []

    img_basename = os.path.join(parameters.data_dir, set_name, "IMG")
    csv_fname = os.path.join(parameters.data_dir, set_name, "driving_log.csv")
    print("- Log file: {}:".format(csv_fname))

    blacklist = read_blacklist(parameters)
    blacklisted = []

    csv_lines = read_from_csv(csv_fname)
    for line in csv_lines:
        fname_center = os.path.join(img_basename, line[0].split("/")[-1])
        fname_left = os.path.join(img_basename, line[1].split("/")[-1])
        fname_right = os.path.join(img_basename, line[2].split("/")[-1])
        value_steering_angle = float(line[3])
        value_throttle = float(line[4])
        value_break = float(line[5])
        value_speed = float(line[6])

        image_fname = fname_center

        if is_in_blacklist(blacklist, image_fname):
            blacklisted.append(image_fname)
            continue

        image = cv2.imread(image_fname)
        images.append(image)
        measurements.append(value_steering_angle)

        if debug:
            print("- center: {}".format(fname_center))
            print("- left: {}".format(fname_left))
            print("- right: {}".format(fname_right))
            print("- steering angle: {:.2f} [-1.0, 1.0]".format(value_steering_angle))
            print("- throttle: {:.2f} [0.0, 1.0]".format(value_throttle))
            print("- break: {:.2f} (always zero?)".format(value_break))
            print("- speed: {:.2f} [0.0, 30.0]".format(value_speed))
            break

        if limit and len(images) >= limit:
            break

    if images:
        print("- Total images: {}.".format(len(csv_lines)))
        print(
            "- Loaded #{} images, and other #{} are blacklisted.".format(
                len(images), len(blacklisted)
            )
        )
    return images, measurements


def load_datasets(parameters, limit=None, debug=False):
    print("=" * 80)
    print("Datasets:")
    print("=" * 80)
    datasets = parameters.datasets

    all_images = []
    all_measurements = []
    for dataset in datasets:
        images, measurements = load_dataset(
            parameters, dataset, limit=limit, debug=debug
        )
        all_images.extend(images)
        all_measurements.extend(measurements)

    print("")
    print("Loaded #{} images from #{} datasets.".format(len(all_images), len(datasets)))
    print("")
    return all_images, all_measurements


if __name__ == "__main__":
    from parameters import Parameters

    parameters = Parameters()

    # single dataset
    # images, measurements = load_dataset(parameters, parameters.datasets[0], debug=True)

    # all of them
    images, measurements = load_datasets(parameters, limit=100, debug=False)
