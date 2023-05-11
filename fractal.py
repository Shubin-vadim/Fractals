import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

"""
    Необходимые параметры для построения множества
"""
n_iter = 20000
xmin = -1
xmax = 1
n_points_x = 250
ymin = -1
ymax = 1
n_points_y = 250
R = 1e-10
C = -1
colors = ['b', 'g', 'r', 'y', 'k']


def f(z: complex, c: complex) -> complex:
    return z ** 5 + c


def fdiff(z: complex) -> complex:
    return 5 * z ** 4


def build_newton_fractal(z, c, r, max_iter=1000) -> int:
    for i in range(max_iter):
        dz = f(z, c)/fdiff(z)
        if abs(dz) < r:
            return z
        z -= dz
    return False


def get_root_index(roots, rez, r):
    try:
        return np.where(np.isclose(roots, rez, atol=r))[0][0]
    except IndexError:
        roots.append(rez)
        return len(roots) - 1


def plot_fractal(c, points_x=200, points_y=200, domain=(-1, 1, -1, 1), iters=1000, r=1e-10) -> None:
    roots = []
    m = np.zeros((points_x, points_y))
    cmap = ListedColormap(colors)
    xmin, xmax, ymin, ymax = domain
    X_points = np.linspace(xmin, xmax, points_x)
    Y_points = np.linspace(ymin, ymax, points_y)
    for ix, x in enumerate(X_points):
        for iy, y in enumerate(Y_points):
            z0 = x + y*1j
            rez = build_newton_fractal(z0, c, r, iters)
            if rez is not False:
                ir = get_root_index(roots, rez, r)
                m[iy, ix] = ir

    plt.imshow(m, cmap=cmap, origin='lower')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    plot_fractal(C, points_x=n_points_x, points_y=n_points_y, domain=(xmin, xmax, ymin, ymax), iters=n_iter, r=R)


