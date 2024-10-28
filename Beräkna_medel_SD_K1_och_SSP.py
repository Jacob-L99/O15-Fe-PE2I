# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 11:54:45 2024

@author: jacke
"""

import zipfile
import numpy as np
import io
import matplotlib.pyplot as plt
from scipy import stats

def SD_K1():
    # Load and process the grey matter array
    grey = np.load('Register_grey_matter.npy')
    grey = np.flip(grey, axis=1)
    grey = np.flip(grey, axis=2)
    grey = np.where(grey > 0.5, 1, 0)  # Apply thresholding
    
    # grey=np.ones(np.shape(grey))
    
    # Load the region masks
    region_masks = {
        'cerebellum_dex': np.load('cerebellum_dex_down_corrected.npy'),
        'cerebellum_sin': np.load('cerebellum_sin_down_corrected.npy'),
        'middle_dex': np.load('middle_dex_down_corrected.npy'),
        'middle_sin': np.load('middle_sin_down_corrected.npy'),
        'posterior_dex': np.load('posterior_dex_down_corrected.npy'),
        'posterior_sin': np.load('posterior_sin_down_corrected.npy'),
        'anterior_dex': np.load('anterior_dex_down_corrected.npy'),
        'anterior_sin': np.load('anterior_sin_down_corrected.npy'),
    }
    
    # Add a key for the whole brain (no region mask, only grey matter mask)
    region_masks['whole_brain'] = np.ones_like(grey)  # No additional region mask
    
    # Replace 'your_zip_file.zip' with the actual file path of the zip file
    zip_file_path = 'K_1.zip'
    
    # Example metadata for the files (age and sex)
    metadata = {
        'ASPC0230-01-K_1.npy': {'age': 56, 'sex': 'male'},
        'ASPC0230-02-K_1.npy': {'age': 54, 'sex': 'female'},
        'ASPC0230-03-K_1.npy': {'age': 73, 'sex': 'male'},
        'ASPC0230-04-K_1.npy': {'age': 54, 'sex': 'female'},
        'ASPC0230-06-K_1.npy': {'age': 70, 'sex': 'male'},
        'ASPC0230-07-K_1.npy': {'age': 64, 'sex': 'male'},
        'ASPC0230-08-K_1.npy': {'age': 58, 'sex': 'female'},
        'ASPC0230-09-K_1.npy': {'age': 65, 'sex': 'female'},
        'ASPC0230-10-K_1.npy': {'age': 73, 'sex': 'female'},
        'ASPC0230-11-K_1.npy': {'age': 61, 'sex': 'male'},
        'ASPC0230-12-K_1.npy': {'age': 70, 'sex': 'female'},
        'ASPC0230-13-K_1.npy': {'age': 72, 'sex': 'male'},
        'ASPC0230-14-K_1.npy': {'age': 66, 'sex': 'female'},
        'ASPC0230-15-K_1.npy': {'age': 66, 'sex': 'male'},
        'Diamox-wat1-s304-K_1.npy': {'age': 44, 'sex': 'female'},
        'Diamox-wat1-s305-K_1.npy': {'age': 38, 'sex': 'female'},
        'Diamox-wat1-s308-K_1.npy': {'age': 29, 'sex': 'female'},
        'Diamox-wat1-s309-K_1.npy': {'age': 33, 'sex': 'male'},
        'Diamox-wat1-s310-K_1.npy': {'age': 53, 'sex': 'female'},
        'Diamox-wat1-s311-K_1.npy': {'age': 23, 'sex': 'male'},
        'Diamox-wat1-s312-K_1.npy': {'age': 46, 'sex': 'male'},
    }
    
    # Open the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        file_list = zip_ref.namelist()
    
        # Only include .npy files that are in metadata
        npy_files = [f for f in file_list if f.endswith('.npy') and ('ASPC' in f or 'Diamox-wat1' in f)]
    
        for region_name, region_mask in region_masks.items():
            # Multiply region mask by grey to get combined mask
            combined_mask = grey * region_mask
    
            combined_data_male = []
            combined_data_female = []
            ages_male = []
            ages_female = []
            missing_metadata = []
    
            for npy_file in npy_files:
                # Read the file into a bytes buffer
                with zip_ref.open(npy_file) as file:
                    npy_data = file.read()
                    array = np.load(io.BytesIO(npy_data))
    
                    # Flip and preprocess the array (if needed)
                    # array = np.flip(array, axis=1)
                    # array = np.flip(array, axis=2)
    
                    # Calculate the mean as the sum over the masked array divided by the sum of the mask
                    numerator = np.sum(array * combined_mask)
                    denominator = np.sum(combined_mask)
    
                    if denominator != 0:
                        mean_value = numerator / denominator
    
                        # Get metadata (age and sex)
                        file_metadata = metadata.get(npy_file)
    
                        if file_metadata:
                            age = file_metadata['age']
                            sex = file_metadata['sex']
                            if sex == 'male':
                                combined_data_male.append(mean_value)
                                ages_male.append(age)
                            elif sex == 'female':
                                combined_data_female.append(mean_value)
                                ages_female.append(age)
                        else:
                            # Track missing metadata entries
                            missing_metadata.append(npy_file)
                    else:
                        # If denominator is zero, skip this file
                        print(f"Warning: Denominator is zero for file {npy_file} in region {region_name}. Skipping.")
                        continue
    
            # Calculate and print mean and std for males and females
            if combined_data_male:
                mean_male = np.mean(combined_data_male)
                std_male = np.std(combined_data_male)
                print(f"{region_name} - Males: Mean = {mean_male:.4f}, Std = {std_male:.4f}")
    
            if combined_data_female:
                mean_female = np.mean(combined_data_female)
                std_female = np.std(combined_data_female)
                print(f"{region_name} - Females: Mean = {mean_female:.4f}, Std = {std_female:.4f}")
    
            # Create the scatter plot for the current region
            plt.figure(figsize=(10, 6))
            plt.title(f"Region: {region_name}")
    
            # Plot males in blue
            plt.scatter(ages_male, combined_data_male, color='blue', label='Males')
            # Plot females in orange
            plt.scatter(ages_female, combined_data_female, color='orange', label='Females')
    
            # Add linear fit for males
            if len(ages_male) > 1:
                slope_male, intercept_male, r_value, p_value, std_err = stats.linregress(ages_male, combined_data_male)
                fit_label_male = f'Male Fit: y = {slope_male:.4f}x + {intercept_male:.2f}'
                plt.plot(ages_male, np.array(ages_male) * slope_male + intercept_male, color='blue', linestyle='-', label=fit_label_male)
    
            # Add linear fit for females
            if len(ages_female) > 1:
                slope_female, intercept_female, r_value, p_value, std_err = stats.linregress(ages_female, combined_data_female)
                fit_label_female = f'Female Fit: y = {slope_female:.4f}x + {intercept_female:.2f}'
                plt.plot(ages_female, np.array(ages_female) * slope_female + intercept_female, color='orange', linestyle='-', label=fit_label_female)
    
            # Set fixed y-axis from 0.1 to 1
            plt.ylim(0.1, 1.5)
    
            # Labels and legend
            plt.xlabel('Ålder')
            plt.ylabel('Medel perfusion i grå substans [ml/cm³/g]')
            plt.legend()
            plt.show()
            print(f'{region_name}: {mean_female:.3f}, {std_female:.3f}, {slope_female:.4f}, {intercept_female:.2f}')
            # Print any missing metadata for this region
            if missing_metadata:
                print(f"Warning: The following files were missing metadata and were not included in the plot for {region_name}:")
                for file in missing_metadata:
                    print(file)
    return

SD_K1()
#%%
import zipfile
import numpy as np
from SSP_2d import SSP_2D  # Ensure SSP_2d.py is in your Python path or working directory

def SD_SSP():
    # Your provided metadata
    metadata = {
        'ASPC0230-01-K_1.npy': {'age': 56, 'sex': 'male'},
        'ASPC0230-02-K_1.npy': {'age': 54, 'sex': 'female'},
        'ASPC0230-03-K_1.npy': {'age': 73, 'sex': 'male'},
        'ASPC0230-04-K_1.npy': {'age': 54, 'sex': 'female'},
        'ASPC0230-06-K_1.npy': {'age': 70, 'sex': 'male'},
        'ASPC0230-07-K_1.npy': {'age': 64, 'sex': 'male'},
        'ASPC0230-08-K_1.npy': {'age': 58, 'sex': 'female'},
        'ASPC0230-09-K_1.npy': {'age': 65, 'sex': 'female'},
        'ASPC0230-10-K_1.npy': {'age': 73, 'sex': 'female'},
        'ASPC0230-11-K_1.npy': {'age': 61, 'sex': 'male'},
        'ASPC0230-12-K_1.npy': {'age': 70, 'sex': 'female'},
        'ASPC0230-13-K_1.npy': {'age': 72, 'sex': 'male'},
        'ASPC0230-14-K_1.npy': {'age': 66, 'sex': 'female'},
        'ASPC0230-15-K_1.npy': {'age': 66, 'sex': 'male'},
        'Diamox-wat1-s304-K_1.npy': {'age': 44, 'sex': 'female'},
        'Diamox-wat1-s305-K_1.npy': {'age': 38, 'sex': 'female'},
        'Diamox-wat1-s308-K_1.npy': {'age': 29, 'sex': 'female'},
        'Diamox-wat1-s309-K_1.npy': {'age': 33, 'sex': 'male'},
        'Diamox-wat1-s310-K_1.npy': {'age': 53, 'sex': 'female'},
        'Diamox-wat1-s311-K_1.npy': {'age': 23, 'sex': 'male'},
        'Diamox-wat1-s312-K_1.npy': {'age': 46, 'sex': 'male'},
    }
    
    # Function to load .npy files from zip and associate with metadata
    def load_data_from_zip(zip_path, metadata):
        data_dict = {}
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Filter for .npy files
            npy_files = [f for f in zip_ref.namelist() if f.endswith('.npy')]
            
            for file_name in npy_files:
                if file_name in metadata:
                    # Read the file into a BytesIO object
                    with zip_ref.open(file_name) as file:
                        data_array = np.load(file)
                        data_dict[file_name] = {
                            'data': data_array,
                            'metadata': metadata[file_name]
                        }
                else:
                    print(f"Metadata for {file_name} not found.")
        return data_dict
    
    # Usage
    zip_file_path = 'K_1.zip'  # Ensure this is the correct path to your zip file
    data = load_data_from_zip(zip_file_path, metadata)
    
    # Initialize lists to store the outputs from SSP_2D
    first_values_yz_neg_x0_list = []
    first_values_yz_pos_x1_list = []
    first_values_yz_pos_x2_list = []
    first_values_yz_neg_x2_list = []
    first_values_xz_pos_y2_list = []
    first_values_xz_neg_y2_list = []
    
    # Now, apply SSP_2D to each data array and collect the results
    for file_name, content in data.items():
        transformed_K_1 = content['data']
        # Apply SSP_2D function
        try:
            first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, \
            first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2 = SSP_2D(transformed_K_1)
            
            # Append each result to the corresponding list
            first_values_yz_neg_x0_list.append(first_values_yz_neg_x0)
            first_values_yz_pos_x1_list.append(first_values_yz_pos_x1)
            first_values_yz_pos_x2_list.append(first_values_yz_pos_x2)
            first_values_yz_neg_x2_list.append(first_values_yz_neg_x2)
            first_values_xz_pos_y2_list.append(first_values_xz_pos_y2)
            first_values_xz_neg_y2_list.append(first_values_xz_neg_y2)
            
            print(f"Processed {file_name} successfully.")
        except Exception as e:
            print(f"Error processing {file_name}: {e}")
    
    # Convert lists to NumPy arrays and stack them into 3D arrays
    def stack_and_prepare(array_list):
        # Stack the arrays along a new axis (axis=0)
        stacked_array = np.stack(array_list, axis=0)
        # Replace zeros with np.nan to exclude them from calculations
        stacked_array[stacked_array == 0] = np.nan
        return stacked_array
    
    first_values_yz_neg_x0_stack = stack_and_prepare(first_values_yz_neg_x0_list)
    first_values_yz_pos_x1_stack = stack_and_prepare(first_values_yz_pos_x1_list)
    first_values_yz_pos_x2_stack = stack_and_prepare(first_values_yz_pos_x2_list)
    first_values_yz_neg_x2_stack = stack_and_prepare(first_values_yz_neg_x2_list)
    first_values_xz_pos_y2_stack = stack_and_prepare(first_values_xz_pos_y2_list)
    first_values_xz_neg_y2_stack = stack_and_prepare(first_values_xz_neg_y2_list)
    
    # Compute the per-pixel mean and STD, ignoring np.nan values
    mean_first_values_yz_neg_x0 = np.nanmean(first_values_yz_neg_x0_stack, axis=0)
    std_first_values_yz_neg_x0 = np.nanstd(first_values_yz_neg_x0_stack, axis=0)
    
    mean_first_values_yz_pos_x1 = np.nanmean(first_values_yz_pos_x1_stack, axis=0)
    std_first_values_yz_pos_x1 = np.nanstd(first_values_yz_pos_x1_stack, axis=0)
    
    mean_first_values_yz_pos_x2 = np.nanmean(first_values_yz_pos_x2_stack, axis=0)
    std_first_values_yz_pos_x2 = np.nanstd(first_values_yz_pos_x2_stack, axis=0)
    
    mean_first_values_yz_neg_x2 = np.nanmean(first_values_yz_neg_x2_stack, axis=0)
    std_first_values_yz_neg_x2 = np.nanstd(first_values_yz_neg_x2_stack, axis=0)
    
    mean_first_values_xz_pos_y2 = np.nanmean(first_values_xz_pos_y2_stack, axis=0)
    std_first_values_xz_pos_y2 = np.nanstd(first_values_xz_pos_y2_stack, axis=0)
    
    mean_first_values_xz_neg_y2 = np.nanmean(first_values_xz_neg_y2_stack, axis=0)
    std_first_values_xz_neg_y2 = np.nanstd(first_values_xz_neg_y2_stack, axis=0)
    
    # Collect all mean and STD arrays into a single structure
    somthing = [
        [mean_first_values_yz_neg_x0, std_first_values_yz_neg_x0],
        [mean_first_values_yz_pos_x1, std_first_values_yz_pos_x1],
        [mean_first_values_yz_pos_x2, std_first_values_yz_pos_x2],
        [mean_first_values_yz_neg_x2, std_first_values_yz_neg_x2],
        [mean_first_values_xz_pos_y2, std_first_values_xz_pos_y2],
        [mean_first_values_xz_neg_y2, std_first_values_xz_neg_y2]
    ]
    #%%
    
    plt.imshow(somthing[0][0])
    import zipfile
    import numpy as np
    import pickle  # Import pickle module
    from SSP_2d import SSP_2D  # Ensure SSP_2d.py is in your Python path or working directory
    
    # [The rest of your code remains the same up to where you construct 'somthing']
    
    # Collect all mean and STD arrays into a single structure
    somthing = [
        [mean_first_values_yz_neg_x0, std_first_values_yz_neg_x0],
        [mean_first_values_yz_pos_x1, std_first_values_yz_pos_x1],
        [mean_first_values_yz_pos_x2, std_first_values_yz_pos_x2],
        [mean_first_values_yz_neg_x2, std_first_values_yz_neg_x2],
        [mean_first_values_xz_pos_y2, std_first_values_xz_pos_y2],
        [mean_first_values_xz_neg_y2, std_first_values_xz_neg_y2]
    ]
    
    # Save 'somthing' using pickle
    with open('SSP_results.pkl', 'wb') as f:
        pickle.dump(somthing, f)
    
    print("Mean and STD arrays have been saved to 'SSP_results.pkl'.")
    return


#%%
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Load the data
with open('SSP_results.pkl', 'rb') as f:
    somthing = pickle.load(f)

# Access mean and STD arrays
mean_first_values_yz_neg_x0 = somthing[0][0]
std_first_values_yz_neg_x0 = somthing[0][1]

mean_first_values_yz_pos_x1 = somthing[1][0]
std_first_values_yz_pos_x1 = somthing[1][1]

# And so on for the other arrays
plt.imshow(np.rot90(np.rot90(np.rot90(mean_first_values_yz_neg_x0))))
plt.show()

transformed_K_1=np.load('ASPC0230-01-K_1.npy')
from SSP_2d import SSP_2D
first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2=SSP_2D(transformed_K_1)

from matplotlib.colors import LinearSegmentedColormap
colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1 ,1 ,1), (1, 0, 0), (0.5, 0, 0)]  # R, G, B
n_bins = 10  # Number of bins in the colormap

# Create the colormap
cmap_name = 'custom_blue_white_red'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

plt.imshow(np.rot90(np.rot90(np.rot90((first_values_yz_neg_x0-mean_first_values_yz_neg_x0)/std_first_values_yz_neg_x0))), cmap=custom_cmap, vmin=-5, vmax=5)
plt.colorbar()
plt.show()


