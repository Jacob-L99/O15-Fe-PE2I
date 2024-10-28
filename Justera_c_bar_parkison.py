import matplotlib
from matplotlib.colors import LinearSegmentedColormap
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.gridspec import GridSpec
from matplotlib.colors import Normalize
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt

# Define the custom colormaps
cdict = {
    'red': (
        (0.0, 0.0, 0.0),
        (0.1, 0.5, 0.5),
        (0.2, 0.0, 0.0),
        (0.4, 0.2, 0.2),
        (0.6, 0.0, 0.0),
        (0.8, 1.0, 1.0),
        (1.0, 1.0, 1.0)
    ),
    'green': (
        (0.0, 0.0, 0.0),
        (0.1, 0.0, 0.0),
        (0.2, 0.0, 0.0),
        (0.4, 1.0, 1.0),
        (0.6, 1.0, 1.0),
        (0.8, 1.0, 1.0),
        (1.0, 0.0, 0.0)
    ),
    'blue': (
        (0.0, 0.0, 0.0),
        (0.1, 0.5, 0.5),
        (0.2, 1.0, 1.0),
        (0.4, 1.0, 1.0),
        (0.6, 0.0, 0.0),
        (0.8, 0.0, 0.0),
        (1.0, 0.0, 0.0)
    )
}

my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', cdict, 256)

# Define the custom blue-white-red colormap
colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1, 1, 1), (1, 0, 0), (0.5, 0, 0)]
n_bins = 10
cmap_name = 'custom_blue_white_red'
custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)


class App(tk.Toplevel):
    def __init__(self, BP_MNI=None, R_I_MNI=None, Z_brain=None, z_min=None, z_med=None, z_max=None,
                 master=None, button_var=None):
        """
        Initializes the App window.

        Args:
            master (tk.Tk or tk.Toplevel): The parent window.
            button_var (tk.StringVar): Variable to capture which button is pressed.
        """
        super().__init__(master)
        self.resizing = False  # Flag to prevent recursive resizing
        self.state('zoomed')  # Keep the window maximized
        self.button_var = button_var  # Store the reference to the StringVar
        self.title("Adjust Colormap Scale")
        self.configure(bg="black")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Style configuration for dark theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="grey", foreground="white")
        style.configure("TFrame", background="black")
        style.configure("TLabel", background="black", foreground="white")
        style.configure("TCombobox", background="grey", foreground="white", fieldbackground="grey")
        style.configure("TScale", background="black", troughcolor="grey", sliderlength=30)

        # Configure the main window's grid
        self.grid_rowconfigure(0, weight=1)  # Main content
        self.grid_rowconfigure(1, weight=0)  # Bottom buttons
        self.grid_columnconfigure(0, weight=1)

        # Main frame to hold canvas and sliders
        main_frame = ttk.Frame(self, style="TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_rowconfigure((0, 1, 2), weight=1)
        main_frame.grid_columnconfigure(1, weight=1)  # Column for figures

        # Create three matplotlib figures without fixed figsize
        self.fig1 = Figure(facecolor='black')
        gs1 = GridSpec(1, 4, width_ratios=[1, 1, 1, 0.02], figure=self.fig1)  # Reduced colorbar width ratio
        self.ax1 = [self.fig1.add_subplot(gs1[0, i]) for i in range(3)]
        self.cbar_ax1 = self.fig1.add_subplot(gs1[0, 3])

        self.fig2 = Figure(facecolor='black')
        gs2 = GridSpec(1, 4, width_ratios=[1, 1, 1, 0.02], figure=self.fig2)  # Reduced colorbar width ratio
        self.ax2 = [self.fig2.add_subplot(gs2[0, i]) for i in range(3)]
        self.cbar_ax2 = self.fig2.add_subplot(gs2[0, 3])

        self.fig3 = Figure(facecolor='black')
        gs3 = GridSpec(1, 4, width_ratios=[1, 1, 1, 0.02], figure=self.fig3)  # Reduced colorbar width ratio
        self.ax3 = [self.fig3.add_subplot(gs3[0, i]) for i in range(3)]
        self.cbar_ax3 = self.fig3.add_subplot(gs3[0, 3])

        # Load or generate test datasets for the first three rows
        try:
            self.data1 = np.rot90(BP_MNI)
            self.data2 = np.rot90(R_I_MNI)
            self.data3 = np.rot90(Z_brain)  # For the third row
            self.data4 = np.rot90(Z_brain)  # Z-score data

            self.data5 = np.rot90(np.rot90(np.rot90(np.load('BP_pat.npy'))))
            self.data6 = np.rot90(np.rot90(np.rot90(np.load('R_I_pat.npy'))))

        except FileNotFoundError as e:
            print(f"Data file not found: {e}")
            messagebox.showerror("Error", f"Data file not found: {e}")
            self.destroy()
            return

        # Select specific channels to display
        slices = [60, 80, 100]
        self.channel_data1 = [self.data1[..., i] for i in slices]
        self.channel_data2 = [self.data2[..., i] for i in slices]
        self.channel_data3 = [self.data3[..., i] for i in slices]
        self.channel_data4 = [self.data4[..., i] for i in slices]

        slices_2 = [z_min, z_med, z_max]
        self.channel_data5 = [self.data5[..., i] for i in slices_2]
        self.channel_data6 = [self.data6[..., i] for i in slices_2]

        # Initialize normalization objects
        self.norm = Normalize(vmin=0, vmax=10)
        self.norm2 = Normalize(vmin=0, vmax=5)  # New Normalization for Row 2
        self.norm3 = Normalize(vmin=-5, vmax=5)
        self.norm4 = Normalize(vmin=-5, vmax=5)  # For Z-score data

        # Define colormap
        self.cmap = my_cmap
        self.cmap_BWR = custom_cmap

        # Initialize image plots with the datasets
        self.images1 = [
            self.ax1[i].imshow(self.channel_data1[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap)
            for i in range(3)
        ]
        self.images2 = [
            self.ax2[i].imshow(self.channel_data2[i], interpolation='bicubic', norm=self.norm2, cmap=self.cmap)
            for i in range(3)
        ]
        self.images3 = [
            self.ax3[i].imshow(self.channel_data3[i], interpolation='nearest', norm=self.norm3, cmap=self.cmap_BWR)
            for i in range(3)
        ]

        # Remove axis from each plot and set facecolor
        for ax in self.ax1 + self.ax2 + self.ax3:
            ax.set_facecolor('black')
            ax.tick_params(axis='both', colors='white')
            ax.spines['bottom'].set_color('white')
            ax.spines['top'].set_color('white')
            ax.spines['right'].set_color('white')
            ax.spines['left'].set_color('white')
            ax.axis('off')

        # Create colorbars for the first three plots using the fourth subplot
        self.cbar1 = self.fig1.colorbar(self.images1[-1], cax=self.cbar_ax1)
        self.cbar1.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
        self.cbar1.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
        self.cbar1.outline.set_edgecolor('white')

        self.cbar2 = self.fig2.colorbar(self.images2[-1], cax=self.cbar_ax2)
        self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
        self.cbar2.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
        self.cbar2.outline.set_edgecolor('white')

        self.cbar3 = self.fig3.colorbar(self.images3[-1], cax=self.cbar_ax3)
        self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
        self.cbar3.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
        self.cbar3.outline.set_edgecolor('white')

        # Embed the figures in the Tk window using grid
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=main_frame)
        self.canvas_widget1 = self.canvas1.get_tk_widget()
        self.canvas_widget1.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=main_frame)
        self.canvas_widget2 = self.canvas2.get_tk_widget()
        self.canvas_widget2.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=main_frame)
        self.canvas_widget3 = self.canvas3.get_tk_widget()
        self.canvas_widget3.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

        # Frame for the sliders
        sliders_frame = ttk.Frame(main_frame, style="TFrame")
        sliders_frame.grid(row=0, column=2, rowspan=3, sticky="ns", padx=10, pady=10)
        sliders_frame.grid_rowconfigure((0, 1), weight=1)

        # Create a vertical slider for the upper limit adjustment (Row 1 and Row 2)
        # Existing slider for Row 1
        self.slider_vmax = ttk.Scale(
            sliders_frame,
            from_=10,
            to=0.01,
            orient='vertical',
            command=self.update_vmax,
            style="TScale"
        )
        self.slider_vmax.set(10)
        ttk.Label(sliders_frame, text="Övre gräns BP", background="black", foreground="white").pack(pady=(0, 5))
        self.slider_vmax.pack(expand=True, fill=tk.Y, pady=(0, 10))

        # New slider for Row 2
        self.slider_vmax2 = ttk.Scale(
            sliders_frame,
            from_=5,
            to=0.01,
            orient='vertical',
            command=self.update_vmax2,  # Callback for Row 2
            style="TScale"
        )
        self.slider_vmax2.set(5)
        ttk.Label(sliders_frame, text="Övre gräns R_I", background="black", foreground="white").pack(pady=(0, 5))
        self.slider_vmax2.pack(expand=True, fill=tk.Y, pady=(0, 10))

        # Create frame for the first row controls
        row1_controls = ttk.Frame(main_frame, style="TFrame")
        row1_controls.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

        # Dropdown menu to select the dataset for the first row
        self.plot_var1 = tk.StringVar()
        self.plot_dropdown1 = ttk.Combobox(
            row1_controls,
            textvariable=self.plot_var1,
            state='readonly',
            width=25,
            style="TCombobox"
        )
        self.plot_dropdown1['values'] = (
            "BP (MNI space)", "BP (pat space)"
        )
        self.plot_dropdown1.current(0)
        self.plot_dropdown1.grid(row=0, column=0, padx=5, pady=5)

        # Button to show the first row large
        self.show_large_button1 = ttk.Button(
            row1_controls,
            text="Visa stort",
            command=lambda: self.show_large_image(self.ax1, self.cbar1),
            style="TButton"
        )
        self.show_large_button1.grid(row=1, column=0, padx=5, pady=5)

        # Create frame for the second row controls
        row2_controls = ttk.Frame(main_frame, style="TFrame")
        row2_controls.grid(row=1, column=0, sticky="ns", padx=5, pady=5)

        # Dropdown menu to select the dataset for the second row
        self.plot_var2 = tk.StringVar()
        self.plot_dropdown2 = ttk.Combobox(
            row2_controls,
            textvariable=self.plot_var2,
            state='readonly',
            width=25,
            style="TCombobox"
        )
        self.plot_dropdown2['values'] = ('R_I (MNI space)', 'R_I (pat space)')
        self.plot_dropdown2.current(0)
        self.plot_dropdown2.grid(row=0, column=0, padx=5, pady=5)

        # Button to show the second row large
        self.show_large_button2 = ttk.Button(
            row2_controls,
            text="Visa stort",
            command=lambda: self.show_large_image(self.ax2, self.cbar2),
            style="TButton"
        )
        self.show_large_button2.grid(row=1, column=0, padx=5, pady=5)

        # Create frame for the third row controls
        row3_controls = ttk.Frame(main_frame, style="TFrame")
        row3_controls.grid(row=2, column=0, sticky="ns", padx=5, pady=5)

        # Dropdown menu to select the dataset for the third row
        self.plot_var3 = tk.StringVar()
        self.plot_dropdown3 = ttk.Combobox(
            row3_controls,
            textvariable=self.plot_var3,
            state='readonly',
            width=25,
            style="TCombobox"
        )
        self.plot_dropdown3['values'] = ('Z-score (R_I)',)
        self.plot_dropdown3.current(0)
        self.plot_dropdown3.grid(row=0, column=0, padx=5, pady=5)

        # Button to show the third row large
        self.show_large_button3 = ttk.Button(
            row3_controls,
            text="Visa stort",
            command=lambda: self.show_large_image(self.ax3, self.cbar3),
            style="TButton"
        )
        self.show_large_button3.grid(row=1, column=0, padx=5, pady=5)

        # Configure grid to expand properly within main_frame
        for i in range(3):
            main_frame.grid_rowconfigure(i, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)  # Column for figures
        main_frame.grid_columnconfigure(0, weight=0)  # Column for controls
        main_frame.grid_columnconfigure(2, weight=0)  # Column for sliders

        # Remove fixed figure sizes and allow them to fit the grid
        self.fig1.tight_layout()
        self.fig2.tight_layout()
        self.fig3.tight_layout()
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()

        # Bind dropdown change events
        self.plot_dropdown1.bind('<<ComboboxSelected>>', self.change_first_row)
        self.plot_dropdown2.bind('<<ComboboxSelected>>', self.change_second_row)
        self.plot_dropdown3.bind('<<ComboboxSelected>>', self.change_third_row)

        # Bottom frame for buttons
        bottom_frame = ttk.Frame(self, style="TFrame")
        bottom_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        bottom_frame.grid_columnconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)
        bottom_frame.grid_columnconfigure(2, weight=1)

        # Create a subframe to center the buttons and restrict their maximum width
        buttons_subframe = ttk.Frame(bottom_frame, style="TFrame")
        buttons_subframe.grid(row=0, column=0, columnspan=3, sticky="n")
        buttons_subframe.grid_columnconfigure((0, 1, 2), weight=1)

        # Create buttons for the buttons_subframe using grid
        self.button_left = ttk.Button(
            buttons_subframe,
            text="Spara som .nii",
            command=self.left_button_action,
            style="TButton",
            width=15  # Set a fixed width for consistency
        )
        self.button_left.grid(row=0, column=0, padx=20, pady=5, sticky="ew")

        self.button_middle = ttk.Button(
            buttons_subframe,
            text="Spara som dicom",
            command=self.middle_button_action,
            style="TButton",
            width=15  # Set a fixed width for consistency
        )
        self.button_middle.grid(row=0, column=1, padx=20, pady=5, sticky="ew")

        self.button_right = ttk.Button(
            buttons_subframe,
            text="Ny patient",
            command=self.right_button_action,
            style="TButton",
            width=15  # Set a fixed width for consistency
        )
        self.button_right.grid(row=0, column=2, padx=20, pady=5, sticky="ew")

        # Bind the window's configure event for dynamic resizing
        self.bind("<Configure>", self.on_resize)

        # Add Window Management Commands
        self.deiconify()           # Ensure the window is not minimized or hidden
        self.lift()                # Bring the window to the top
        self.focus_force()         # Focus on the App window
        self.grab_set()            # Make the App window modal (optional but recommended)
        self.update_idletasks()    # Process any pending idle tasks
        self.update()              # Force an update to render all widgets

        # Release the grab to make the window interactive
        self.grab_release()

    def on_resize(self, event):
        """Handle the window resize event to adjust figure sizes dynamically."""
        if self.resizing:
            return  # Prevent recursive resizing
        self.resizing = True

        try:
            # Define a helper function to resize a figure based on its container's size
            def resize_figure(canvas, figure):
                container = canvas.get_tk_widget()
                width = container.winfo_width()
                height = container.winfo_height()
                if width < 10 or height < 10:
                    return  # Avoid too small sizes
                dpi = figure.get_dpi()
                figure.set_size_inches(width / dpi, height / dpi)
                figure.tight_layout()
                canvas.draw()

            # Resize each figure
            resize_figure(self.canvas1, self.fig1)
            resize_figure(self.canvas2, self.fig2)
            resize_figure(self.canvas3, self.fig3)

        finally:
            self.resizing = False

    def on_close(self):
        """Handle the window close event."""
        print("App window is closing.")
        if self.button_var:
            self.button_var.set("Closed")  # Optionally set a value indicating closure
        self.destroy()
        if self.master:
            self.master.quit()  # Ensure the application exits when App window is closed

    def left_button_action(self):
        """Action for the left button."""
        from Save_as_nifyt_dicom import save_as_nifti
        array1=np.rot90(np.rot90(np.transpose(np.rot90(np.rot90(self.data1, axes=(1,2)), axes=(1,2)), (1,0,2))))
        array2=np.rot90(np.rot90(np.transpose(np.rot90(np.rot90(self.data2, axes=(1,2)), axes=(1,2)), (1,0,2))))
        array3=np.rot90(np.rot90(np.transpose(np.rot90(np.rot90(self.data3, axes=(1,2)), axes=(1,2)), (1,0,2))))

        affine_matrix = np.eye(4)
        arrays=[array1, array2]
        filenames=['BP.nii', 'R_I.nii']
        save_as_nifti(arrays, filenames, affine=affine_matrix)
        # if self.button_var:
        #     self.button_var.set("Left")
        # self.destroy()

    def middle_button_action(self):
        """Action for the middle button."""
        from Save_as_nifyt_dicom import save_as_dicom
        arrays=[self.data1, self.data2]
        output_dirs=['dicom BP', 'dicom R_I']
        save_as_dicom(
                arrays=arrays,
                output_dirs=output_dirs,
                patient_id='Patient_001',
                # series_instance_uid=series_instance_uid,  # Optional
                # study_instance_uid='1.2.840.113619.2.55.3.604688123.12345.1607771234.467',  # Optional
                # sop_instance_uid_prefix='1.2.840.113619.2.55.3.604688123.12345.1607771234'
            )

    def right_button_action(self):
        """Action for the right button."""
        if self.button_var:
            self.button_var.set("Right")
        self.destroy()

    def change_first_row(self, event):
        """Change the plot based on the selection from the first dropdown menu."""
        selection = self.plot_var1.get()
        print(f"First row selection changed to: {selection}")
        if selection == "BP (MNI space)":
            for i in range(3):
                self.images1[i].set_data(self.channel_data1[i])
        elif selection == "BP (pat space)":
            for i in range(3):
                self.images1[i].set_data(self.channel_data5[i])

        self.canvas1.draw()

    def change_second_row(self, event):
        """Change the plot based on the selection from the second dropdown menu."""
        selection = self.plot_var2.get()
        print(f"Second row selection changed to: {selection}")
        if selection == 'R_I (MNI space)':
            for i in range(3):
                self.images2[i].set_data(self.channel_data2[i])
                self.images2[i].set_cmap(self.cmap)
                self.images2[i].set_norm(self.norm2)  # Use self.norm2
            self.cbar2.update_normal(self.images2[-1])
            self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
        elif selection == 'R_I (pat space)':
            for i in range(3):
                self.images2[i].set_data(self.channel_data6[i])
                self.images2[i].set_cmap(self.cmap)
                self.images2[i].set_norm(self.norm2)  # Use self.norm2
            self.cbar2.update_normal(self.images2[-1])
            self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
        self.canvas2.draw()

    def change_third_row(self, event):
        """Change the plot based on the selection from the third dropdown menu."""
        selection = self.plot_var3.get()
        print(f"Third row selection changed to: {selection}")
        if selection == 'Z-score (R_I)':
            for i in range(3):
                self.images3[i].set_data(self.channel_data3[i])
                self.images3[i].set_cmap(self.cmap_BWR)
                self.images3[i].set_norm(self.norm3)
            self.cbar3.update_normal(self.images3[-1])
            self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
        self.canvas3.draw()

    def update_vmax(self, value):
        """Adjust the colormap normalization based on the upper limit slider."""
        vmax = float(value)
        print(f"Updating vmax to: {vmax} for Row 1")
        self.norm.vmax = vmax
        self.update_plots()

    def update_vmax2(self, value):
        """Adjust the colormap normalization based on the upper limit slider for Row 2."""
        vmax = float(value)
        print(f"Updating vmax to: {vmax} for Row 2")
        self.norm2.vmax = vmax
        self.update_plots()

    def update_plots(self):
        """Update the normalization across plots that respond to the slider."""
        print("Updating plots with new normalization.")
        # Update images that use self.norm (Row 1)
        for img in self.images1:
            img.set_norm(self.norm)
        # Update images that use self.norm2 (Row 2)
        for img in self.images2:
            img.set_norm(self.norm2)
        # Update colorbars
        self.cbar1.update_normal(self.images1[-1])
        self.cbar2.update_normal(self.images2[-1])
        self.canvas1.draw()
        self.canvas2.draw()
        # Update SSP images if applicable
        # Since Row 4 is removed, no need to update it

    def show_large_image(self, axes, colorbar=None):
        """Open a new window to display a larger version of the images in the selected row with a colorbar (if provided)."""
        print("Opening large image window...")
        # Create a new window for displaying the large images
        large_image_window = tk.Toplevel(self)
        large_image_window.title("Large Images")
        large_image_window.configure(bg="black")
        fig = Figure(facecolor='black')

        # Adjust GridSpec depending on whether we have a colorbar
        if colorbar:
            gs = GridSpec(1, len(axes) + 1, width_ratios=[1] * len(axes) + [0.02], figure=fig)  # Reduced colorbar ratio
        else:
            gs = GridSpec(1, len(axes), width_ratios=[1] * len(axes), figure=fig)

        # Plot each image in the new figure
        large_axes = []
        for i, axis in enumerate(axes):
            # Create a subplot for each image
            ax = fig.add_subplot(gs[0, i], facecolor='black')

            # Extract the data and norm from the corresponding smaller plot
            img_data = axis.images[0].get_array()
            norm = axis.images[0].norm
            cmap = axis.images[0].get_cmap()

            # Display the data in the large subplot
            im = ax.imshow(img_data, cmap=cmap, norm=norm, interpolation='nearest')
            ax.axis('off')

            large_axes.append(im)

        # Add the colorbar to the figure if provided
        if colorbar:
            cbar_ax = fig.add_subplot(gs[0, len(axes)])
            cbar = fig.colorbar(large_axes[-1], cax=cbar_ax, orientation='vertical')
            cbar.set_label(colorbar.ax.get_ylabel(), rotation=270, labelpad=15, color='white')

            # Set colorbar properties to match the theme
            cbar.ax.yaxis.set_tick_params(color='white')
            cbar.outline.set_edgecolor('white')
            cbar.ax.yaxis.set_tick_params(labelcolor='white')
            cbar.ax.tick_params(labelsize=14, colors='white')

        # Create a canvas to hold the figure and embed it in the new window
        canvas = FigureCanvasTkAgg(fig, master=large_image_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Adjust the layout and draw the canvas
        fig.tight_layout()
        canvas.draw()


def open_app_window_park(initial_window, button_var,
                         BP_MNI, R_I_MNI, Z_brain, z_min, z_med, z_max):
    """
    Hides the initial_window and opens the App window as a new top-level window.

    Args:
        initial_window (tk.Tk or tk.Toplevel): The window to be hidden.
        button_var (tk.StringVar): Variable to capture which button is pressed.

    Returns:
        App: An instance of the App window.
    """
    print("Opening App window...")
    initial_window.withdraw()  # Hide the initial window instead of destroying it
    print("Initial window hidden.")

    # Create the App window as a Toplevel instance, passing the button_var
    app = App(BP_MNI, R_I_MNI, Z_brain, z_min, z_med, z_max,
              master=initial_window, button_var=button_var)
    print("App window created.")

    return app


# Example usage:
if __name__ == "__main__":
    # Initialize dummy data if files are not found
    try:
        BP_MNI = np.load("BP.npy")
        R_I_MNI = np.load("R_I.npy")
        Z_brain = np.load("z_score_R_I.npy")
    except FileNotFoundError as e:
        print(f"Required data file not found: {e}")
        # Optionally, create dummy data for testing
        BP_MNI = np.random.rand(100, 100, 100)
        R_I_MNI = np.random.rand(100, 100, 100)
        Z_brain = np.random.rand(100, 100, 100)

    z_min, z_med, z_max = 25, 34, 44
    root = tk.Tk()
    root.geometry("1200x800")  # Set a default size
    root.title("Initial Window")  # Optional: Set a title for the initial window

    button_pressed = tk.StringVar()
    open_app_window_park(root, button_pressed, BP_MNI, R_I_MNI, Z_brain, z_min, z_med, z_max)
    root.wait_variable(button_pressed)

    # Retrieve the value set by the button
    response = button_pressed.get()
    print(f"Button pressed: {response}")
    root.destroy()
    root.mainloop()
