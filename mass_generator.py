import numpy as np
import matplotlib.pyplot as plt
import star_builder

# feel free to modify range constraints as desired!
for p in range(97,98):
    for q in range(1,97):
        # creates graphs in alternating colors
        if q * 2 == p: # would only generate a boring line
            pass # do nothing
        elif p % 2 == 0:
            star_builder.star_plotter(p,q,'m')
        else:
            star_builder.star_plotter(p,q,'b')