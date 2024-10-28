# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:40:51 2024

@author: jacke
"""

filnamn='FE-PE2I-BRAIN-VPFX-S-3-34'
# filnamn= 'FE-PE2I-DYN-VPFX-S-3MM'
nr="FE-PE2I-06-"

import time
import numpy as np
start=time.time()

from Parkinson_read import läsa_in_parkinson
data_4d, first_image_shape, Ref_concentration_time = läsa_in_parkinson(filnamn)

from Nersampling import Downsample
data_4d=Downsample(data_4d, first_image_shape)

from Registrering import Registrering
registration_2, template_3d=Registrering(data_4d)

from Rörelse_korrektion import rörelse_korrektion
corrected_data=rörelse_korrektion(data_4d)

from Parkinson_transform import transform_park
small_corrected_data = transform_park(corrected_data, registration_2, template_3d)

from Parkinson_ref_con import ref_con
Ref_TAC=ref_con(small_corrected_data)

# print(np.transpose(corrected_data, (3,0,1,2)).shape)
# print(small_corrected_data.shape)

from parkinson_beräkningar import beräkning_park
BP_reshape_list, K_2_reshape_list, R_I_reshape_list, K_2_p_reshape_list = beräkning_park(Ref_TAC, Ref_concentration_time, small_corrected_data)

# np.save("BP_pat.npy", BP_reshape_list)
# np.save("R_I_pat.npy", R_I_reshape_list)

from parkinson_plot import plot_specific_slices
plot_specific_slices(K_2_reshape_list, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=1, title="k_2")
plot_specific_slices(BP_reshape_list, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=7.5, title="BP")
plot_specific_slices(R_I_reshape_list, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=2.5, title="R_I")
plot_specific_slices(K_2_p_reshape_list, axis=2, slice_indices=[60, 80, 100], vmin=0, vmax=1, title="k_2'")
#%%
from Z_score_BP_R_I import z_score_BP_R_I
z_score_R_I, z_score_BP = z_score_BP_R_I(R_I_reshape_list, BP_reshape_list)

from MNI_to_pat_space import MNI_to_pat
z_min, z_med, z_max = MNI_to_pat(BP_reshape_list, registration_2, template_3d)

print('total tid för programmet: ', time.time()-start)

spara_namn_BP= nr+"BP.npy"
spara_namn_R_I= nr+"R_I.npy"
import numpy as np
#%%

print(z_min)
# np.save("BP.npy", BP_reshape_list)
# np.save("R_I.npy", R_I_reshape_list)
# np.save("z_score_R_I.npy", z_score_R_I)
# np.save(spara_namn_BP, BP_reshape_list)
# np.save(spara_namn_R_I, R_I_reshape_list)


