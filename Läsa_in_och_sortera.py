# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:44:37 2024

@author: jacke
"""
import numpy as np
import os
import pydicom
import time
import re  # Import regex module for age parsing

def läsa_in(dicom_name, inf_name):
    def apply_dicom_slope_intercept(pixel_array, slope, intercept):
        """Apply DICOM slope and intercept to pixel values."""
        return (pixel_array * slope + intercept) / 1000

    def load_and_sort_dicom_images(directory, frames):
        global first_image_shape
        # List all DICOM files in the directory
        dicom_files = [f for f in os.listdir(directory) if f.endswith('.dcm')]

        # Initialize age and sex variables
        age = None
        sex = None

        # Read each file and extract slice number, acquisition time, slope, and intercept
        dicom_files_with_info = []
        for filename in dicom_files:
            file_path = os.path.join(directory, filename)
            dicom_image = pydicom.dcmread(file_path)
            slice_number = dicom_image.get('InstanceNumber', float('inf'))
            acquisition_time = dicom_image.get('AcquisitionTime', 'Unknown')
            slope = dicom_image.get('RescaleSlope', 1)
            intercept = dicom_image.get('RescaleIntercept', 0)

            # # Extract age and sex from the first DICOM file
            # if age is None:
            #     raw_age = dicom_image.get('PatientAge', 'Unknown')
            #     if raw_age != 'Unknown':
            #         # Use regex to extract numeric part
            #         match = re.match(r'(\d+)([YMDW])', raw_age)
            #         if match:
            #             age_value, age_unit = match.groups()
            #             age = int(age_value.lstrip('0'))  # Remove leading zeros and convert to int
            #             # Convert age to years if necessary
            #             if age_unit == 'M':
            #                 age = age / 12  # Convert months to years
            #             elif age_unit == 'W':
            #                 age = age / 52  # Convert weeks to years
            #             elif age_unit == 'D':
            #                 age = age / 365  # Convert days to years
            #             # Round age to two decimal places
            #             age = round(age, 2)
            #         else:
            #             age = 'Unknown'
            #     else:
            #         age = 'Unknown'

            # if sex is None:
            #     sex = dicom_image.get('PatientSex', 'Unknown')

            dicom_files_with_info.append(
                (file_path, slice_number, acquisition_time, slope, intercept))

        # Sort the list by slice number
        dicom_files_sorted = sorted(dicom_files_with_info, key=lambda x: x[1])

        images = []
        for i in range(len(dicom_files_sorted)):
            file_path, slice_number, acquisition_time, slope, intercept = dicom_files_sorted[i]
            dicom_image = pydicom.dcmread(file_path)
            pixel_array = apply_dicom_slope_intercept(dicom_image.pixel_array, slope, intercept)
            images.append(pixel_array)

        # Assuming all images have the same dimensions, extract the shape from the first image
        first_image_shape = images[0].shape

        slices = int(len(dicom_files_sorted) / frames)
        # Reshape according to the read dimensions and the number of frames and slices
        data_4d = np.array(images).reshape(frames, slices, *first_image_shape)
        # Transpose the array to fit the desired shape (y, x, slices, time)
        data_4d_reshaped = np.transpose(data_4d, (3, 2, 1, 0))
        return data_4d_reshaped, age, sex

    # Read AIF curve and times from .inp file
    start_tid_0 = time.time()
    inp_file_path = inf_name

    # Initialize lists to store the data from each column
    AIF_time = []
    AIF = []

    # Open and read the .inp file
    with open(inp_file_path, 'r') as file:
        for line in file:
            # Split each line into parts based on whitespace
            parts = line.strip().split()
            if len(parts) >= 2:
                # Append data to respective lists
                AIF_time.append(float(parts[0]))
                AIF.append(float(parts[1]))

    AIF_time = np.array(AIF_time)
    AIF = np.array(AIF)
    frames = len(AIF_time)

    dicom_directory = dicom_name
    data_4d, age, sex = load_and_sort_dicom_images(dicom_directory, frames)
    slut_tid_0 = time.time()
    sort_tid = slut_tid_0 - start_tid_0
    print("läsa in och sortera tid:", int(sort_tid), "s")

    return data_4d, AIF, AIF_time, first_image_shape, age, sex
