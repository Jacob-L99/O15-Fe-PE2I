import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

def läs_in_nifty_temp():
    # Load the NIfTI file
    nifti_file = 'sub-102621_ses-rescan_pet.nii.gz'
    nifti_data = nib.load(nifti_file)
    
    # Get the image data as a NumPy array (4D)
    image_data = nifti_data.get_fdata()
    
    # Get the shape of the image data
    image_shape = image_data.shape
    
    # Time points (in minutes)
    time = np.array([0, 15.0, 45.0, 75.0, 105.0, 135.0, 165.0, 210.0, 270.0, 330.0, 420.0, 
                     540.0, 750.0, 1050.0, 1350.0, 1650.0, 1950.0, 2250.0, 2550.0, 
                     2850.0, 3150.0, 3450.0, 3750.0, 4050.0, 4350.0, 4650.0, 4950.0]) / 60
    # print(image_shape[:2])

    # Return image data, its shape, and time points
    return image_data, image_shape[:2], time

image_data, image_shape, time= läs_in_nifty_temp()
#%%
