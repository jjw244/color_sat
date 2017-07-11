#! /bin/python3
import argparse #might have to install this on your python version
from skimage import data

#import numpy libs
def saturate(img):
    photo_data = misc.imread('./wifire/971276_10201598950433282_948247132_n.jpg')

    red_mask   = photo_data[:, : , 0] < 210
    green_mask = photo_data[:, : , 1] > 20
    blue_mask  = photo_data[:, : , 2] < 100

    final_mask = np.logical_and(red_mask, green_mask, blue_mask)
    photo_data[final_mask] = 2550
    plt.figure(figsize=(15,15))
    plt.imshow(photo_data)


def blur(img):
    return 0
## main

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-s",
        "--saturate",
        help="perform for just one org assignment",
        action="store_true")
    parser.add_argument(
        "-b",
        "--blur",
        help="perform for just one org assignment",
        action="store_true")
    parser.add_argument(
        "image",
        help="perform for users in Zendesk",
        action="store_true")

org_image = parser.args.image

if saturate:
  return saturate(org_image)

### python  Untitle.py  -s org_image.jpg > saturated_image.jpg
