import numpy as np
import math
import os
from matplotlib import pyplot as plt
from matplotlib import patches
import matplotlib.animation as animation


def rot_matrix(angle):
    return np.array([[math.cos(angle), -math.sin(angle)],[math.sin(angle),math.cos(angle)]])


def golden_ratio():
    return 0.5 * (-1 + math.sqrt(5.0))


def draw_square_rect(xy, w, h, angle):
    return plt.Rectangle(xy, w, h, angle, ec='k', fill=False)


def draw_square_plot(xy, w, h):
    xs = [xy[0], xy[0] ,xy[0] + w ,xy[0] + w,xy[0]]
    ys = [xy[1], xy[1] + h, xy[1] + h ,xy[1] ,xy[1]]
    return plt.plot(xs,ys, linestyle="-",linewidth = 0.5),


def draw_square_fill(xy, w, h):
    xs = [xy[0], xy[0] ,xy[0] + w ,xy[0] + w,xy[0]]
    ys = [xy[1], xy[1] + h, xy[1] + h ,xy[1] ,xy[1]]
    return plt.fill(xs,ys, linestyle="-",linewidth = 0.5),


def main():
    print("Draw fractal.")
    
    fig = plt.figure(figsize=(16, 12))
    plt.axes().set_aspect('equal')
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)

    dir = "./img"
    if os.path.exists(dir) is not True:
        os.mkdir(dir)

    n = 20
    xy = np.c_[np.array([-2.0, -2.0])]
    v = np.c_[np.array([4.0, 4.0])] 
    currentAngle = 0
    imgs = []

    for i in range(n):
        print("--------------")

        v = np.dot(rot_matrix(currentAngle) , v)
        print(v)        

        img = draw_square_fill((xy[0], xy[1]), v[0], v[1])
        imgs.extend(img)

        xy = xy + v
        v = golden_ratio() * v
        currentAngle = -0.5 * math.pi
        fig.savefig(os.path.join(dir, 'img{:02}.png'.format(i)), dpi=200)

    fig.savefig(os.path.join(dir, 'img.png'), dpi=200)
    ani = animation.ArtistAnimation(fig, imgs)
    ani.save(os.path.join(dir, 'anim.gif'), writer="imagemagick")
    print('finished')
  

if __name__ == '__main__':
    main()
