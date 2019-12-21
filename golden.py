import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import patches


def main():
    print("Draw fractal.")

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    # patches.Rectangle((0.0, 0.0), 1, 1)
    rectangle = patches.Rectangle((-0.5, -0.5), 1.0, 1.0, ec='k', fill=False)
    ax1.add_patch(rectangle)

    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    ax1.set_aspect('equal')

    fig.savefig('img.png', dpi=800)
    print('finished')
  

if __name__ == '__main__':
    main()
