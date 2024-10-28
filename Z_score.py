# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 09:28:48 2024

@author: jacke
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')

def SD_corrected(transformed_K_1, ålder, kön):
    
    background=np.load('background_down_corrected.npy')
    
    grey = np.load('Register_grey_matter.npy')
    grey = np.flip(grey, axis=1)
    grey = np.flip(grey, axis=2)
    grey = np.where(grey > 0.5, 1, 0)
    
    Cerebellum_dex=np.load('cerebellum_dex_down_corrected.npy')*grey
    Cerebellum_mean_dex=np.sum(transformed_K_1*Cerebellum_dex)/np.sum(Cerebellum_dex)
    Cerebellum_sin=np.load('cerebellum_sin_down_corrected.npy')*grey
    Cerebellum_mean_sin=np.sum(transformed_K_1*Cerebellum_sin)/np.sum(Cerebellum_sin)
    
    middle_dex=np.load('middle_dex_down_corrected.npy')*grey
    middle_mean_dex=np.sum(transformed_K_1*middle_dex)/np.sum(middle_dex)
    middle_sin=np.load('middle_sin_down_corrected.npy')*grey
    middle_mean_sin=np.sum(transformed_K_1*middle_sin)/np.sum(middle_sin)
    
    posterior_dex=np.load('posterior_dex_down_corrected.npy')*grey
    posterior_mean_dex=np.sum(transformed_K_1*posterior_dex)/np.sum(posterior_dex)
    posterior_sin=np.load('posterior_sin_down_corrected.npy')*grey
    posterior_mean_sin=np.sum(transformed_K_1*posterior_sin)/np.sum(posterior_sin)
    
    anterior_dex=np.load('anterior_dex_down_corrected.npy')*grey
    anterior_mean_dex=np.sum(transformed_K_1*anterior_dex)/np.sum(anterior_dex)
    anterior_sin=np.load('anterior_sin_down_corrected.npy')*grey
    anterior_mean_sin=np.sum(transformed_K_1*anterior_sin)/np.sum(anterior_sin)
    
    
    # plt.imshow(grey[:,:,100])
    # plt.show()
    # plt.imshow(Cerebellum_dex[:,:,100])
    # plt.show()
    # plt.imshow(transformed_K_1[:,:,100])
    # plt.show()
    
    
    
    
    # Let's read the data directly from the text file named "Mean perfusion with slope and intersect"
    file_path = 'Mean perfusion with slope and intersect.txt'
    
    # Reading the text file and parsing it
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Extract the relevant lines, removing headers and footer sections
    data_lines = [line.strip() for line in lines if not line.startswith('%') and line.strip()]
    
    # Now let's split the values and create a list for each relevant column
    regions, means, stds, slopes, intersects = [], [], [], [], []
    
    for line in data_lines:
        if ':' in line:
            # This is the label "Male:" which we don't need to include
            continue
        parts = line.split(',')
        regions.append(parts[0].strip())
        means.append(float(parts[1].strip()))
        stds.append(float(parts[2].strip()))
        slopes.append(float(parts[3].strip()))
        intersects.append(float(parts[4].strip()))
    
    # Create a DataFrame from the parsed data
    df_from_file = pd.DataFrame({
        'Region': regions,
        'Mean': means,
        'Std': stds,
        'Slope': slopes,
        'Intersect': intersects
    })
    if kön=="M":
        calculated_cerebellum_mean_dex=slopes[1]*ålder+intersects[1]
        z_cerebellum_dex=(calculated_cerebellum_mean_dex-Cerebellum_mean_dex)/stds[9]
        calculated_cerebellum_mean_sin=slopes[0]*ålder+intersects[0]
        z_cerebellum_sin=(calculated_cerebellum_mean_sin-Cerebellum_mean_sin)/stds[0]
    
        calculated_middle_mean_sin=slopes[3]*ålder+intersects[3]
        z_middle_dex=(calculated_middle_mean_sin-middle_mean_sin)/stds[3]
        calculated_middle_mean_sin=slopes[2]*ålder+intersects[2]
        z_middle_sin=(calculated_middle_mean_sin-middle_mean_sin)/stds[2]
    
        calculated_posterior_mean_dex=slopes[5]*ålder+intersects[5]
        z_posterior_dex=(calculated_posterior_mean_dex-posterior_mean_dex)/stds[5]
        calculated_posterior_mean_sin=slopes[4]*ålder+intersects[4]
        z_posterior_sin=(calculated_posterior_mean_sin-posterior_mean_sin)/stds[4]
    
        calculated_anterior_mean_dex=slopes[7]*ålder+intersects[7]
        z_anterior_dex=(calculated_anterior_mean_dex-anterior_mean_dex)/stds[7]
        calculated_anterior_mean_sin=slopes[6]*ålder+intersects[6]
        z_anterior_sin=(calculated_anterior_mean_sin-anterior_mean_sin)/stds[6]
        
    else:
        calculated_cerebellum_mean_dex=slopes[9]*ålder+intersects[9]
        z_cerebellum_dex=(calculated_cerebellum_mean_dex-Cerebellum_mean_dex)/stds[9]
        print("Cerebellum dex: z =", (calculated_cerebellum_mean_dex-Cerebellum_mean_dex)/stds[9])
        calculated_cerebellum_mean_sin=slopes[8]*ålder+intersects[8]
        print("Cerebellum sin: z =", (calculated_cerebellum_mean_sin-Cerebellum_mean_sin)/stds[8])
    
        calculated_middle_mean_sin=slopes[11]*ålder+intersects[11]
        print("middle sin: z =", (calculated_middle_mean_sin-middle_mean_sin)/stds[11])
        calculated_middle_mean_sin=slopes[10]*ålder+intersects[10]
        print("middle sin: z =", (calculated_middle_mean_sin-middle_mean_sin)/stds[10])
    
        calculated_posterior_mean_dex=slopes[13]*ålder+intersects[13]
        print("posterior dex: z =", (calculated_posterior_mean_dex-posterior_mean_dex)/stds[13])
        calculated_posterior_mean_sin=slopes[12]*ålder+intersects[12]
        print("posterior sin: z =", (calculated_posterior_mean_sin-posterior_mean_sin)/stds[12])
    
        calculated_anterior_mean_dex=slopes[15]*ålder+intersects[15]
        print("anterior dex: z =", (calculated_anterior_mean_dex-anterior_mean_dex)/stds[15])
        calculated_anterior_mean_sin=slopes[14]*ålder+intersects[14]
        print("anterior sin: z =", (calculated_anterior_mean_sin-anterior_mean_sin)/stds[14])
        
    cerebellum_dex_all=np.load('cerebellum_dex_down_corrected.npy')    
    cerebellum_sin_all=np.load('cerebellum_sin_down_corrected.npy') 
    middle_dex_all=np.load('middle_dex_down_corrected.npy') 
    middle_sin_all=np.load('middle_sin_down_corrected.npy') 
    posterior_dex_all=np.load('posterior_dex_down_corrected.npy') 
    posterior_sin_all=np.load('posterior_sin_down_corrected.npy') 
    anterior_dex_all=np.load('anterior_dex_down_corrected.npy') 
    anterior_sin_all=np.load('anterior_sin_down_corrected.npy') 
    
    Z_brain=z_cerebellum_dex*cerebellum_dex_all+z_cerebellum_sin*cerebellum_sin_all\
        +z_anterior_dex*anterior_dex_all+z_anterior_sin*anterior_sin_all\
        +z_middle_dex*middle_dex_all+z_middle_sin*middle_sin_all\
        +z_posterior_dex*posterior_dex_all+z_posterior_sin*posterior_sin_all\
        +background
        
    return Z_brain

# transformed_K_1=np.load('ASPC0230-01-K_1.npy')
# ålder=56
# kön="M"

# Z_brain=SD_corrected(transformed_K_1, ålder, kön)
# plt.imshow(Z_brain[:,:,100], cmap='bwr', vmin=-5, vmax=5)