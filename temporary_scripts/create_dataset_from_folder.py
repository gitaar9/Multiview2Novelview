import h5py
import numpy as np


h = h5py.File("test", 'w')


id = '123'
# Example of ids:
# f10263256eeb840b732c9e6120e90cf8_18_20
# 11c9c57efad0b5ec297936c81e7f6629_27_0
pose = np.array([2, 3])
# Example of poses:
# 27 0
# 18 20
# 0 20
image = np.array([1])  # Shape should be 256, 256, 3
h.create_group(id)

h['123'].create_dataset('pose', pose)
h['123'].create_dataset('image', image)