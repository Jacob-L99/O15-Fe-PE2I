# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:11:31 2024

@author: jacke
"""
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import os

# Define the path to your zip file
zip_file_path = 'BP, R_I.zip'

# Create a temporary directory to extract the npy files
temp_dir = 'temp_npy_files'
os.makedirs(temp_dir, exist_ok=True)

# Extract all .npy files from the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)

# Initialize variables to store the sum of arrays and the count of non-zero elements
sum_array = None
count_array = None

# Loop through each .npy file in the extracted folder
for file_name in os.listdir(temp_dir):
    if file_name.endswith('.npy') and file_name.startswith('FE-PE2I-') and '-BP' not in file_name:
        # Load the 3D array
        file_path = os.path.join(temp_dir, file_name)
        array = np.load(file_path)

        # Initialize sum_array and count_array if they are None
        if sum_array is None:
            sum_array = np.zeros_like(array, dtype=np.float64)
            count_array = np.zeros_like(array, dtype=np.int32)

        # Create a mask for non-zero elements
        mask = array != 0

        # Add the values where the mask is True
        sum_array[mask] += array[mask]

        # Update the count of non-zero elements
        count_array[mask] += 1

# Avoid division by zero by using np.where
mean_array = np.where(count_array > 0, sum_array / count_array, 0)

# Calculate standard deviation
squared_diff_sum = np.zeros_like(sum_array)

for file_name in os.listdir(temp_dir):
    if file_name.endswith('.npy') and file_name.startswith('FE-PE2I-') and '-BP' not in file_name:
        # Load the 3D array
        file_path = os.path.join(temp_dir, file_name)
        array = np.load(file_path)

        # Create a mask for non-zero elements
        mask = array != 0

        # Calculate the squared difference and add to the sum
        squared_diff_sum[mask] += ((array[mask] - mean_array[mask]) ** 2)

# Calculate the standard deviation
std_array = np.where(count_array > 0, np.sqrt(squared_diff_sum / count_array), 0)

output_file_path = 'R_I_mean_and_std.npy'
np.save(output_file_path, [mean_array, std_array])



# Cleanup: remove the temporary directory and its contents
import shutil
shutil.rmtree(temp_dir)

# mean_array and std_array now contain the mean and standard deviation, respectively
print("Mean array calculated.")
print("Standard deviation array calculated.")

print(np.shape(mean_array))

from parkinson_plot import plot_specific_slices
plot_specific_slices(mean_array, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=2.5, title="R_I mean")
plot_specific_slices(std_array, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=1, title="R_I STD")

#%%
import numpy as np
import zipfile
import os

# Define the path to your zip file
zip_file_path = 'BP, R_I.zip'

# Create a temporary directory to extract the npy files
temp_dir = 'temp_npy_files'
os.makedirs(temp_dir, exist_ok=True)

# Extract all .npy files from the zip file
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(temp_dir)

# Initialize variables to store the sum of arrays and the count of non-zero elements
sum_array = None
count_array = None

# Loop through each .npy file in the extracted folder
for file_name in os.listdir(temp_dir):
    if file_name.endswith('.npy') and file_name.startswith('FE-PE2I-') and '-BP' in file_name:
        # Load the 3D array
        file_path = os.path.join(temp_dir, file_name)
        array = np.load(file_path)

        # Initialize sum_array and count_array if they are None
        if sum_array is None:
            sum_array = np.zeros_like(array, dtype=np.float64)
            count_array = np.zeros_like(array, dtype=np.int32)

        # Create a mask for non-zero elements
        mask = array != 0

        # Add the values where the mask is True
        sum_array[mask] += array[mask]

        # Update the count of non-zero elements
        count_array[mask] += 1

# Avoid division by zero by using np.where
mean_array = np.where(count_array > 0, sum_array / count_array, 0)

# Calculate standard deviation
squared_diff_sum = np.zeros_like(sum_array)

for file_name in os.listdir(temp_dir):
    if file_name.endswith('.npy') and file_name.startswith('FE-PE2I-') and '-BP' in file_name:
        # Load the 3D array
        file_path = os.path.join(temp_dir, file_name)
        array = np.load(file_path)

        # Create a mask for non-zero elements
        mask = array != 0

        # Calculate the squared difference and add to the sum
        squared_diff_sum[mask] += ((array[mask] - mean_array[mask]) ** 2)

# Calculate the standard deviation
std_array = np.where(count_array > 0, np.sqrt(squared_diff_sum / count_array), 0)

# Save the mean and standard deviation arrays in a single .npy file
output_file_path = 'BP_mean_and_std.npy'
np.save(output_file_path, [mean_array, std_array])

# Cleanup: remove the temporary directory and its contents
import shutil
shutil.rmtree(temp_dir)

# mean_array and std_array now contain the mean and standard deviation, respectively
print("Mean array calculated.")
print("Standard deviation array calculated.")
print(f"Arrays saved to {output_file_path}.")

from parkinson_plot import plot_specific_slices
plot_specific_slices(mean_array, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=7.5, title="BP mean")
plot_specific_slices(std_array, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=2, title="BP STD")
