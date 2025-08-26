# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 14:50:00 2025

@author: dlinogarda
"""

"""
Created Read Meta Data File Landsat 7 and Landsat 8
@author: dlinogarda@gmail.com
"""
"Add Machines"
"-----------------------------------------------------------------------------"
"For image plotting"
import matplotlib.image as mpimg
import numpy
#from numpy import zeros
"For open the window"
from tkinter import filedialog
import os
import re 
#import pandas
import datetime
from PIL import Image
# import cv2
import rasterio
"-----------------------------------------------------------------------------"


class SatelliteImage:
    def readImage():
        "Open Window and read Files"
        file_paths = filedialog.askopenfilenames(title='Choose Meta Data files')
        numfile = numpy.array(file_paths).shape[0]
        currentpath = "/".join(os.getcwd().split('\\')); print(currentpath)
        numfilepath = {}
        data = []
        image_data = []
        for i in range (numfile):
            # Open an image file
            data = rasterio.open(file_paths[i])
            image_data.append(rasterio.open(file_paths[i]).read([1,2,3,4]))
            numfilepath[i] = file_paths[i].split('/')
        return image_data