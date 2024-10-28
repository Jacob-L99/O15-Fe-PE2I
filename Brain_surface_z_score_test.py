import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import SimpleITK as sitk
import matplotlib

plt.style.use('dark_background')

def fig_get():
    def apply_colormap(image_np, cmap='bwr'):
        """
        Apply a colormap to a 2D numpy image.
        Args:
            image_np: The numpy array of the image.
            cmap: The colormap to apply.
        Returns:
            Colormapped image as a numpy array.
        """
        # Normalize the image to [0, 1] range
        normalized_img = (image_np - image_np.min()) / (image_np.max() - image_np.min())
        
        # Apply the colormap
        colormap = plt.cm.get_cmap(cmap)
        colored_img = colormap(normalized_img)  # This returns an RGBA image
        
        # Convert RGBA to RGB (drop the alpha channel)
        return colored_img[:, :, :3]
    
    def blend_images(fixed_image_np, transformed_image_colored_np, alpha=0.5):
        """
        Alpha blend the fixed grayscale image and the colored registered image.
        Args:
            fixed_image_np: The numpy array of the fixed (template) grayscale image.
            transformed_image_colored_np: The numpy array of the colored registered image (RGB format).
            alpha: The blending factor for the fixed image. The transformed image is always shown at full intensity.
        Returns:
            A blended numpy array of the two images.
        """
        # Normalize the fixed grayscale image to [0, 1]
        fixed_image_norm = (fixed_image_np - fixed_image_np.min()) / (fixed_image_np.max() - fixed_image_np.min())
    
        # Convert the fixed image to RGB format by stacking it
        fixed_image_rgb = np.stack([fixed_image_norm]*3, axis=-1)
    
        # Blend the images using the formula: blended = alpha * fixed + (1 - alpha) * transformed
        blended_image = alpha * fixed_image_rgb + (1 - alpha) * transformed_image_colored_np
        
        # Clip the values to the [0, 1] range to avoid overflow
        blended_image = np.clip(blended_image, 0, 1)
        
        return blended_image
    
    # Load images (assuming these are 3D medical images, like NIfTI)
    transformed_K_1 = np.load('ASPC0230-01-K_1.npy')
    from SSP_2d import SSP_2D
    first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2 = SSP_2D(transformed_K_1)
    
    from Z_score_SSP import SSP_Z
    neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2 = SSP_Z(first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2)
    
    project90 = np.load('projection_270.npy')
    
    background=np.load('background_down_corrected.npy')
    
    def mr_angel(project90, pos_x2):
        target_shape = np.rot90(np.rot90(np.rot90(pos_x2))).shape
        
        # Get the current shape of projection90
        current_shape = project90.shape
        
        # Calculate the padding required for each dimension
        padding = []
        for dim, (current, target) in enumerate(zip(current_shape, target_shape)):
            if dim == 0:  # For the first dimension (rows), pad only at the top
                total_pad = max(target - current, 0)
                pad_before = total_pad  # All padding at the top
                pad_after = 0
            else:  # For the second dimension (columns), pad symmetrically
                total_pad = max(target - current, 0)
                pad_before = total_pad // 2
                pad_after = total_pad - pad_before
            padding.append((pad_before, pad_after))
        
        # Pad the projection90 array with zeros to match the target shape
        projection90_padded = np.pad(project90, padding, mode='constant', constant_values=0)
        projection90_padded = np.flip(projection90_padded, axis=1)
        
        # Remove 20 layers from the bottom and add them to the top of the fixed_slice
        fixed_slice = projection90_padded
        # if fixed_slice.shape[0] > 9:
        #     fixed_slice = np.vstack((fixed_slice[-9:], fixed_slice[:-9]))
        return fixed_slice
    
    #%%
    
    
    plt.style.use('dark_background')
    colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1, 1, 1), (1, 0, 0), (0.5, 0, 0)]  # R, G, B
    n_bins = 10  # Number of bins in the colormap
    cmap_name = 'custom_blue_white_red'
    custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)
    
    def temp_name(pet_image, fixed_slice):
        # Create the colormap
        
        
        # Existing code
        alpha_value = 0.6  # Fixed alpha value
        transformed_slice = pet_image
        transformed_slice = np.nan_to_num(transformed_slice, nan=0)
        
        # Clip and normalize the transformed slice to the range [-5, 5]
        transformed_slice_clipped = np.clip(transformed_slice, -5, 5)
        normalized_transformed_slice = (transformed_slice_clipped + 5) / 10  # Normalizes to [0, 1] range for the colormap
        
        # Apply colormap to the normalized transformed image
        transformed_colored = custom_cmap(normalized_transformed_slice)  # Apply custom colormap
        # transformed_colored is an RGBA array (height, width, 4)
        
        # Create a mask for values between -1 and 1 and set alpha to 0 for those pixels
        alpha_channel = transformed_colored[:, :, 3]  # Extract the alpha channel
        
        # Create a mask where the original values are between -1 and 1
        transparent_mask = (transformed_slice_clipped >= -1) & (transformed_slice_clipped <= 1)
        
        # Set alpha to 0 for values within the range [-1, 1]
        alpha_channel[transparent_mask] = 0  # Fully transparent
        # Set alpha to 1 for values outside the range [-1, 1]
        alpha_channel[~transparent_mask] = 1  # Fully opaque
        
        # Update the alpha channel in transformed_colored
        transformed_colored[:, :, 3] = alpha_channel
        
        # Plot the transformed image with transparency applied
        plt.imshow(transformed_colored)
        plt.axis('off')
        
        # Add a colorbar for the transformed_colored plot with fixed limits
        sm = plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=-5, vmax=5))
        cbar = plt.colorbar(sm, ax=plt.gca(), fraction=0.03, pad=0.04)
        cbar.set_label('Color Scale')
        cbar.set_ticks(np.arange(-5, 6, 1))  # Set colorbar range from -5 to 5 in steps of 1
        
        plt.show()
        
        # Generate the mask and expand dimensions
        mask_1 = np.where(transformed_slice != 0, 1, np.nan)
        mask_1_expanded = mask_1[:, :, np.newaxis]  # Shape becomes (128, 158, 1)
        
        # Blend images
        blended_image_np = blend_images(fixed_slice, transformed_colored[:, :, :3], alpha_value)
        blended_image_np = np.where(blended_image_np == 0, np.nan, blended_image_np) * mask_1_expanded
        
        # Plotting the blended image with fixed color limits
        fig_blended, ax_blended = plt.subplots(figsize=(8, 8), dpi=50)  # Increased size and set DPI
        ax_blended.axis('off')  # Turn off axes
        im = ax_blended.imshow(blended_image_np)
        
        # Add a colorbar for the blended image with fixed limits
        cbar_blended = fig_blended.colorbar(sm, ax=ax_blended, fraction=0.03, pad=0.04)
        cbar_blended.set_label('Color Scale')
        cbar_blended.set_ticks(np.arange(-5, 6, 1))  # Set colorbar range from -5 to 5 in steps of 1
        
        plt.show()
        
        # New Plot: MR image as base, color regions for parametric PET values between [-5, -1] and [1, 5]
        fig, ax = plt.subplots(figsize=(8, 8), dpi=50)
        
        # Plot the MR image in grayscale
        ax.imshow(fixed_slice, cmap='gray')
        
        # Create a mask for the PET values between [-5, -1] and [1, 5]
        highlight_mask = ((transformed_slice_clipped >= -5) & (transformed_slice_clipped <= -1)) | \
                         ((transformed_slice_clipped >= 1) & (transformed_slice_clipped <= 5))
        
        # Apply the colormap only to the regions within the highlight_mask
        highlighted_region = np.zeros_like(transformed_colored) * mask_1_expanded
        highlighted_region[highlight_mask] = transformed_colored[highlight_mask]
        
        # Plot the highlighted regions on top of the MR image
        ax.imshow(highlighted_region)
        ax.axis('off')
        
        # Add a colorbar for the highlighted regions with fixed limits
        cbar_highlight = fig.colorbar(sm, ax=ax, fraction=0.03, pad=0.04)
        cbar_highlight.set_label('Color Scale')
        cbar_highlight.set_ticks(np.arange(-5, 6, 1))
        
        plt.show()
        
        # Return the last figure
        return fig
    
    project_dex_medial = np.load('projection_90.npy')
    fixed_slice_dex_medial = mr_angel(project_dex_medial, neg_x2)
    
    last_figure_4 = temp_name(np.rot90(np.rot90(np.rot90(neg_x2))), fixed_slice_dex_medial)
    
    # Now, you can use loaded_figure as you would use last_figure_4
    
    
    # print(type(last_figure))
    # plt.imshow(np.rot90(np.rot90(np.rot90(neg_x2))))
    # plt.axis('off')
    # plt.colorbar()
    # plt.show()
    
    project_sin_medial = np.load('projection_270.npy')
    fixed_slice_sin_medial=mr_angel(project_sin_medial, pos_x2)
    
    last_figure_3 = temp_name(np.flip(np.rot90(np.rot90(np.rot90(pos_x2))),axis=1), fixed_slice_sin_medial)
    
    # plt.imshow(np.flip(np.rot90(np.rot90(np.rot90(pos_x2))),axis=1))
    # plt.axis('off')
    # plt.colorbar()
    # plt.show()
    
    project_dex = np.load('projection_0.npy')
    fixed_slice_dex=mr_angel(project_dex, neg_y2)
    
    last_figure_6 = temp_name(np.rot90(np.rot90(np.rot90(neg_y2))), fixed_slice_dex)
    # plt.imshow(np.rot90(np.rot90(np.rot90(neg_y2))))
    # plt.axis('off')
    # plt.colorbar()
    # plt.show()
    
    project_sin = np.load('projection_180.npy')
    fixed_slice_sin=mr_angel(project_sin, pos_y2)
    
    last_figure_5 = temp_name(np.rot90(np.rot90(np.rot90(pos_y2))), fixed_slice_sin)
    # plt.imshow(np.rot90(np.rot90(np.rot90(pos_y2))))
    # plt.axis('off')
    # plt.colorbar()
    # plt.show()
    
    project_back = np.load('projection_inside_sin.npy')
    fixed_slice_back=mr_angel(project_back, neg_x0)
    
    last_figure_1 = temp_name(np.rot90(np.rot90(np.rot90(neg_x0))), fixed_slice_back)
    # plt.imshow(np.rot90(np.rot90(np.rot90(neg_x0))))
    # plt.axis('off')
    # plt.colorbar()
    # plt.show()
    
    project_front = np.load('projection_inside_dex.npy')
    fixed_slice_front=mr_angel(project_front, pos_x1)
    
    last_figure_2 = temp_name(np.flip(np.rot90(np.rot90(np.rot90(pos_x1))), axis=1), fixed_slice_front)
    # plt.imshow(np.flip(np.rot90(np.rot90(np.rot90(pos_x1))), axis=1))
    # plt.axis('off')
    # plt.colorbar()
    # plt.show()
    return last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6
# #%%
# last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6 = fig_get()
# all_figures = [last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6]

# # Create a new figure with 1 row and 6 columns to combine all six figures
# fig, axs = plt.subplots(1, 6, figsize=(28, 10))  # Create a 1-row, 6-column layout with larger width for more padding

# # Loop over all the figures and plot them in subplots (the first 6 columns)
# for i, figure in enumerate(all_figures):
#     ax_new = axs[i]
#     for ax_old in figure.axes:
#         # Extract the image data from each figure (assuming it's an imshow-based plot)
#         for img in ax_old.images:
#             blended_image = img.get_array()  # Get the blended image array from the original figure
#             im = ax_new.imshow(blended_image, cmap=img.get_cmap(), alpha=img.get_alpha())  # Reuse the original colormap and alpha settings
        
#         # Set titles and turn off axes for a cleaner look
#         if i == 0:
#             ax_new.set_title('Dex medial', fontsize=16)
#         elif i == 1:
#             ax_new.set_title('Sin medial', fontsize=16)
#         elif i == 2:
#             ax_new.set_title('Dex', fontsize=16)
#         elif i == 3:
#             ax_new.set_title('Sin', fontsize=16)
#         elif i == 4:
#             ax_new.set_title('Back', fontsize=16)
#         elif i == 5:
#             ax_new.set_title('Front', fontsize=16)
#         ax_new.axis('off')

# # Define the custom colormap for the shared colorbar
# colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1, 1, 1), (1, 0, 0), (0.5, 0, 0)]  # RGB values
# n_bins = 10  # Number of bins in the colormap
# cmap_name = 'custom_blue_white_red'
# custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# # Add one shared colorbar for all subplots
# cbar_ax = fig.add_axes([1, 0.15, 0.02, 0.63])  # [left, bottom, width, height] - more padding for colorbar
# sm = plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=-5, vmax=5))
# cbar = fig.colorbar(sm, cax=cbar_ax, label='Z-score')  # Add colorbar to the specified axis
# cbar.ax.tick_params(labelsize=14)  # Increase the size of colorbar tick labels
# cbar.set_label('Z-score', fontsize=20)  # Set the label for the colorbar with increased fontsize


# # Adjust layout and show the combined figure with all six blended images and the shared colorbar
# plt.tight_layout()
# plt.show()