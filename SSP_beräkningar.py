# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 11:03:35 2024

@author: jacke
"""
import time
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
from numba import jit
import numpy as np

import matplotlib

plt.style.use('dark_background')
cdict = {'red': ((0.0, 0.0, 0.0),
                  (0.1, 0.5, 0.5),
                  (0.2, 0.0, 0.0),
                  (0.4, 0.2, 0.2),
                  (0.6, 0.0, 0.0),
                  (0.8, 1.0, 1.0),
                  (1.0, 1.0, 1.0)),
        'green':((0.0, 0.0, 0.0),
                  (0.1, 0.0, 0.0),
                  (0.2, 0.0, 0.0),
                  (0.4, 1.0, 1.0),
                  (0.6, 1.0, 1.0),
                  (0.8, 1.0, 1.0),
                  (1.0, 0.0, 0.0)),
        'blue': ((0.0, 0.0, 0.0),
                  (0.1, 0.5, 0.5),
                  (0.2, 1.0, 1.0),
                  (0.4, 1.0, 1.0),
                  (0.6, 0.0, 0.0),
                  (0.8, 0.0, 0.0),
                  (1.0, 0.0, 0.0))}

my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)

from matplotlib.colors import LinearSegmentedColormap
colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1 ,1 ,1), (1, 0, 0), (0.5, 0, 0)]  # R, G, B
n_bins = 10  # Number of bins in the colormap

# Create the colormap
cmap_name = 'custom_blue_white_red'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

def SSP(transformed_K_1):
    K_1_reshape_list_np=np.array(transformed_K_1)
    ssp_t=time.time()
    volume_brain=np.array(transformed_K_1)
    
    
    # volume_brain=territories_3d_inverted

    
    @jit(nopython=True)
    def trilinear_interpolate(volume, x, y, z):
        # Clip coordinates to ensure they are within the volume bounds
        x = min(max(x, 0), volume.shape[0] - 1)
        y = min(max(y, 0), volume.shape[1] - 1)
        z = min(max(z, 0), volume.shape[2] - 1)
        
        x0, y0, z0 = int(np.floor(x)), int(np.floor(y)), int(np.floor(z))
        x1, y1, z1 = x0 + 1, y0 + 1, z0 + 1
        
        # Ensure x1, y1, z1 do not exceed volume boundaries
        x1 = min(x1, volume.shape[0] - 1)
        y1 = min(y1, volume.shape[1] - 1)
        z1 = min(z1, volume.shape[2] - 1)
        
        # Calculate distances from point to grid points
        xd, yd, zd = x - x0, y - y0, z - z0
        
        # Compute interpolation
        c00 = volume[x0, y0, z0] * (1 - xd) + volume[x1, y0, z0] * xd
        c01 = volume[x0, y0, z1] * (1 - xd) + volume[x1, y0, z1] * xd
        c10 = volume[x0, y1, z0] * (1 - xd) + volume[x1, y1, z0] * xd
        c11 = volume[x0, y1, z1] * (1 - xd) + volume[x1, y1, z1] * xd
        
        c0 = c00 * (1 - yd) + c10 * yd
        c1 = c01 * (1 - yd) + c11 * yd
        c = c0 * (1 - zd) + c1 * zd
        
        return c
    
    def mean_along_vectors(volume, vectors_with_points, vector_length, num_steps):
        # print(volume.shape)
        volume_2 = np.empty((volume.shape[0], volume.shape[1], volume.shape[2]))
        
        for i, vector_info in enumerate(vectors_with_points):
            start_point = vector_info[:3]
            vector_direction = vector_info[3:6]
            
            # Normalize the vector direction
            direction_norm = np.linalg.norm(vector_direction)
            if direction_norm == 0:  # Skip zero vectors
                continue
            normalized_direction = vector_direction / direction_norm
            
            step_vector = normalized_direction * (vector_length / num_steps)
            sum_values = 0
            
            for step in range(num_steps + 1):
                point = start_point + step_vector * step
                interpolated_value = trilinear_interpolate(volume, *point)
                sum_values += interpolated_value
            
            mean_value = sum_values / (num_steps + 1)
            volume_2[int(start_point[0]), int(start_point[1]), int(start_point[2])] = mean_value
    
        return volume_2
    

    
    vector_length = 13  # Specify the desired length of the vector for mean calculation
    num_steps = 20
    
    points_and_normals_sin=np.load("points_and_normals_sin_corrected.npy")
    points_and_normals_dex=np.load("points_and_normals_dex_corrected.npy")
    
    for i in range(2):
        # image=image_list[i]
        # # print("1")
        # points_and_normals=norm_cal(image, i)
        if i==0:
            points_and_normals=points_and_normals_sin
        else:
            points_and_normals=points_and_normals_dex
        means = mean_along_vectors(volume_brain, points_and_normals, vector_length, num_steps)
        brain_shell=means
        # Assuming brain_shell is your 3D numpy array
        # Apply the Gaussian filter
        sigma = 0  # Standard deviation for Gaussian kernel, adjust as needed
        brain_shell_filtered = gaussian_filter(brain_shell, sigma=sigma)
        if i==0:
            x0=points_and_normals[:,0]
            y0=points_and_normals[:,1]
            z0=points_and_normals[:,2]
            mask = np.zeros_like(brain_shell_filtered, dtype=bool)
            for x, y, z in zip(x0, y0, z0):
                # print(x,y,z)
                mask[int(x), int(y), int(z)] = True  # Ensure indices are integers
            
            # Extract pixel values using the mask
            pixel_values0 = brain_shell_filtered[mask]
            # np.save('pixel_values0_s304_wat2.npy', pixel_values0)
            # print(pixel_values0.shape)
        
        if i==1:
            x1=points_and_normals[:,0]
            y1=points_and_normals[:,1]
            z1=points_and_normals[:,2]
            mask = np.zeros_like(brain_shell_filtered, dtype=bool)
            for x, y, z in zip(x1, y1, z1):
                # print(x,y,z)
                mask[int(x), int(y), int(z)] = True  # Ensure indices are integers
            
            # Extract pixel values using the mask
            pixel_values1 = brain_shell_filtered[mask]
            # np.save('pixel_values1_s304_wat2.npy', pixel_values1)
            # print(pixel_values1.shape)
            
    x2, y2, z2 = np.concatenate((x0,x1)), np.concatenate((y0,y1)), np.concatenate((z0,z1))
    pixel_values2=np.concatenate((pixel_values0,pixel_values1))
    
    # np.save('pixel_values2_s304_wat2.npy', pixel_values2)
    
    fig, axs = plt.subplots(1, 6, figsize=(26,5), subplot_kw={'projection': '3d'}) #(30,5) borde det vara (29,5) för att kolla om den blir lite bättre
    
    views_angles = [
        ([179, 180, "med"], 0),
        ([179, 0, "lat"], 1),
        ([179, 0, "med"], 2),
        ([179, 180, "lat"], 3),
        ([179, 90, "back"], 4),
        ([179, 270, "front"], 5),
    ]
    
    # Plotting
    from matplotlib.lines import Line2D
    
    for angles, idx in views_angles:
        elevation_angle, azimuth_angle, view = angles
        ax = axs[idx]
        
        if view in ["med", "lat"]:  
            x, y, z, pixel_values, pixel_values = (x0, y0, z0, pixel_values0, pixel_values0) if "med" in view else (x1, y1, z1, pixel_values1, pixel_values1)
        else:  
            x, y, z, pixel_values, pixel_values = x2, y2, z2, pixel_values2, pixel_values2
    
        point_size = 1
        # print(pixel_values2.shape)
        scatter = ax.scatter(x, y, z, c=pixel_values, s=point_size, cmap=my_cmap, vmin=0, vmax=1)
    
        label_text = ""
        if azimuth_angle == 180:
            if view == "med":
                label_text = "Dex (med)"
            else:
                label_text = "Sin (lat)"
        elif azimuth_angle == 0:
            if view == "lat":
                label_text = "Sin (med)"
            else:
                label_text = "Dex (lat)"
        else:
            label_text = view.capitalize()
    
        legend_line = Line2D([0], [0], linestyle='none', marker='none', color='none', label=label_text)
        
        # Reduce handle length to minimize the offset
        legend = ax.legend(handles=[legend_line], loc='upper center', frameon=False, handlelength=0)
    
        ax.view_init(elev=int(elevation_angle), azim=int(azimuth_angle))
        ax.axis("equal")
        ax.axis("off")
        
        # Colorbar setup (might need adjustment or omission based on visual clutter)
        # cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
        # cbar.set_label(f'Mean perfusion ({vector_length/10}cm) [min$^{-1}$]', rotation=270, labelpad=15)
    
    # Adjust layout to make plots closer
    plt.tight_layout()
    
    # Adjust the spacing between subplots
    plt.subplots_adjust(wspace=0)  # Adjust this value as needed to bring plots closer
    
    # cbar = fig.colorbar(scatter, ax=axs[-1], shrink=0.5, aspect=10)
    # cbar.set_label(f'Mean perfusion ({vector_length/10}cm) [min$^{-1}$]', rotation=270, labelpad=15)
    # plt.show()
    from matplotlib.colors import Normalize
    from matplotlib.cm import ScalarMappable
    norm = Normalize(vmin=0, vmax=np.max(pixel_values2))
    sm = ScalarMappable(norm=norm, cmap=my_cmap)
    
    # Add an axes at the end of the figure for the colorbar
    # The position is [left, bottom, width, height] in figure coordinates
    cbar_ax = fig.add_axes([0.91, 0.15, 0.01, 0.7])  # You might need to adjust these values
    cbar = fig.colorbar(sm, cax=cbar_ax, shrink=0.5, aspect=10)
    cbar.set_label(f'Mean perfusion ({vector_length/10}cm) [min$^{-1}$] bild 4', rotation=270, labelpad=15)
    
    plt.subplots_adjust(wspace=0.2, right=0.9)  # Adjust spacing and right margin to make room for colorbar
    # save4="4_"+Wx+".png"
    
    plt.show()
    print("SSP tid:", time.time()-ssp_t)
    
    SSP_mean_pixel_values0 = np.load('SSP_mean_wat1_value0.npy')
    SSP_mean_pixel_values1 = np.load('SSP_mean_wat1_value1.npy')
    SSP_mean_pixel_values2 = np.load('SSP_mean_wat1_value2.npy')
    
    SSP_SD_pixel_values0 = np.load('SSP_std_wat1_value0.npy')
    SSP_SD_pixel_values1 = np.load('SSP_std_wat1_value1.npy')
    SSP_SD_pixel_values2 = np.load('SSP_std_wat1_value2.npy')
    # print(pixel_values0[0])
    # print(SSP_mean_pixel_values0[0])
    fig, axs = plt.subplots(1, 6, figsize=(26,5), subplot_kw={'projection': '3d'}) #(30,5) borde det vara (29,5) för att kolla om den blir lite bättre
    
    views_angles = [
        ([179, 180, "med"], 0),
        ([179, 0, "lat"], 1),
        ([179, 0, "med"], 2),
        ([179, 180, "lat"], 3),
        ([179, 90, "back"], 4),
        ([179, 270, "front"], 5),
    ]
    
    # Plotting
    from matplotlib.lines import Line2D
    
    for angles, idx in views_angles:
        elevation_angle, azimuth_angle, view = angles
        ax = axs[idx]
        
        if view in ["med", "lat"]:  
            x, y, z, pixel_values, pixel_values = (x0, y0, z0, (pixel_values0-SSP_mean_pixel_values0)/SSP_SD_pixel_values0, (pixel_values0-SSP_mean_pixel_values0)/SSP_SD_pixel_values0) if "med" in view else (x1, y1, z1, (pixel_values1-SSP_mean_pixel_values1)/SSP_SD_pixel_values1, (pixel_values1-SSP_mean_pixel_values1)/SSP_SD_pixel_values1)
        else:  
            x, y, z, pixel_values, pixel_values = x2, y2, z2, (pixel_values2-SSP_mean_pixel_values2)/SSP_SD_pixel_values2, (pixel_values2-SSP_mean_pixel_values2)/SSP_SD_pixel_values2
    
        point_size = 1
        scatter = ax.scatter(x, y, z, c=pixel_values, s=point_size, cmap=custom_cmap, vmin=-5, vmax=5)
    
        label_text = ""
        if azimuth_angle == 180:
            if view == "med":
                label_text = "Dex (med)"
            else:
                label_text = "Sin (lat)"
        elif azimuth_angle == 0:
            if view == "lat":
                label_text = "Sin (med)"
            else:
                label_text = "Dex (lat)"
        else:
            label_text = view.capitalize()
    
        legend_line = Line2D([0], [0], linestyle='none', marker='none', color='none', label=label_text)
        
        # Reduce handle length to minimize the offset
        legend = ax.legend(handles=[legend_line], loc='upper center', frameon=False, handlelength=0)
    
        ax.view_init(elev=int(elevation_angle), azim=int(azimuth_angle))
        ax.axis("equal")
        ax.axis("off")
        
        # Colorbar setup (might need adjustment or omission based on visual clutter)
        # cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=10)
        # cbar.set_label(f'Mean perfusion ({vector_length/10}cm) [min$^{-1}$]', rotation=270, labelpad=15)
    
    # Adjust layout to make plots closer
    plt.tight_layout()
    
    # Adjust the spacing between subplots
    plt.subplots_adjust(wspace=0)  # Adjust this value as needed to bring plots closer
    
    # cbar = fig.colorbar(scatter, ax=axs[-1], shrink=0.5, aspect=10)
    # cbar.set_label(f'Mean perfusion ({vector_length/10}cm) [min$^{-1}$]', rotation=270, labelpad=15)
    # plt.show()
    from matplotlib.colors import Normalize
    from matplotlib.cm import ScalarMappable
    norm = Normalize(vmin=-5, vmax=5)
    sm = ScalarMappable(norm=norm, cmap=custom_cmap)
    
    # Add an axes at the end of the figure for the colorbar
    # The position is [left, bottom, width, height] in figure coordinates
    cbar_ax = fig.add_axes([0.91, 0.15, 0.01, 0.7])  # You might need to adjust these values
    cbar = fig.colorbar(sm, cax=cbar_ax, shrink=0.5, aspect=10, location="right")
    cbar.set_label('Standard deviation', rotation=270, labelpad=15)
    
    plt.subplots_adjust(wspace=0.2, right=0.9)  # Adjust spacing and right margin to make room for colorbar
    plt.show()
    print("total tid:", time.time()-ssp_t)
    
    return pixel_values0, pixel_values1, pixel_values2, (pixel_values0-SSP_mean_pixel_values0)/SSP_SD_pixel_values0, (pixel_values1-SSP_mean_pixel_values1)/SSP_SD_pixel_values1, (pixel_values2-SSP_mean_pixel_values2)/SSP_SD_pixel_values2

# transformed_K_1=np.load("transformed_K_1.npy")
# SSP(transformed_K_1)