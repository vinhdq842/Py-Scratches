"""
@author: SOE

Image compression using Singular Value Decomposition (svd)
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

path = "is-Linh.jpg"

img = Image.open(path)
s = float(os.path.getsize(path)) / 1024
print("Size(dimension): ", img.size)
plt.title("Original Image (%.2f Kb):" % s)
plt.imshow(img)
plt.axis("off")
plt.show()

img_matrix_red = np.array(list(img.getdata(band=0)), float)
img_matrix_green = np.array(list(img.getdata(band=1)), float)
img_matrix_blue = np.array(list(img.getdata(band=2)), float)

img_matrix_red.resize(img.size[1], img.size[0])
img_matrix_green.resize(img.size[1], img.size[0])
img_matrix_blue.resize(img.size[1], img.size[0])

img_matrix_red = np.matrix(img_matrix_red)
img_matrix_green = np.matrix(img_matrix_green)
img_matrix_blue = np.matrix(img_matrix_blue)

U_r, S_r, Vt_r = np.linalg.svd(img_matrix_red)
U_g, S_g, Vt_g = np.linalg.svd(img_matrix_green)
U_b, S_b, Vt_b = np.linalg.svd(img_matrix_blue)

print("Dimension of A is: ", img_matrix_red.shape)

fig, sub = plt.subplots(1, 4)

for s, i in zip(sub.flat, range(10, 90, 20)):
    cmp_img_r = np.matrix(U_r[:, :i]) * np.diag(S_r[:i]) * np.matrix(Vt_r[:i, :])
    cmp_img_g = np.matrix(U_g[:, :i]) * np.diag(S_g[:i]) * np.matrix(Vt_g[:i, :])
    cmp_img_b = np.matrix(U_b[:, :i]) * np.diag(S_b[:i]) * np.matrix(Vt_b[:i, :])
    img_r = Image.fromarray(cmp_img_r).convert("L")
    img_g = Image.fromarray(cmp_img_g).convert("L")
    img_b = Image.fromarray(cmp_img_b).convert("L")
    new_img = Image.merge("RGB", (img_r, img_g, img_b))
    s.imshow(new_img)
    s.set_title(f"{i} singular values remained")
    s.axis(False)
    new_img.save('remained-%s.jpg' % i)

plt.show()
