import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import patches


def draw_square(xy, w, h, angle):
    return patches.Rectangle(xy, w, h, angle, ec='k', fill=False)


def main():
    print("Draw fractal.")

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)

    rectangle = draw_square((-0.5, 0.5), 1.0, 1.0, -90)
    ax1.add_patch(rectangle)

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    ax1.set_aspect('equal')

    fig.savefig('img.png', dpi=800)
    print('finished')
  

if __name__ == '__main__':
    main()
