# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 09:43:48 2024

@author: jacke
"""


import numpy as np
import time

start=time.time()
inf_name="ASPC0230_02_WAT_aQuant_corrected.inp"
# inf_name='ASPC0230_13_WAT_corrected.inp'
dicom_name="WAT-BRAIN-VPFX-S-3-34"
nr="ASPC0230-02"

# inf_name='IF_interp_s308_10478_WAT1._15_5s_fitvb_ekvb.inp'
# dicom_name="QCFX-S 300 WAT1 s308"
# nr="Diamox-wat1-s308-"


from Läsa_in_och_sortera import läsa_in
data_4d, AIF, AIF_time, first_image_shape, age, sex=läsa_in(dicom_name, inf_name)

#%%
from Nersampling import Downsample
data_4d=Downsample(data_4d, first_image_shape)
#%%
from Registrering import Registrering
registration_2, template_3d=Registrering(data_4d)

from Rörelse_korrektion import rörelse_korrektion
corrected_data=rörelse_korrektion(data_4d)

#%%
from Beräkningar_3 import beräkningar_3
K_1_reshape_list, K_2_reshape_list, V_a_reshape_list  = beräkningar_3(corrected_data, AIF_time, AIF)

#%%
from Transform import transform
transformed_K_1, transformed_K_2, transformed_V_a = transform(K_1_reshape_list, K_2_reshape_list, V_a_reshape_list, registration_2, template_3d)

#%%
from SSP_2d import SSP_2D
first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2=SSP_2D(transformed_K_1)
#%%
age=50
sex="M"
from Z_score import SD_corrected
Z_brain=SD_corrected(transformed_K_1, age, sex)

#%%
from Z_score_SSP import SSP_Z
neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2 = SSP_Z(first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2)

from Z_score_brain_surface import fig_get
fig_get(neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2)
#%%
print("Total tid=", int(time.time()-start),"s")

from MNI_to_pat_space import MNI_to_pat
z_min, z_med, z_max = MNI_to_pat(transformed_K_1, registration_2, template_3d)

save='K_1-' + nr + '.npy'
np.save(save, transformed_K_1)