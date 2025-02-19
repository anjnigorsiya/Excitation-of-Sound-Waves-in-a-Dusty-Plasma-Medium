# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 10:54:24 2024

@author: Anjni Gorsiya
"""

import numpy as np
import matplotlib.pyplot as plt
from pims import ImageSequence

# Load images from a sequence of TIFF files
file_pattern = "E:/3.1_files/*.tif"
images = ImageSequence(file_pattern)

"""
After executing s1=[], the variable s1 can be used to store a list of values. 
Initially, it contains no elements, but you can add elements to it later using 
various list operations like .append() or by directly assigning a list of values.
"""
s1=[]  

#Process each image in the sequence 
#select the range according to how many picture you need
 
for i in range(50):  
    #From whole file at which we have to start upload image,this is indicate below
    ig = images[505+i][:, :, 1]
    #select the region of intrest
    ig1 = ig[70:700, 1300:2000]
    #[505+i] it means you are upload 506th image from your file
    # 70:700 it means you are selecting 630 row index
    # 1300:2000 it means you are selecting 700 coloumn index
    back=images[1159][:, :, 2]
    #mention that region of intrest(ROI) is same for both ig1 and back1
    back1=back[70:700, 1300:2000]
    #substract two images 
    diff=ig1-back1
    #variable s can be used to store a list of values 
    #here this store diff variable value
    s=[]
    #in for loop each itration,values is enters & by this append command all append
    s1.append(s)

    # Calculate mean intensity for each column
    # select the range = coloumn index difference of ROI
    for i in range(700):
        column_data = ig1[:, i]
        mean_intensity = np.mean(column_data)
        #used to add the value of mean_intensity to the 
        #end of the list s, it expanding the list by one element.
        s.append(mean_intensity)
  
#Plot colour Picture of wave propagation combine all images which you selected   
#first value=at which we have to start plot
#secound value=at which we have to end plot
#third value for x=coloumn index difference of ROI
#third value for y=select the range according to how many picture you need
x=np.linspace(0,100,700)   
y=np.linspace(0,100,50)  
#This function in Matplotlib is used to create a pseudocolor plot of a 2D array.
plt.pcolor(y,x,np.transpose(s1))
plt.xlabel('coloumn index')
plt.ylabel('No. of picture taken')
plt.show()

# Plot mean intensities for the All combined image
plt.figure(figsize=(8, 6))  
plt.plot(s)
plt.xlabel('Column Index')
plt.ylabel('Mean Intensity')
plt.title('Mean Intensity across Columns - Image')
plt.grid(True)
plt.show()
