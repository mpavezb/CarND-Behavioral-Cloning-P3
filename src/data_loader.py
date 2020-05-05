import os.path
import csv
import cv2


def read_from_csv(fname):
    print("- Reading CSV: {}".format(fname))
    lines = []
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            lines.append(line)
    return lines


def read_blacklist(data_dir):
    blacklist = []
    fname = os.path.join(data_dir, "blacklist.txt")
    with open(fname) as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            line_str = "".join(line)
            if len(line) == 0 or line_str[0] == "#":
                continue
            # print(", ".join(line))
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


def load_dataset(data_dir, set_name, limit=None, debug=False):
    print("Loading Dataset: {}".format(set_name))
    images = []
    measurements = []

    img_basename = os.path.join(data_dir, set_name, "IMG")
    csv_fname = os.path.join(data_dir, set_name, "driving_log.csv")

    blacklist = read_blacklist(data_dir)
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

    print("- Total images: {}.".format(len(csv_lines)))
    print(
        "- Loaded #{}, and #{} are in blacklist.".format(len(images), len(blacklisted))
    )
    return images, measurements


if __name__ == "__main__":
    load_dataset("../data/", "track1_forward", debug=True)
