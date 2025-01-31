import numpy as np
import matplotlib.pyplot as plt
from random import shuffle

# Implement an artificial neural netword for Optical Character Recognition (OCR). 
# Use multilayer perceptron (MLP) with a single hidden layer

# charstr = """
#           OOOOOO  OOOOOO  OOOOOO  OO..OO
#           OOOOOO  OOOOOO  OOOOOO  OO..OO
#           O.OO.O  OO..OO  ..OO..  OO..OO
#           O.OO.O  OO..OO  ..OO..  OOOOOO
#           O....O  OOOOOO  ..OO..  OO..OO
#           O....O  OO..OO  ..OO..  OO..OO
#           O... O  OO..OO  ..OO..  OO..OO
#           """


# training is a size 42 x 4 array contianing the 42 pixel-values for each of the 4 characters. This is the result from the OCR.jl file after reshaping
# target is a size 2 x 4 array containing the desired output for each of the 4 characters
# mapstr is the string "MATH" which is the characters that each target output corresponds to 

import numpy as np

training = np.array([
    [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], 
    [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], 
    [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 1, 1], 
    [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], 
    [1, 0, 1, 1], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 1], [1, 1, 1, 1], 
    [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [0, 1, 0, 1], [1, 1, 1, 1], 
    [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1], [1, 1, 0, 1]
])

target = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
target_transposed = target.T

mapstr = "MATH"

def plot_chars(images):
    plt.gray()  # Use grayscale
    n_images = images.shape[1]  # Number of images
    rows = int(np.ceil(n_images / 4))  # Number of rows for subplots

    for j in range(n_images):
        im = np.copy(np.reshape(images[:, j], (7, 6), order='F'))  # order='F' is important here, it forces reshaping to follow column-major (Fortran-style) order, which is the default reshaping order in Julia
        im = 1 - im.copy()  # Invert the values

        # Display the image
        plt.subplot(rows, 4, j + 1)
        plt.imshow(im, cmap='gray')
        plt.axis('off')  # Hide axis
    
    plt.show()
#plot_chars(training)

# Now need to generate noisy test characters to test the trained OCR code. Modify the true character images in training

def make_testdata(training):
    testdata = np.zeros((42, 20), dtype=int)
    testdata[:, 0:4] = training
    
    for i in range(4):
        numberPixelsChange = 2 * (i + 1)
        img = training
        for j in range(4):
            jthLetter = img[:, j].copy()
            indicesToFlip = list(range(42))
            shuffle(indicesToFlip)
            indicesToFlip = indicesToFlip[:numberPixelsChange]
            for index in indicesToFlip:
                jthLetter[index] = 1 if jthLetter[index] == 0 else 0  # Flips the value from 0 to 1, and vice versa
            columnAffected = 4 + i * 4 + j
            testdata[:, columnAffected] = jthLetter
    return testdata

testdata = make_testdata(training)
plot_chars(testdata)