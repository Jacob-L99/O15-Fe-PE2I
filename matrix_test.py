import tkinter as tk
from tkinter import filedialog, messagebox
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from screeninfo import get_monitors

# Initialize global variables for selected paths and the number of selections
monitors = get_monitors()
monitor = monitors[0]  # Use the first monitor
original_screen_width = monitor.width
original_screen_height = monitor.height
scale_factor = 1.5 * (original_screen_width / 1920)

selected_directory1 = None
selected_file1 = None
selected_directory2 = None
selected_file2 = None
num_selections = 1

def proceed():
    global num_selections
    num_selections = 2 if two_files_var.get() else 1
    if selected_directory1 and selected_file1:
        if num_selections == 2 and (not selected_directory2 or not selected_file2):
            messagebox.showinfo("Info", "Välj både andra mappen och andra filen för att fortsätta.")
            return
        update_window_for_tasks()
    else:
        messagebox.showinfo("Info", "Välj åtminstone en mapp och en fil för att fortsätta.")

def def_global(n):
    global Wx, dicom_name, inf_name
    if n == 1:
        Wx = "wat1"
        dicom_name = selected_directory1
        inf_name = selected_file1
    elif n == 2:
        Wx = "wat2"
        dicom_name = selected_directory2
        inf_name = selected_file2

from Läsa_in_och_sortera import läsa_in
from Nersampling import Downsample
# from Registrering import Registrering
from Registrering_med_GUI import Registrering
from Rörelse_korrektion import rörelse_korrektion
from Beräkningar_3 import beräkningar_3
from Transform import transform
from SSP_2d import SSP_2D
from Z_score import SD_corrected
from Z_score_SSP import SSP_Z
from Z_score_brain_surface import fig_get
from Justera_c_bar import open_app_window


def flow_regions():
    data_4d_1, AIF_1, AIF_time_1, first_image_shape_1, age, sex = läsa_in(dicom_name, inf_name)
    loading_label.config(text="Omskalar bild")
    initial_window.update_idletasks()  # Force update of the label text
    data_4d_1 = Downsample(data_4d_1, first_image_shape_1)
    loading_label.config(text="Registrerar")
    initial_window.update_idletasks()  # Force update of the label text
    registration_2_1, template_3d_1=Registrering(data_4d_1, initial_window, loading_label, original_screen_width)
    for widget in initial_window.winfo_children():
        widget.pack_forget()
    loading_label.config(text="Rörelse korrection")
    loading_label.pack(expand=True)
    initial_window.update_idletasks()  # Force update of the label text
    initial_window.update()
    corrected_data_1=rörelse_korrektion(data_4d_1)
    loading_label.config(text="Beräknar")
    initial_window.update_idletasks()  # Force update of the label text
    K_1_reshape_list_1, K_2_reshape_list_1, V_a_reshape_list_1 = beräkningar_3(corrected_data_1, AIF_time_1, AIF_1)
    # np.save('K_2_reshape_list_1.npy', K_2_reshape_list_1)
    loading_label.config(text="Transformerar")
    initial_window.update_idletasks()  # Force update of the label text
    transformed_K_1_1, transformed_K_2_1, transformed_V_a_1 = transform(K_1_reshape_list_1, K_2_reshape_list_1, V_a_reshape_list_1, registration_2_1, template_3d_1)
    loading_label.config(text="Beräknar SSP")
    initial_window.update_idletasks()  # Force update of the label text
    first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2=SSP_2D(transformed_K_1_1)
    loading_label.config(text="Beräknar SSP Z")
    initial_window.update_idletasks()  # Force update of the label text
    age=50
    sex="M"
    Z_brain=SD_corrected(transformed_K_1_1, age, sex)
    loading_label.config(text="Beräknar SSP Z 2")
    initial_window.update_idletasks()  # Force update of the label text
    neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2 = SSP_Z(first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, first_values_xz_neg_y2)
    last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6 = fig_get(neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2)
    from plot_regioner_mean import regions_z_score
    regions_first_values_yz_neg_x0, regions_first_values_yz_pos_x1, regions_first_values_yz_pos_x2, regions_first_values_yz_neg_x2, regions_first_values_xz_pos_y2, regions_first_values_xz_neg_y2 = regions_z_score(transformed_K_1_1)
    
   # transformed_K_1_1, transformed_K_2_1, Z_brain, K_1_reshape_list_1=np.load("K_1_test.npy"),1,1,1
    # # K_2_reshape_list_1, first_values_yz_neg_x0, first_values_yz_pos_x1=1,1,1
    # # first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2=1,1,1
    # # first_values_xz_neg_y2=1
    # # neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2=1,1,1,1,1,1
    # # initial_window.destroy()
    V_a_reshape_list_1, K_2_reshape_list_1, K_1_reshape_list_1=np.transpose(V_a_reshape_list_1, (1,2,0)), np.transpose(K_2_reshape_list_1, (1,2,0)), np.transpose(K_1_reshape_list_1, (1,2,0))
    button_pressed = tk.StringVar()
    # Open the App window, passing the StringVar
    initial_window.app_window = open_app_window(initial_window, button_pressed, \
                                                transformed_K_1_1, transformed_K_2_1, Z_brain, K_1_reshape_list_1, \
                                                K_2_reshape_list_1, first_values_yz_neg_x0, first_values_yz_pos_x1, \
                                                first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
                                                first_values_xz_neg_y2, \
                                                last_figure_1, last_figure_2, last_figure_3, \
                                                last_figure_4, last_figure_5, last_figure_6, \
                                                regions_first_values_yz_neg_x0, regions_first_values_yz_pos_x1, \
                                                regions_first_values_yz_pos_x2, regions_first_values_yz_neg_x2, \
                                                regions_first_values_xz_pos_y2, regions_first_values_xz_neg_y2)

    # Wait until the StringVar is set by one of the buttons
    initial_window.wait_variable(button_pressed)

    # Retrieve the value set by the button
    response = button_pressed.get()
    print(f"Button pressed: {response}")
    initial_window.destroy()

    # hej=input("stäng av")
    # initial_window.destroy()
    if num_selections==2:
        def_global(2)
        data_4d_2, AIF_2, AIF_time_2, first_image_shape_2 = läsa_in(dicom_name, inf_name)
        loading_label.config(text="Omskalar bild")
        initial_window.update_idletasks()  # Force update of the label text
        data_4d_2 = Downsample(data_4d_2, first_image_shape_2)
        loading_label.config(text="Registrerar")
        initial_window.update_idletasks()  # Force update of the label text
        registration_2_2, template_3d_2=Registrering(data_4d_2)
        loading_label.config(text="Rörelse korrigering")
        initial_window.update_idletasks()  # Force update of the label text
        corrected_data_2=rörelse_korrektion(data_4d_2)
        loading_label.config(text="Beräknar")
        initial_window.update_idletasks()  # Force update of the label text
        V_a_reshape_list_2, K_2_reshape_list_2, K_1_reshape_list_2= beräkningar_3(AIF_2, AIF_time_2, corrected_data_2)
        loading_label.config(text="Transformerar")
        initial_window.update_idletasks()  # Force update of the label text
        transformed_K_1_2, transformed_K_2_2, transformed_V_a_2 = transform(K_1_reshape_list_2, K_2_reshape_list_2, V_a_reshape_list_2, registration_2_2, template_3d_2)
        loading_label.config(text="Beräknar SSP")
        initial_window.update_idletasks()  # Force update of the label text
        pixel_values0_2, pixel_values1_2, pixel_values2_2, Z_pixel_values0_2, Z_pixel_values1_2, Z_pixel_values2_2=SSP_2D(transformed_K_1_2)

from Parkinson_read import läsa_in_parkinson
from Parkinson_transform import transform_park
from Parkinson_ref_con import ref_con
from parkinson_beräkningar import beräkning_park
from Z_score_BP_R_I import z_score_BP_R_I
from MNI_to_pat_space import MNI_to_pat
from Justera_c_bar_parkison import open_app_window_park


def Parkinson(directory):
    initial_window.geometry(f"{int(0.625 * original_screen_width)}x{int(0.32 * original_screen_width)}")
    loading_label = tk.Label(initial_window, font=('Helvetica', int(16 * scale_factor)), fg='white', bg='black')
    # Hide all widgets but keep them in memory (don't destroy)
    for widget in initial_window.winfo_children():
        widget.pack_forget()
    loading_label.config(text="Läser in")
    loading_label.pack(expand=True)
    initial_window.update_idletasks()  # Force update of the label text
    initial_window.update()

    data_4d, first_image_shape, Ref_concentration_time = läsa_in_parkinson(directory)
    loading_label.config(text="Omskalar")
    initial_window.update_idletasks() 
    data_4d=Downsample(data_4d, first_image_shape)
    loading_label.config(text="Registrerar")
    initial_window.update_idletasks()  # Force update of the label text
    registration_2, template_3d=Registrering(data_4d, initial_window, loading_label, original_screen_width)
    for widget in initial_window.winfo_children():
        widget.pack_forget()
    loading_label.config(text="Rörelse korrigering")
    loading_label.pack(expand=True)
    initial_window.update_idletasks()  # Force update of the label text
    initial_window.update()
    corrected_data=rörelse_korrektion(data_4d)
    loading_label.config(text="Transformerar")
    initial_window.update_idletasks()  # Force update of the label text
    small_corrected_data = transform_park(corrected_data, registration_2, template_3d)
    loading_label.config(text="Beräknar ref concentration")
    initial_window.update_idletasks()  # Force update of the label text
    Ref_TAC=ref_con(small_corrected_data)
    loading_label.config(text="Beräknar")
    initial_window.update_idletasks()  # Force update of the label text
    BP_reshape_list, K_2_reshape_list, R_I_reshape_list, K_2_p_reshape_list = beräkning_park(Ref_TAC, Ref_concentration_time, small_corrected_data)
    loading_label.config(text="Beräknar Z-score")
    initial_window.update_idletasks()  # Force update of the label text
    z_score_R_I, z_score_BP = z_score_BP_R_I(R_I_reshape_list, BP_reshape_list)
    z_min, z_med, z_max = MNI_to_pat(BP_reshape_list, registration_2, template_3d)
    button_pressed = tk.StringVar()
    open_app_window_park(initial_window, button_pressed, BP_reshape_list, R_I_reshape_list, z_score_R_I, z_min, z_med, z_max)
    initial_window.wait_variable(button_pressed)

    # Retrieve the value set by the button
    response = button_pressed.get()

    
    initial_window.destroy()


def fort3_1():
    loading_label.config(text="klar")
    initial_window.destroy()

def update_window_for_tasks():
    for widget in initial_window.winfo_children():
        widget.pack_forget()
    loading_label.config(text="Läser in")
    loading_label.pack(expand=True)
    def_global(1)
    initial_window.after(100, flow_regions)
    


def change_template_function():
    print("byter template")
    

from parkinson_screen import parkinson_function

# Initialize the initial selection window
initial_window = tk.Tk()
# initial_window.title("AMANDAV: står för den stakaste tjejen jag vet och min gymchrush❤️❤️❤️, hon kommer ta 201kg före Joar!")
initial_window.title("Perfusion and SSP")
initial_window.configure(background='black')
initial_window.geometry(f"{int(0.625 * original_screen_width)}x{int(0.32 * original_screen_width)}")

def initial():
    global loading_label
    global two_files_var
    global types
    selected_directory1 = None
    selected_file1 = None
    selected_directory2 = None
    selected_file2 = None
    num_selections = 1
    types = "dicom"
    
    for widget in initial_window.winfo_children():
        widget.destroy()

    initial_window.geometry(f"{int(0.625 * original_screen_width)}x{int(0.32 * original_screen_width)}")
    loading_label = tk.Label(initial_window, font=('Helvetica', int(16 * scale_factor)), fg='white', bg='black')

    def choose_directory(number):
        global selected_directory1, selected_directory2
        directory = filedialog.askdirectory(title=f"Välj mapp {number}")
        if directory:
            if number == 1:
                selected_directory1 = directory
                choose_dir_btn1.config(text=f"Mapp 1: {directory.split('/')[-1]}")
            else:
                selected_directory2 = directory
                choose_dir_btn2.config(text=f"Mapp 2: {directory.split('/')[-1]}")

    def choose_file(number):
        global selected_file1, selected_file2
        file_path = filedialog.askopenfilename(
            title=f"Välj .inp-fil {number}",
            filetypes=[("INP files", "*.inp")]
        )
        if file_path:
            if number == 1:
                selected_file1 = file_path
                choose_file_btn1.config(text=f"Fil 1: {file_path.split('/')[-1]}")
            else:
                selected_file2 = file_path
                choose_file_btn2.config(text=f"Fil 2: {file_path.split('/')[-1]}")

    def toggle_additional_options():
        state = tk.NORMAL if two_files_var.get() else tk.DISABLED
        choose_dir_btn2.config(state=state)
        choose_file_btn2.config(state=state)

    def choose_nii_file(number):
        global selected_directory1, selected_directory2
        file_path = filedialog.askopenfilename(
            title=f"Välj .nii fil {number}",
            filetypes=[("NIfTI files", "*.nii;*.nii.gz")]
        )
        if file_path:
            if number == 1:
                selected_directory1 = file_path
                choose_dir_btn1.config(text=f"Fil 1: {file_path.split('/')[-1]}")
            else:
                selected_directory2 = file_path
                choose_dir_btn2.config(text=f"Fil 2: {file_path.split('/')[-1]}")

    def change_to_nii():
        global types
        if nii_files_var.get():
            types = "nii"
            choose_dir_btn1.config(command=lambda: choose_nii_file(1))
            choose_dir_btn1.config(text="Välj första .nii filen")
            choose_dir_btn2.config(command=lambda: choose_nii_file(2))
            choose_dir_btn2.config(text="Välj andra .nii filen")
        else:
            types = "dicom"
            choose_dir_btn1.config(command=lambda: choose_directory(1))
            choose_dir_btn1.config(text="Välj första mapp")
            choose_dir_btn2.config(command=lambda: choose_directory(2))
            choose_dir_btn2.config(text="Välj andra mapp")

    # Bottom buttons defined first to anchor them
    bottom_frame = tk.Frame(initial_window, background='black')
    bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=20)



    # "Parkinson" button
    parkinson_btn = tk.Button(bottom_frame, text="Parkinson", command=lambda: parkinson_function(initial_window, initial, Parkinson), fg='white', bg='grey')
    parkinson_btn.pack(pady=10)

    # Other components (like directory and file selection) defined after bottom buttons
    two_files_var = tk.BooleanVar(value=False)
    two_files_check = tk.Checkbutton(initial_window, text="Välj två mappar och filer", var=two_files_var, 
                                     command=toggle_additional_options, fg='white', bg='black', selectcolor='grey')
    two_files_check.pack(pady=10)
    
    # Checkbox for selecting ".nii" files
    nii_files_var = tk.BooleanVar(value=False)
    nii_files_check = tk.Checkbutton(initial_window, text="Använd endast '.nii' filer", var=nii_files_var, 
                                     command=change_to_nii, fg='white', bg='black', selectcolor='grey')
    nii_files_check.pack(pady=10)
    
    frame_left = tk.Frame(initial_window, background='black')
    frame_right = tk.Frame(initial_window, background='black')
    
    choose_dir_btn1 = tk.Button(frame_left, text="Välj första mapp", command=lambda: choose_directory(1), fg='white', bg='grey')
    choose_file_btn1 = tk.Button(frame_left, text="Välj första fil", command=lambda: choose_file(1), fg='white', bg='grey')
    choose_dir_btn2 = tk.Button(frame_right, text="Välj andra mapp", command=lambda: choose_directory(2), state=tk.DISABLED, fg='white', bg='grey')
    choose_file_btn2 = tk.Button(frame_right, text="Välj andra fil", command=lambda: choose_file(2), state=tk.DISABLED, fg='white', bg='grey')
    
    choose_dir_btn1.pack(pady=10)
    choose_file_btn1.pack(pady=10)
    choose_dir_btn2.pack(pady=10)
    choose_file_btn2.pack(pady=10)
    
    continue_btn = tk.Button(initial_window, text="Fortsätt", command=proceed, fg='white', bg='gray')
    continue_btn.pack(pady=20)
    
    frame_left.pack(side=tk.LEFT, fill=tk.Y, expand=True, padx=20, pady=20)
    frame_right.pack(side=tk.RIGHT, fill=tk.Y, expand=True, padx=20, pady=20)

initial()


# Add this line to keep the window open and responsive
initial_window.mainloop()
