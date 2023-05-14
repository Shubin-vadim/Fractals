import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from typing import Union


class NewtonFractal:
    def __init__(self) -> None:
        """
        Необходимые параметры для построения множества
        """
        self.n_iter = 20000
        self.xmin = -1
        self.xmax = 1
        self.n_points_x = 300
        self.ymin = -1
        self.ymax = 1
        self.n_points_y = 300
        self.colors = ['b', 'g', 'r', 'y', 'k']

    def __f(self, z: complex, c: complex) -> complex:
        return z ** 5 + c

    def __fdiff(self, z: complex) -> complex:
        return 5 * z ** 4

    def __build_newton_fractal(self, z, c, r, max_iter=1000) -> int:
        for i in range(max_iter):
            dz = self.__f(z, c) / self.__fdiff(z)
            if abs(dz) < r:
                return z
            z -= dz
        return False

    def __get_root_index(self, roots, rez, r) -> Union[int, np.array]:
        try:
            return np.where(np.isclose(roots, rez, atol=r))[0][0]
        except IndexError:
            roots.append(rez)
            return len(roots) - 1

    def plot_fractal(self, c=-1, r=1e-10, px=1) -> None:
        plt.figure(figsize=(10, 10))
        roots = []
        m = np.zeros((self.n_points_x, self.n_points_y))
        cmap = ListedColormap(self.colors)
        self.xmin *= px
        self.xmax *= px
        self.ymin *= px
        self.ymax *= px
        X_points = np.linspace(self.xmin, self.xmax, self.n_points_x)
        Y_points = np.linspace(self.ymin, self.ymax, self.n_points_y)
        for ix, x in enumerate(X_points):
            for iy, y in enumerate(Y_points):
                z0 = x + y * 1j
                rez = self.__build_newton_fractal(z0, c, r, self.n_iter)
                if rez is not False:
                    ir = self.__get_root_index(roots, rez, r)
                    m[iy, ix] = ir

        plt.imshow(m, cmap=cmap, origin='lower')
        plt.axis('off')
        plt.show()
