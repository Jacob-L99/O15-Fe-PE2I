# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:12:40 2024

@author: jacke
"""
import pickle
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.colors import LinearSegmentedColormap
colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1 ,1 ,1), (1, 0, 0), (0.5, 0, 0)]  # R, G, B
n_bins = 10  # Number of bins in the colormap

# Create the colormap
cmap_name = 'custom_blue_white_red'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)


def SSP_Z(first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2):
    # Load the data
    with open('SSP_results.pkl', 'rb') as f:
        somthing = pickle.load(f)
    
    
    mean_first_values_yz_neg_x0, std_first_values_yz_neg_x0=somthing[0][0], somthing[0][1]
    mean_first_values_yz_pos_x1, std_first_values_yz_pos_x1=somthing[1][0], somthing[1][1]
    mean_first_values_yz_pos_x2, std_first_values_yz_pos_x2=somthing[2][0], somthing[2][1]
    mean_first_values_yz_neg_x2, std_first_values_yz_neg_x2=somthing[3][0], somthing[3][1]
    mean_first_values_xz_pos_y2, std_first_values_xz_pos_y2=somthing[4][0], somthing[4][1]
    mean_first_values_xz_neg_y2, std_first_values_xz_neg_y2=somthing[5][0], somthing[5][1]
    
    neg_x0=(first_values_yz_neg_x0-mean_first_values_yz_neg_x0)/std_first_values_yz_neg_x0
    pos_x1=(first_values_yz_pos_x1-mean_first_values_yz_pos_x1)/std_first_values_yz_pos_x1
    pos_x2=(first_values_yz_pos_x2-mean_first_values_yz_pos_x2)/std_first_values_yz_pos_x2
    neg_x2=(first_values_yz_neg_x2-mean_first_values_yz_neg_x2)/std_first_values_yz_neg_x2
    pos_y2=(first_values_xz_pos_y2-mean_first_values_xz_pos_y2)/std_first_values_xz_pos_y2
    neg_y2=(first_values_xz_neg_y2-mean_first_values_xz_neg_y2)/std_first_values_xz_neg_y2
    
    def plot_first_values(vmin=None, vmax=None):
        fig, axes = plt.subplots(1, 6, figsize=(20, 6))
        
        # Plot for the first non-NaN value along positive x-axis
        im1 = axes[0].imshow(np.rot90(np.rot90(np.rot90(neg_x0))), interpolation='nearest', cmap=custom_cmap, vmin=vmin, vmax=vmax)
        axes[0].set_title('Dex inside')
        axes[0].axis('off')  # Remove axis
    
        # Plot for the first non-NaN value along negative x-axis
        im2 = axes[1].imshow(np.flip(np.rot90(np.rot90(np.rot90(pos_x1))), axis=1), interpolation='nearest', cmap=custom_cmap, vmin=vmin, vmax=vmax)
        axes[1].set_title('Sin inside)')
        axes[1].axis('off')  # Remove axis
    
        # Plot for the first non-NaN value along positive y-axis
        im3 = axes[2].imshow(np.flip(np.rot90(np.rot90(np.rot90(pos_x2))), axis=1), interpolation='nearest', cmap=custom_cmap, vmin=vmin, vmax=vmax)
        axes[2].set_title('Dex')
        axes[2].axis('off')  # Remove axis
    
        # Plot for the first non-NaN value along negative y-axis
        im4 = axes[3].imshow(np.rot90(np.rot90(np.rot90(neg_x2))), interpolation='nearest', cmap=custom_cmap, vmin=vmin, vmax=vmax)
        axes[3].set_title('Sin')
        axes[3].axis('off')  # Remove axis
    
        # Plot for the first non-NaN value along positive y-axis
        im5 = axes[4].imshow(np.rot90(np.rot90(np.rot90(pos_y2))), interpolation='nearest', cmap=custom_cmap, vmin=vmin, vmax=vmax)
        axes[4].set_title('Back')
        axes[4].axis('off')  # Remove axis
    
        # Plot for the first non-NaN value along negative y-axis
        im6 = axes[5].imshow(np.rot90(np.rot90(np.rot90(neg_y2))), interpolation='nearest', cmap=custom_cmap, vmin=vmin, vmax=vmax)
        axes[5].set_title('Front')
        axes[5].axis('off')  # Remove axis
    
        # Add one shared colorbar for all subplots
        fig.subplots_adjust(right=0.85)  # Adjust to leave space for colorbar
        cbar_ax = fig.add_axes([1, 0.15, 0.02, 0.7])  # [left, bottom, width, height]
        fig.colorbar(im1, cax=cbar_ax, label='ml/cm3/min')
    
        plt.tight_layout()
        plt.show()
    
    # Example usage:
    plot_first_values(vmin=-5, vmax=5)
    plt.imshow(pos_x2)
    return neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2