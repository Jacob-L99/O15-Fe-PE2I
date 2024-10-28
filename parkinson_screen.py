import tkinter as tk
from tkinter import filedialog, messagebox


# Global variables to track selected directory and file
selected_directory = None

def parkinson_function(initial_window, initial, on_proceed):
    global selected_directory, selected_file  # Make sure to use global variables for directory and file
    
    # Clear the current window to update it for the Parkinson screen
    for widget in initial_window.winfo_children():
        widget.destroy()

    # Define the change_to_nii function for the Parkinson screen
    def change_to_nii():
        global types
        if nii_files_var.get():
            types = "nii"
            choose_dir_btn.config(command=lambda: choose_nii_file(choose_dir_btn, 1))
            choose_dir_btn.config(text="Välj första .nii fil")
        else:
            types = "dicom"
            choose_dir_btn.config(command=lambda: choose_directory(choose_dir_btn))
            choose_dir_btn.config(text="Välj mapp")

    # Checkbox for selecting ".nii" files
    nii_files_var = tk.BooleanVar(value=False)
    nii_files_check = tk.Checkbutton(initial_window, text="Använd endast '.nii' filer", var=nii_files_var, 
                                     command=change_to_nii, fg='white', bg='black', selectcolor='grey')
    nii_files_check.pack(pady=10)

    # Continue button, same place as before
    continue_btn = tk.Button(initial_window, text="Fortsätt", command=lambda: proceed(on_proceed), fg='white', bg='gray')
    continue_btn.pack(pady=20)

    # Create a frame to hold the "Välj mapp" button in the same row
    button_frame = tk.Frame(initial_window, bg='black')
    button_frame.pack(pady=20)  # Add space above and below the button

    # "Välj mapp" button
    choose_dir_btn = tk.Button(button_frame, text="Välj mapp", command=lambda: choose_directory(choose_dir_btn), fg='white', bg='grey')
    choose_dir_btn.pack(side=tk.LEFT, padx=10)  # Space between the buttons

    # "15-O" button to return to the initial screen
    back_btn = tk.Button(initial_window, text="15-O", command=initial, fg='white', bg='grey')
    back_btn.pack(pady=20)

# Function to handle selecting .nii files and update button text
def choose_nii_file(button, number):
    global selected_directory
    file_path = filedialog.askopenfilename(
        title=f"Välj .nii fil {number}",
        filetypes=[("NIfTI files", "*.nii;*.nii.gz")]
    )
    if file_path:
        selected_directory = file_path
        # Update button text to show the selected file name
        button.config(text=f"Fil 1: {file_path.split('/')[-1]}")
        print(f"Selected .nii file: {file_path}")

# Function to handle selecting directories and update button text
def choose_directory(button):
    global selected_directory
    directory = filedialog.askdirectory(title="Välj mapp")
    if directory:
        selected_directory = directory
        # Update button text to show the selected folder name
        button.config(text=f"Mapp: {directory.split('/')[-1]}")
        print(f"Selected directory: {directory}")

# Function to handle the "Fortsätt" button press and return values
def proceed(on_proceed):
    global selected_directory
    
    # Check if at least one directory is selected
    if selected_directory:
        print(f"Proceeding with directory: {selected_directory}")
        on_proceed(selected_directory)  # Call the callback function with the selected paths
    else:
        messagebox.showinfo("Info", "Välj åtminstone en mapp för att fortsätta.")
        # You could add a message box or label here to notify the user, if needed.