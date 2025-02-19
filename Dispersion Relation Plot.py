# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:43:38 2024

@author: Anjni Gorsiya
"""

import numpy as np
import matplotlib.pyplot as plt
import math 

Ti = 0.03*1.6*10**(-19) #in eV
Te = 1*11606 #in eV
ne = 10**15 #in /m^3
nd = 10**11 #in m^3
md = 2.99* 10**(-13)
Zd = 10**4
E0= 8.854 * 10**(-12)
e= 1.6 * 10**(-19)
Kb= 1.38 * 10**(-23)

ni = ne + nd*Zd
print(" ni=",ni)

lambdaDe = np.sqrt(E0*Kb*Te/(ne*e*e))
print("lambdaDe =",lambdaDe) #meter

lambdaDi = np.sqrt((E0*Kb*Ti)/(ni*e*e))
print("lambdaDi=",lambdaDi)   #meter

lambdaD = lambdaDe*lambdaDi/(np.sqrt(lambdaDe*lambdaDe + lambdaDi*lambdaDi))
print("lambdaD",lambdaD)   # Debye Length in meter

qd = Zd*e
print("qd=",qd)

omega_pd_rad = np.sqrt(qd*qd*nd/(E0*md))  #rad/sec
print("omega_pd_rad=",omega_pd_rad)

omega_pd= omega_pd_rad/(2*3.14)   #1/sec
#print("omega_pd=",omega_pd)

Cd = omega_pd_rad*lambdaDi    #Dust Acoustic Velocity in m/s
print("Cd=",Cd)   #m/sec

# Wave number range
k = np.linspace(0, 5, 10000)  # Adjust the range and number of points as needed

# Calculate angular frequency (dispersion relation)
omega = k*0.09/ (np.sqrt(1 + (k*lambdaD)**2))
x1=[1.73655,
2.95752,
2.81861,
4.41213,
2.40609,
1.7029,
1.703586,
4.507539,
2.43155,
1.70961]
y1=[19.46863571,
26.46578177,
23.96673389,
42.84770338,
22.63100449,
14.0744685,
10.2939183,
38.09116116,
16.63403903,
11.77731523
]



# Plotting
plt.figure(figsize=(8, 6))
plt.plot(k, omega, label=r'$\omega(k) = \frac{k C_d}{\sqrt{1 + (k^2 \lambda_D^2)}}$')
#plt.scatter(x1,y1)
plt.xlabel('Wave number $k$')
plt.ylabel('Angular frequency $\omega$')
plt.title('Dispersion Relation of Dust Acoustic Wave')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
