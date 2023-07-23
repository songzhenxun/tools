# Extract video frame
import cv2
import numpy as np
import os


# The videos go under the videos folder
current_path = os.path.abspath(".")
video_path = current_path + "/" + "videos/"
pic_path = current_path + "/" + "pics/"
videos_type = {"1": ".jpg", "2": ".png"}


# flag 1 for jpg,2 for png
def save_image(image, pic_path, video_name, name_label, flag):
    folder = os.path.exists(pic_path)
    if not folder:
        os.makedirs(pic_path)
    pic_name = video_name + "_" + str(name_label) + videos_type[flag]
    cv2.imwrite(pic_path + pic_name, image)
    return pic_name


# Read videos
# timeF  The parameter is used for capturing the picture by frame
def video_in(timeF):
    dirs = os.listdir(video_path)
    for v in dirs:
        i = 0
        name_label = 0
        videoCapture = cv2.VideoCapture(video_path + "/" + str(v))
        video_name = v.replace(".mp4", "", 1)
        success, frame = videoCapture.read()
        while success:
            i += 1
            if (i % timeF == 0):
                name_label += 1
                pic_name = save_image(
                    frame, pic_path, video_name, name_label, "1")
                print('save image:', video_name, "  ", pic_name)
            success, frame = videoCapture.read()


if __name__ == "__main__":
    video_in(30)

# TODO: add add_argument()
