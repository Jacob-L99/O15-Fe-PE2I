# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 13:13:56 2024

@author: jacke
"""
import matplotlib.pyplot as plt
import numpy as np

def ref_con(motion_corrected_data):
    
    motion_corrected_data=np.array(motion_corrected_data)

    cerebellum_dex=np.load('cerebellum_dex_down_corrected.npy')
    cerebellum_sin=np.load('cerebellum_sin_down_corrected.npy')
    grey=np.load('Register_grey_matter.npy')

    grey=np.flip(grey, axis=1)
    grey=np.flip(grey, axis=2)
    

    Ref_concentration=motion_corrected_data*(cerebellum_dex+cerebellum_sin)
    
    Ref_TAC = []
    
    # Loop over the first dimension (t)
    for frame in Ref_concentration:
        # Get all non-zero values in the frame
        non_zero_values = frame[frame != 0]
        
        # Calculate the mean of non-zero values
        if non_zero_values.size > 0:
            mean_value = np.mean(non_zero_values)
        else:
            mean_value = 0  # Handle case where there are no non-zero values
        
        # Store the mean value
        Ref_TAC.append(mean_value)
    
    Ref_TAC = np.array(Ref_TAC)

    
    return Ref_TAC