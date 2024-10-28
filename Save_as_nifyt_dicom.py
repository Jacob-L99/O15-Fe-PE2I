# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:25:24 2024

@author: jacke
"""

import numpy as np
import nibabel as nib
import os

def save_as_nifti(arrays, filenames, affine=np.eye(4)):
    """
    Save multiple 3D NumPy arrays as separate NIfTI files.

    Parameters:
    - arrays (list or tuple of np.ndarray): 3D NumPy arrays to be saved.
    - filenames (list or tuple of str): Output filenames or full paths for the NIfTI files.
    - affine (np.ndarray): 4x4 affine transformation matrix. Defaults to identity matrix.

    Raises:
    - TypeError: If any input is not a NumPy array or filenames are not strings.
    - ValueError: If any input array is not 3D or if the number of arrays and filenames do not match.
    - OSError: If the directory for a filename does not exist and cannot be created.
    """
    if not isinstance(arrays, (list, tuple)):
        raise TypeError("arrays must be a list or tuple of NumPy arrays.")
    if not isinstance(filenames, (list, tuple)):
        raise TypeError("filenames must be a list or tuple of strings.")
    if len(arrays) != len(filenames):
        raise ValueError("The number of arrays and filenames must be the same.")
    
    for idx, (array, fname) in enumerate(zip(arrays, filenames), start=1):
        # Validate that the input is a NumPy array
        if not isinstance(array, np.ndarray):
            raise TypeError(f"Input {idx} ({fname}) is not a NumPy array.")
        
        # Validate that the array is 3D
        if array.ndim != 3:
            raise ValueError(f"Input {idx} ({fname}) is not a 3D array. It has {array.ndim} dimensions.")
        
        # Ensure the directory exists
        dir_name = os.path.dirname(fname)
        if dir_name and not os.path.exists(dir_name):
            try:
                os.makedirs(dir_name)
                print(f"Created directory: {dir_name}")
            except OSError as e:
                raise OSError(f"Could not create directory {dir_name}: {e}")
        
        # Create a NIfTI image
        nifti_img = nib.Nifti1Image(array, affine)
        
        # Save the NIfTI file
        nib.save(nifti_img, fname)
        print(f"Saved {fname} successfully.")




# if __name__ == "__main__":
#     # Create sample 3D NumPy arrays (e.g., synthetic MRI data)
#     array1 = np.random.rand(64, 64, 30)  # Replace with your actual data
#     array2 = np.random.rand(64, 64, 30)  # Replace with your actual data
#     array3 = np.random.rand(64, 64, 30)  # Replace with your actual data
#     array4 = np.random.rand(64, 64, 30)  # Additional array
#     array5 = np.random.rand(64, 64, 30)  # Additional array

#     # Define filenames with different directories
#     filenames = [
#         'scan1.nii',          # Saved in 'subject1' directory
#         'scan2.nii',          # Saved in 'subject1' directory
#         'scan1.nii',          # Saved in 'subject2' directory
#         'scan3.nii',    # Saved in an absolute path
#         'scan4.nii'                     # Saved in the current directory
#     ]

#     # List of arrays to save
#     arrays = [array1, array2, array3, array4, array5]

#     # Optionally, define an affine matrix (here using identity)
#     affine_matrix = np.eye(4)  # Modify if you have specific spatial information

#     # Save the arrays as NIfTI files
#     save_as_nifti(arrays, filenames, affine=affine_matrix)


# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:00:00 2024

@author:
"""


import pydicom
from pydicom.dataset import Dataset, FileDataset
import datetime
import tempfile

def save_as_dicom(arrays, output_dirs, patient_id='12345', study_instance_uid=None, series_instance_uid=None, sop_instance_uid_prefix=None):
    """
    Save multiple 3D NumPy arrays as separate DICOM series.
    
    Parameters:
    - arrays (list or tuple of np.ndarray): 3D NumPy arrays to be saved.
    - output_dirs (list or tuple of str): Directories where each DICOM series will be saved.
    - patient_id (str): Patient ID to include in DICOM metadata. Default is '12345'.
    - study_instance_uid (str): UID for the study. If None, a new UID is generated.
    - series_instance_uid (list of str): List of UIDs for each series. If None, new UIDs are generated.
    - sop_instance_uid_prefix (str): Prefix for SOP Instance UIDs. If None, a random UID is generated.
    
    Raises:
    - TypeError: If inputs are of incorrect types.
    - ValueError: If lengths of arrays and output_dirs do not match.
    - OSError: If directories cannot be created.
    """
    import uuid
    
    if not isinstance(arrays, (list, tuple)):
        raise TypeError("arrays must be a list or tuple of 3D NumPy arrays.")
    if not isinstance(output_dirs, (list, tuple)):
        raise TypeError("output_dirs must be a list or tuple of directory paths.")
    if len(arrays) != len(output_dirs):
        raise ValueError("The number of arrays must match the number of output directories.")
    
    # Generate Study Instance UID if not provided
    if study_instance_uid is None:
        study_instance_uid = pydicom.uid.generate_uid()
    
    # Generate Series Instance UIDs if not provided
    if series_instance_uid is None:
        series_instance_uid = [pydicom.uid.generate_uid() for _ in arrays]
    elif isinstance(series_instance_uid, list) or isinstance(series_instance_uid, tuple):
        if len(series_instance_uid) != len(arrays):
            raise ValueError("Length of series_instance_uid must match the number of arrays.")
    else:
        raise TypeError("series_instance_uid must be a list or tuple of UIDs.")
    
    # Generate SOP Instance UID prefix if not provided
    if sop_instance_uid_prefix is None:
        sop_instance_uid_prefix = pydicom.uid.generate_uid()[:64]  # Max length for UID
    
    for idx, (array, out_dir, series_uid) in enumerate(zip(arrays, output_dirs, series_instance_uid), start=1):
        # Validate that the input is a 3D NumPy array
        if not isinstance(array, np.ndarray):
            raise TypeError(f"Array {idx} is not a NumPy array.")
        if array.ndim != 3:
            raise ValueError(f"Array {idx} is not 3D. It has {array.ndim} dimensions.")
        
        # Ensure the output directory exists
        if not os.path.exists(out_dir):
            try:
                os.makedirs(out_dir)
                print(f"Created directory: {out_dir}")
            except OSError as e:
                raise OSError(f"Could not create directory {out_dir}: {e}")
        
        # Iterate over each slice in the 3D array
        num_slices = array.shape[2]
        for slice_idx in range(num_slices):
            # Create a new FileDataset instance (Initial DICOM file)
            file_meta = pydicom.dataset.FileMetaDataset()
            file_meta.MediaStorageSOPClassUID = pydicom.uid.generate_uid()  # Example UID
            file_meta.MediaStorageSOPInstanceUID = pydicom.uid.generate_uid()
            file_meta.ImplementationClassUID = pydicom.uid.generate_uid()
            
            ds = FileDataset(None, {}, file_meta=file_meta, preamble=b"\0" * 128)
            
            # Set the transfer syntax
            ds.is_little_endian = True
            ds.is_implicit_VR = True
            
            # Set patient and study information
            ds.PatientID = patient_id
            ds.StudyInstanceUID = study_instance_uid
            ds.SeriesInstanceUID = series_uid
            ds.SOPInstanceUID = f"{sop_instance_uid_prefix}.{idx}.{slice_idx+1}"
            ds.SOPClassUID = pydicom.uid.generate_uid()
            
            # Set study and series descriptions
            ds.StudyDescription = "Example Study"
            ds.SeriesDescription = f"Series {idx}"
            
            # Set image specifics
            ds.Modality = "MR"  # Change as appropriate
            ds.InstanceNumber = slice_idx + 1
            ds.ImagePositionPatient = [0.0, 0.0, float(slice_idx)]
            ds.ImageOrientationPatient = [1,0,0,0,1,0]
            ds.PixelSpacing = [1.0, 1.0]  # Example spacing
            ds.SliceThickness = 1.0  # Example thickness
            ds.Rows, ds.Columns = array.shape[0], array.shape[1]
            ds.PixelData = array[:, :, slice_idx].tobytes()
            ds.BitsAllocated = 16
            ds.BitsStored = 16
            ds.HighBit = 15
            ds.SamplesPerPixel = 1
            ds.PhotometricInterpretation = "MONOCHROME2"
            ds.PixelRepresentation = 1  # 0 for unsigned, 1 for signed
            ds.RescaleIntercept = "0"
            ds.RescaleSlope = "1"
            
            # Set the necessary DICOM header fields
            ds.ContentDate = datetime.datetime.now().strftime('%Y%m%d')
            ds.ContentTime = datetime.datetime.now().strftime('%H%M%S')
            
            # Define the filename
            filename = os.path.join(out_dir, f"slice_{slice_idx+1:03d}.dcm")
            
            # Save the DICOM file
            ds.save_as(filename)
            print(f"Saved DICOM slice: {filename}")
    
    print("All DICOM series have been saved successfully.")
    
# import numpy as np

# if __name__ == "__main__":
#     # Create sample 3D NumPy arrays (e.g., synthetic MRI data)
#     array1 = np.random.randint(-32768, 32767, size=(64, 64, 30), dtype=np.int16)  # Example signed 16-bit data
#     array2 = np.random.randint(-32768, 32767, size=(64, 64, 25), dtype=np.int16)
#     array3 = np.random.randint(-32768, 32767, size=(64, 64, 28), dtype=np.int16)
    
#     # Define output directories for each DICOM series
#     output_dirs = [
#         'subject1_scan1',
#         'subject1_scan2',
#         'subject2_scan1'
#     ]
    
#     # List of arrays to save
#     arrays = [array1, array2, array3]
    
#     # Optionally, define series_instance_uid (must be unique for each series)
#     # If not provided, the function will generate them
#     # series_instance_uid = [pydicom.uid.generate_uid() for _ in arrays]
    
#     # Save the arrays as DICOM series
#     save_as_dicom(
#         arrays=arrays,
#         output_dirs=output_dirs,
#         patient_id='Patient_001',
#         # series_instance_uid=series_instance_uid,  # Optional
#         # study_instance_uid='1.2.840.113619.2.55.3.604688123.12345.1607771234.467',  # Optional
#         # sop_instance_uid_prefix='1.2.840.113619.2.55.3.604688123.12345.1607771234'
#     )

