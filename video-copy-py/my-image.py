from pathlib import Path

import cv2
import numpy as np


class MyImage:

    def __init__(self, name, image_path):
        path = Path(image_path).resolve()
        assert path.exists()
        self._img_path = str(path)
        self.img = cv2.imread(self._img_path)
        self._name = name

    @property
    def name(self):
        return self._name

    def __str__(self):
        s = f'{self.name} {self.img_path}'
        return s

    def show(self, timeout=10):
        cv2.imshow(self.name, self.img)
        k = cv2.waitKey(timeout*1000)
        cv2.destroyAllWindows()


    # @property
    # def num_cols(self):
    #     return self._arr.shape[1]
    #
    # @property
    # def type(self):
    #     return self._arr.dtype


if __name__ == '__main__':
    img = "./images/lion.jpg"
    a = MyImage('lion', img)
    assert "lion" in a.name
    a.show()

