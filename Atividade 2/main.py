import cv2
import numpy as np

img = cv2.imread('imagem.jpeg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

centerx = magnitude_spectrum.shape[0]//2
centery = magnitude_spectrum.shape[1]//2


new_img = cv2.imdecode(magnitude_spectrum, 0)

cv2.circle(new_img, magnitude_spectrum.shape, 50, 0, -1)


cv2.imwrite("test.jpg", new_img)
