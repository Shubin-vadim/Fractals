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

    def __f(self, z: complex, c: complex) -> complex:   # заданная функция
        return z ** 5 + c

    def __fdiff(self, z: complex) -> complex:           # производная функции
        return 5 * z ** 4

    def __build_newton_fractal(self, z, c, r, max_iter=1000) -> int:   # приближение zn
        for i in range(max_iter):
            dz = self.__f(z, c) / self.__fdiff(z)
            if abs(dz) < r:
                return z
            z -= dz
        return False

    @staticmethod
    def __get_root_index(roots, rez, r) -> Union[int, np.array]:
        try:
            a = np.isclose(roots, rez, atol=r)   # проверяем насколько отличается rez от корней в roots
            b = np.where(a)[0][0]   # извлекаем самый первый элемент из кортежа списка
            return b                # возвращаем точку
        except IndexError:
            roots.append(rez)        # добавляем корень в массив
            return len(roots) - 1    # возвращаем значение для покраски точки, иначе её не будет

    def plot_fractal(self, c=-1, r=1e-10, px=1) -> None:
        plt.figure(figsize=(10, 10))  # размер окна matplotlib
        roots = []                    # список корней
        m = np.zeros((self.n_points_x, self.n_points_y))  # инициализация комплексной плоскости
        cmap = ListedColormap(self.colors)                # инициализация списка цветов для окрашевания точек
        self.xmin *= px
        self.xmax *= px
        self.ymin *= px
        self.ymax *= px                                   # масштабирование
        X_points = np.linspace(self.xmin, self.xmax, self.n_points_x)  # список точек по X
        Y_points = np.linspace(self.ymin, self.ymax, self.n_points_y)  # список точек по Y
        for ix, x in enumerate(X_points):
            for iy, y in enumerate(Y_points):
                z0 = x + y * 1j                                        # перебор точек z0
                zn = self.__build_newton_fractal(z0, c, r, self.n_iter)  # вычисление zn
                if zn is not False:
                    ir = self.__get_root_index(roots, zn, r)
                    m[iy, ix] = ir

        plt.imshow(m, cmap=cmap)
        plt.axis('off')
        plt.show()
