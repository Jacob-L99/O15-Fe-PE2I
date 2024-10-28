# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:56:39 2024

@author: jacke
"""
import matplotlib.pyplot as plt
import numpy as np
import ants
import time
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

def Registrering(data_4d):  
    image_3d_downsampled=np.load('small_templat_corrected.npy')
    print(image_3d_downsampled.shape)
    regions_downsampled=np.load("ter_down.npy")
    
    def plot_slices(volume, title, cm, slice_step=8):
        slices = volume.shape[2]
        fig, axes = plt.subplots(nrows=1, ncols=(slices // slice_step) + 1, figsize=(20, 4))
        fig.suptitle(title)
        for i, ax in enumerate(axes.flatten()):
            slice_idx = i * slice_step+5
            if slice_idx < slices:
                ax.imshow(volume[:, :, slice_idx], cmap=cm, vmin=0, vmax=np.max(volume))
                # ax.imshow(np.rot90(np.array(volume[:, :, slice_idx])), cmap=cm) # om jag vill se bilderna med 90 grader rot
                ax.set_title(f'Slice {slice_idx}')
                ax.axis('off')
            else:
                ax.axis('off')  # Hide unused subplots
        # Show the plot
        plt.show()
    
        # Close the figure to free up memory
        plt.close(fig)  # This line closes the current figure
    # data_4d = data_4d[:, ::-1, :] # invert the image (hjärnorna)
    volume_index = 10  # For example, extracting the 11th volume
    img_3d = ants.from_numpy(data_4d[:,:,:,volume_index])
    
    # Load the template 3D NIfTI file
    
    template_file_path = 'caa_t1_in_mni_template_smooth.nii'
    template_3d_flip = ants.image_read(template_file_path)
    # Convert the numpy array back to an ANTsImage
    template_3d = ants.from_numpy(image_3d_downsampled, origin=template_3d_flip.origin, spacing=template_3d_flip.spacing, direction=template_3d_flip.direction)
    
    while True:
        start_tid_1=time.time()
        random_seed = 42
        np.random.seed(random_seed)
        registration_2 = ants.registration(fixed=template_3d, moving=img_3d , type_of_transform='SyN')
        
        transformed_img_3d = ants.apply_transforms(fixed=template_3d, moving=img_3d, transformlist=registration_2['fwdtransforms'])
        
        
        # Plot slices from the template_3d, img_3d, and transformed_img_3d
        plot_slices(template_3d.numpy(), 'Template Image Slices',"gray")
        # plot_slices(img_3d.numpy(), 'Moving Image Slices')
        plot_slices(transformed_img_3d.numpy(), f'Registered Image Slices (slice:{volume_index})',my_cmap)
        slut_tid_1=time.time()
        reg_tid=slut_tid_1-start_tid_1
        print("Registrering tid:", reg_tid)
        print("är du nöjd med registreringen? (ja/nej)")
        svar=input()
        # svar="ja"
        if svar=="ja":
            break
    return registration_2, template_3d
        