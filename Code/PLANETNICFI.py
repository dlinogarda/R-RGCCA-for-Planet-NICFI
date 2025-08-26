# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 14:52:48 2025

@author: dlinogarda@gmail.com
"""


"Add Machines"
from PLANETools import SatelliteImage
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Read Info
Data = SatelliteImage.readImage()

a= Data

plt.imshow(a[0][3])