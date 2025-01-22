import numpy as np
import matplotlib.pyplot as plt

# x: the angle, in degrees, being converted into radians
# returns the value of the angle in radians
def degs_to_rads(x):
    return x * np.pi / 180

# x: the polar angle, in degrees, used to derive cartesian coordinates
# returns an x-y coordinate pair equal to the polar mapping of the angle on a unit circle
def polar_to_cartesian(x):
    return np.cos(degs_to_rads(x)), np.sin(degs_to_rads(x))

# p: the number of points in the star's polygon frame
# q: the number of points being skipped to draw the star's lines
# returns a vector of x coordinates and a vector of corresponding y coordinates
def star_points(p, q):
    xy_frame = np.array([polar_to_cartesian(n * 360 / p) for n in range(0, p)])
    xframe = xy_frame[:,0]
    yframe = xy_frame[:,1]
    xstar = [xframe[n % p] for n in range(0, (p * q) + 1, q)]
    ystar = [yframe[n % p] for n in range(0, (p * q) + 1, q)]
    return xstar,ystar

# p: the number of points used to build the star's polygon frame
# q: the number of points being skipped to draw the star's lines
# displays the given coordinates plotted on a graph
def star_plotter(p, q, color):
    xcoords, ycoords = star_points(p,q)
    plt.plot(xcoords, ycoords, f'{color}-', markeredgecolor='k', markerfacecolor='k')
    plt.title(f'p = {p}, q = {q}')
    plt.axis('scaled')
    plt.gca().set_frame_on(False)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(f'star_{p}_{q}.png')
    plt.clf()
    return

# guides the user through the star-generating process
def gen_a_star():

    # ensures a valid p input from the user
    p = -1 # initial declaration
    while True:
        try:
            p = int(input("How many points do you want in your frame (p)? "))
            if p < 3:
                print("A frame needs to have at least 3 points. Please try again.\n")
            else:
                break
        except ValueError:
            print("That's not a valid integer. Please try again.\n")

    # ensures a valid q input from the user
    q = -1 # initial declaration
    while True:
        try:
            q = int(input("How many points do you want to skip each time to build your star (q)? "))
            if q < 1:
                print("You need to skip at least 1 point each time. Please try again.\n")
            else:
                break
        except ValueError:
            print("That's not a valid integer. Please try again.\n")

    # ensures a valid color input from the user
    color = -1 # initial declaration
    while True:
        color = input("What color of star do you want? \nAvailable options: \n  [b]lue \n  [m]agenta \n  [c]yan\n").lower()
        if not color.startswith(('b', 'm', 'c')):
            print("Invalid input. Please try again.\n")
        else:
            color = color[0]
            break
    star_plotter(p, q, color)
    
    while True:
        repeat = input("\nWould you like to generate another star? (y/n): ").lower()
        if repeat.startswith('y'):
            gen_a_star()
            break
        elif repeat.startswith('n'):
                print("Goodbye!")
                break
        else:
            print("Invalid input. Please respond with 'yes' or 'no'")
    return