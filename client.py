import numpy as np
import matplotlib.pyplot as plt
import star_builder

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
            elif q >= p:
                print(f"There are only {p} points! Please try skipping a smaller amount.\n")
            elif q * 2 == p:
                print("This would only draw a line, not a star! Please try again.\n")
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
    star_builder.star_plotter(p, q, color)
    
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


# call to the user function
gen_a_star()