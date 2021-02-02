from pathlib import Path

import cv2
import numpy as np
import matplotlib.pyplot as plt


class MyImage:

    def __init__(self, name, image_path, timeout_sec=10):
        self._name = name
        path = Path(image_path).resolve()
        assert path.exists()
        self._timeout_sec = timeout_sec
        self._img_path = str(path)
        self._img = cv2.imread(self._img_path)
        assert self._img is not None

    @property
    def name(self):
        return self._name

    def __str__(self):
        s = f'{self.name} {self.img_path}'
        return s

    def show(self, timeout_sec=None):
        cv2.imshow(self.name, self._img)
        timeout = timeout_sec or self._timeout_sec
        k = cv2.waitKey(timeout * 1000)
        cv2.destroyAllWindows()
        return k

    @staticmethod
    def show(name, img, timeout_sec=10):
        cv2.imshow(name, img)
        k = cv2.waitKey(timeout_sec * 1000)
        cv2.destroyAllWindows()
        return k

    def plot(self):
        # plt.ion()  # turn on interactive mode, non-blocking `show`
        # BGR -> RGB
        # ::-1 in the last position is responsible for reversing the order of channels
        plt.imshow(self._img[:, :, ::-1])
        plt.pause(self._timeout_sec)

    @staticmethod
    def plot(name, img, timeout_sec=10):
        plt.imshow(img[:, :, ::-1])
        plt.pause(timeout_sec)

    @property
    def shape(self):
        return self._img.shape

    def water_mirror(self):
        # Create a new array with double the height
        h, w = self.shape[0], self.shape[1]
        mirror = np.zeros((2*h, w, 3), dtype=np.uint8)
        mirror[:h][:] = self._img
        inverted = self._img[::-1, :, :]
        mirror[h:][:] = inverted
        return mirror


if __name__ == '__main__':
    path = "./images/lion.jpg"
    img = MyImage('lion', path)
    assert "lion" in img.name
    # img.show()
    # img.plot()
    print(f"shape {img.shape}")
    # shape (579, 910, 3)
    m = img.water_mirror()
    MyImage.plot("mirror", m)


