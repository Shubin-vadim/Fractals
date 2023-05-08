import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

"""
    Необходимые параметры для построения множества
"""
n_iter = 40
x_min = -4
x_max = 4
n_points_x = 100
y_min = -2
y_max = 2
n_points_y = 100
R = 1e-4
C = 1
colors = ['b', 'g', 'r', 'y', 'k']


def f(z: complex, c: complex) -> complex:
    return z ** 5 + c


def fdiff(z: complex) -> complex:
    return 5 * z ** 4


def build_newton_fractal(z0, c, max_iters, r) -> int:
    z = z0
    for i in range(max_iters):
        dz = f(z, c) / fdiff(z)
        if abs(dz) < r:
            return z
        z -= dz
    return False


def get_root(roots: list, r):
    try:
        return np.where(np.isclose(roots, r))[0][0]
    except IndexError:
        roots.append(r)
        return len(roots) - 1


def plot_fractal(xmin, xmax, points_x, ymin, ymax, points_y, c, max_iters, r) -> None:
    X_points = np.linspace(xmin, xmax, points_x)
    Y_points = np.linspace(ymin, ymax, points_y)
    cmap = ListedColormap(colors=colors)
    roots = []
    field = np.zeros((points_x, points_y))
    for ix, x in enumerate(X_points):
        for iy, y in enumerate(Y_points):
            z0 = x + y * 1j
            r = build_newton_fractal(z0, c, max_iters, r)
            if r is not False:
                ir = get_root(roots, r)
                field[iy, ix] = ir

    plt.imshow(field, cmap=cmap)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    plot_fractal(x_min, x_max, n_points_x, y_min, y_max, n_points_y, C, max_iters=n_iter, r=R)

