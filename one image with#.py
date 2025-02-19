
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:13:33 2024

@author: Anjni Gorsiya
"""

import numpy as np
import matplotlib.pyplot as plt
from pims import ImageSequence

# Load TIFF images from a folder (adjust the file path and pattern accordingly)
file_pattern = "E:/3.1_files/*.tif"
images = ImageSequence(file_pattern)

# Assuming you want to process the first image in the sequence
image = images[515]

# Extract the green channel (adjust indices based on your image data)
ig = image[:, :, 1]

# Define a region of interest (adjust indices based on your specific ROI)
ig1 = ig[160:415, 350:850]

# Calculate mean intensities across columns
s = []

for i in range(ig1.shape[1]):
    column_data = ig1[:,i]
    mean_intensity = np.mean(column_data)
    s.append(mean_intensity)

# Plot the mean intensities
plt.plot(s)
plt.xlabel('Column Index')
plt.ylabel('Mean Intensity')
plt.title('Mean Intensity across Columns')
plt.show()
