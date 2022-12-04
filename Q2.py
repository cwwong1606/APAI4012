import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image

def SVD(file = 'Q2example1.jpeg'):
    img = cv2.imread(file)[: ,:, 0]
    u, s, v = np.linalg.svd(img, full_matrices=False)
    return u, s, v

mat = cv2.imread('Q2example1.jpeg')
img = Image.fromarray(mat)
img.show()

print('Example 1, Original Image: ')
plt.imshow(cv2.imread('Q2example1.jpeg')[: ,:, 0], cmap='gray')
plt.show()

U, S, V = SVD('Q2example1.jpeg')
rates = S/S.sum()
components = np.einsum('jki,ikh->ijh', np.expand_dims(U, 1), np.expand_dims(V, 1))
print(f'Sum of singular values: {S.sum()}')

p = 0.9
s = np.where(rates.cumsum() > p)[0][0]
print(f'Rate of k-rank approximation: {p*100} %')
compressed = (rates[:s].reshape(-1, 1, 1)*components[:s]).sum(0)
plt.imshow(compressed, cmap='gray')
plt.show()

p = 0.7
s = np.where(rates.cumsum() > p)[0][0]
print(f'Rate of k-rank approximation: {p*100} %')
compressed = (rates[:s].reshape(-1, 1, 1)*components[:s]).sum(0)
plt.imshow(compressed, cmap='gray')
plt.show()

p = 0.5
s = np.where(rates.cumsum() > p)[0][0]
print(f'Rate of k-rank approximation: {p*100} %')
compressed = (rates[:s].reshape(-1, 1, 1)*components[:s]).sum(0)
plt.imshow(compressed, cmap='gray')
plt.show()

print('Example 2, Original Image: ')
plt.imshow(cv2.imread('Q2example2.jpeg')[: ,:, 0], cmap='gray')
plt.show()

U, S, V = SVD('Q2example2.jpeg')
rates = S/S.sum()
components = np.einsum('jki,ikh->ijh', np.expand_dims(U, 1), np.expand_dims(V, 1))
print(f'Sum of singular values: {S.sum()}')

p = 0.9
s = np.where(rates.cumsum() > p)[0][0]
print(f'Rate of k-rank approximation: {p*100} %')
compressed = (rates[:s].reshape(-1, 1, 1)*components[:s]).sum(0)
plt.imshow(compressed, cmap='gray')
plt.show()

p = 0.7
s = np.where(rates.cumsum() > p)[0][0]
print(f'Rate of k-rank approximation: {p*100} %')
compressed = (rates[:s].reshape(-1, 1, 1)*components[:s]).sum(0)
plt.imshow(compressed, cmap='gray')
plt.show()

p = 0.5
s = np.where(rates.cumsum() > p)[0][0]
print(f'Rate of k-rank approximation: {p*100} %')
compressed = (rates[:s].reshape(-1, 1, 1)*components[:s]).sum(0)
plt.imshow(compressed, cmap='gray')
plt.show()