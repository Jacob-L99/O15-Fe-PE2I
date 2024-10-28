# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:34:25 2024

@author: jacke
"""

import ants 
import numpy as np
import matplotlib.pyplot as plt

def MNI_to_pat(BP, registration_2, template_3d):

    transformed_np = BP





    fixed_image = template_3d
    inverse_transforms = registration_2['invtransforms']
    volume_index=10
    img_3d = ants.from_numpy(BP)
    moving_image = img_3d
    
    test=np.zeros(transformed_np.shape)

    test[64,78,100]=100

    test[64,78,60]=-100

    # plt.imshow(test[:,:,80])
    transformed_np = test



    # Convert the NumPy array to an ANTs image
    # It's crucial to provide the same metadata as the fixed image
    transformed_img = ants.from_numpy(
        transformed_np,
        origin=fixed_image.origin,
        spacing=fixed_image.spacing,
        direction=fixed_image.direction
    )

    print("Converted NumPy array to ANTs image.")

    # Apply the forward transforms to align the transformed image to the fixed image
    # Since the image is already transformed, this step might be redundant,
    # but if you need to apply additional transforms, you can do so here.

    # For demonstration, let's assume you want to apply the forward transform to the transformed_img
    # which may not be necessary if BP.npy is already transformed.

    # transformed_img_registered = ants.apply_transforms(
    #     fixed=fixed_image,
    #     moving=transformed_img,
    #     transformlist=forward_transforms,
    #     interpolator='linear'
    # )



    # ---------------------------
    # 6. Revert the Transformation Using Inverse Transforms
    # ---------------------------

    # To revert the transformed image back to the original space (moving image's space),
    # apply the inverse transforms.

    # Apply inverse transforms
    reverted_img = ants.apply_transforms(
        fixed=moving_image,                 # Target space: original moving image's space
        moving=transformed_img,             # Image to revert
        transformlist=inverse_transforms,    # Inverse transforms from registration
        interpolator='linear',               # Choose appropriate interpolator
        invert_transform=False               # Already using inverse transforms
    )

    print("Reverted the transformed image to the original space.")



    # ---------------------------
    # 7. (Optional) Visualize the Images
    # ---------------------------

    # Function to display a middle slice of an image
    # def display_middle_slice(image, title, ax):
    #     array = image.numpy()
    #     slice_index = array.shape[2] // 2-20  # Middle axial slice
    #     ax.imshow(array[:, :, slice_index], cmap='gray')
    #     ax.set_title(title)
    #     ax.axis('off')

    # # Create a figure with three subplots
    # fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    # display_middle_slice(moving_image, 'Original Moving Image', axs[0])
    # display_middle_slice(transformed_img, 'Transformed Image (BP)', axs[1])
    # display_middle_slice(reverted_img, 'Reverted Image', axs[2])

    # plt.tight_layout()
    # plt.show()

    
    print(type(reverted_img.numpy()))
    hej=reverted_img.numpy()
    print(np.max(hej))
    print(np.mean(hej))

    max_val = hej.max()
    max_positions = np.where(hej == max_val)
    max_indices = list(zip(*max_positions))
    z_max = np.array(max_indices)
    z_max = z_max[0][2]
    print(z_max)
    # plt.imshow(hej[:,:,35])
    # plt.show()

    min_val = hej.min()
    min_positions = np.where(hej == min_val)
    min_indices = list(zip(*min_positions))
    z_min = np.array(min_indices)
    z_min = z_min[0][2]
    print(z_min)
    # plt.imshow(hej[:,:,25])
    
    z_med = int(np.floor(z_min+(z_max-z_min)/2))
    return z_min, z_med, z_max

# #%%
# filnamn='FE-PE2I-BRAIN-VPFX-S-3-34'
# # filnamn= 'FE-PE2I-DYN-VPFX-S-3MM'
# nr="FE-PE2I-06-"

# import time
# import numpy as np
# start=time.time()

# from Parkinson_read import läsa_in_parkinson
# data_4d, first_image_shape, Ref_concentration_time = läsa_in_parkinson(filnamn)

# from Nersampling import Downsample
# data_4d=Downsample(data_4d, first_image_shape)

# from Registrering import Registrering
# registration_2, template_3d=Registrering(data_4d)

# from Rörelse_korrektion import rörelse_korrektion
# corrected_data=rörelse_korrektion(data_4d)

# from Parkinson_transform import transform_park
# small_corrected_data = transform_park(corrected_data, registration_2, template_3d)
# #%%
# start=time.time()
# first_z_min, first_z_max = MNI_to_pat(np.load('BP.npy'), registration_2, template_3d)
# print(f'tid: {time.time()-start}')

# #%%
# print(f'60={first_z_min}, 80={int(np.floor(first_z_min+(first_z_max-first_z_min)/2))}, 100={first_z_max}')