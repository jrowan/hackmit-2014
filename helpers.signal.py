###HACKMIT 2014 - James Rowan, Milan Savani, Adam Rawot, and Noah Yonack
## orve
## helper functions for processing EEG signals from the orve

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import random

## param x the array of integer inputs for the function f to find peaks of
## param y the array of doubles f(x) 
## param peak_halfwidth an integer number of samples  in which to test
##          to gaurantee we have a distinct peak
##          defaults to 0
## param peak_height a double representing how far above nearby points
##          the peak has to be
##          defaults to 1e-05
## returns a numpy array containing a list of the locations of all peaks
def get_peaks(x, y, peak_halfwidth = 1, peak_height = 1e-05):
    return np.array([])
