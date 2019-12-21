import numpy as np
import math
from matplotlib import pyplot as plt
from matplotlib import patches


def rot_matrix(angle):
    return np.array([[math.cos(angle), -math.sin(angle)],[math.sin(angle),math.cos(angle)]])


def golden_ratio():
    return 0.5 * (-1 + math.sqrt(5.0))


def draw_square(xy, w, h, angle):
    xs = [xy[0], xy[0] ,xy[0] + w ,xy[0] + w,xy[0]]
    ys = [xy[1], xy[1] + h, xy[1] + h ,xy[1] ,xy[1]]
    return plt.plot(xs,ys, linestyle="-")
    # return plt.Rectangle(xy, w, h, angle, ec='k', fill=False)


def main():
    print("Draw fractal.")
    
    fig = plt.figure(figsize=(16, 12))
    plt.axes().set_aspect('equal')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    n = 10
    xy = np.c_[np.array([-2.0, -2.0])]
    v = np.c_[np.array([4.0, 4.0])] 
    currentAngle = 0
    
    for i in range(n):
        print("--------------")

        v = np.dot(rot_matrix(currentAngle) , v)
        print(v)        

        rectangle = draw_square((xy[0], xy[1]), v[0], v[1], 0)
        # imgs.append(plt.axes().add_patch(rectangle))

        xy = xy + v
        v = golden_ratio() * v
        currentAngle = -0.5 * math.pi

    
    fig.savefig('img.png', dpi=800)
    print('finished')
  

if __name__ == '__main__':
    main()
