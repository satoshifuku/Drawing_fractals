import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import patches




def rot_matrix(angle):
    return np.array([[math.cos(angle), -math.sin(angle)],[math.sin(angle),math.cos(angle)]])


def golden_ratio():
    return 0.5 * (-1 + math.sqrt(5.0))


def draw_square(xy, w, h, angle):
    return patches.Rectangle(xy, w, h, angle, ec='k', fill=False)


def main():
    print("Draw fractal.")
    
    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)

    xy = np.c_[np.array([0.0, 0.0])]
    v = np.c_[np.array([2.0, 2.0])] 
    currentAngle = 0
    for i in range(10):
        print("--------------")
        # print(xy)

        v = np.dot(rot_matrix(currentAngle) , v)
        print(v)        

        rectangle = draw_square((xy[0], xy[1]), v[0], v[1], 0)
        ax1.add_patch(rectangle)

        xy = xy + v
        v = golden_ratio() * v
        currentAngle = -0.5 * math.pi

    
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

    ax1.set_aspect('equal')

    fig.savefig('img.png', dpi=800)
    print('finished')
  

if __name__ == '__main__':
    main()
