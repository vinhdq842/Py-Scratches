import numpy as np

matrix = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

det = np.linalg.det(matrix)
inv_matrix = np.linalg.inv(matrix)

inv_det = 0
while inv_det < 26:
    if (det * inv_det) % 26 == 1:
        break
    inv_det += 1

print((inv_matrix * inv_det * det) % 26)
inv_matrix = [[8, 5, 10], [21, 8, 21], [21, 12, 8]]
print(np.array(matrix) @ np.array(inv_matrix) % 26)

print(int("11", 2))
