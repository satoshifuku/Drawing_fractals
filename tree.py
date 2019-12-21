import matplotlib.pyplot as plt
import matplotlib.cm as cm
import math

def drawTree_symmetry(x1, y1, radian, recursion_n):

    if recursion_n >= 0:

        x2 = x1 + math.cos(radian) * recursion_n
        y2 = y1 + math.sin(radian) * recursion_n

        x_list = [x1, x2]
        y_list = [y1, y2]        

        plt.plot(x_list, y_list, linestyle="-",color=cm.hsv(recursion_n / 5.0),linewidth=3.0)
        n_div = 4
        weight = 0.5
        for i in range(n_div):
            rot = radian + weight * (i * math.pi/n_div + 0.5 * math.pi * ((1 - n_div) / n_div))
            drawTree_symmetry(x2, y2, rot, recursion_n - 1)                



def drawTree_simple(x1, y1, radian, recursion_n):
    
    if recursion_n >= 0:

        x2 = x1 + math.cos(radian) * recursion_n
        y2 = y1 + math.sin(radian) * recursion_n

        x_list = [x1, x2]
        y_list = [y1, y2]        

        plt.plot(x_list, y_list, linestyle="-",color=cm.hsv(recursion_n / 5.0),linewidth=3.0)

        drawTree_simple(x2, y2, radian - 0.15 * math.pi, recursion_n - 1)
        drawTree_simple(x2, y2, radian + 0.15 * math.pi, recursion_n - 1)



def main():
    print("Draw fractal tree.")
    
    fig = plt.figure(figsize=(32, 24))
    plt.axes().set_aspect('equal')

    drawTree_simple(1, 1, 0.5 * math.pi, 7)

    fig.savefig('img.png', dpi=200)


if __name__ == "__main__":
    main()
