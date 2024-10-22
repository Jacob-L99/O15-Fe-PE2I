# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 10:04:20 2024

@author: jacke
"""
import ants
import numpy as np
import time

def rörelse_korrektion(data_4d):
    def motion_correct_4d_array(data, reference_time_point=10):
        """
        Perform motion correction on a 4D numpy array (x, y, z, time)
        to align each 3D volume to the volume at the specified time point.
        
        Parameters:
        - data: A 4D numpy array of shape (x, y, z, time).
        - reference_time_point: The time point of the reference volume.
        
        Returns:
        - A 4D numpy array with motion-corrected volumes.
        """
        # Ensure the reference time point is within the bounds of the data's time dimension
        if reference_time_point < 0 or reference_time_point >= data.shape[3]:
            raise ValueError("Reference time point is out of bounds.")
        
        # Convert the reference volume to an ANTs image
        reference_volume = ants.from_numpy(data[..., reference_time_point])
        
        # Initialize the array to hold the motion-corrected volumes
        corrected_data = np.zeros_like(data)
        
        # Process each time point
        for t in range(data.shape[3]):
            # print(t)
            # Skip the reference volume since it doesn't need registration
            if t == reference_time_point:
                corrected_data[..., t] = data[..., t]
                continue
            #skippar första volymen för den kan vara noll
            if t == 0:
                corrected_data[..., t] = data[..., t]
                continue
            
            # Convert the current volume to an ANTs image
            moving_volume = ants.from_numpy(data[..., t])
            
            # Perform registration (align the moving volume to the reference volume)
            registration = ants.registration(fixed=reference_volume, moving=moving_volume, type_of_transform='QuickRigid')
            
            # Apply the transformation to the moving volume and convert back to numpy array
            corrected_volume = ants.apply_transforms(fixed=reference_volume, moving=moving_volume, transformlist=registration['fwdtransforms'], interpolator='linear')
            
            # Store the corrected volume
            corrected_data[..., t] = corrected_volume.numpy()
        
        return corrected_data
    
    # Example usage:
    # Assuming `data` is your 4D numpy array with shape (x, y, z, time)
    start=time.time()
    corrected_data = motion_correct_4d_array(data_4d)
    print("rörelse korrektion tid:", int(time.time()-start))
    return corrected_data