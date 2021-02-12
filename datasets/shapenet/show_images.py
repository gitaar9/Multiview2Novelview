import h5py
import random

from PIL import Image
import numpy as np


def get_random_image(dataset="ship"):
    data = eval("{}_data".format(dataset))
    ids = eval("{}_ids".format(dataset))
    random_id = random.choice(ids)
    return data[random_id]['image'].value


def show_image(img_array):
    img = Image.fromarray(img_array)
    img.show()


def show_random_image(dataset="ship"):
    show_image(get_random_image(dataset))


chair_data = h5py.File('data_chair.hdf5', 'r')
ship_data = h5py.File('data_ship.hdf5', 'r')

chair_ids = chair_data.keys()
ship_ids = ship_data.keys()

chair_img = chair_data[chair_ids[-1]]['image'].value
ship_img = ship_data[ship_ids[-1]]['image'].value

for i in range(5):
    img_array = get_random_image()
    show_image(img_array)
    img_array = np.interp(img_array, (img_array.min(), img_array.max()), (0, 255)).astype(np.uint8)
    show_image(img_array)
    # show_random_image('chair')
    # show_random_image('ship')
