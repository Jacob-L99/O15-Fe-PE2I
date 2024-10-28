# # # # import matplotlib
# # # # cdict = {'red': ((0.0, 0.0, 0.0),
# # # #                   (0.1, 0.5, 0.5),
# # # #                   (0.2, 0.0, 0.0),
# # # #                   (0.4, 0.2, 0.2),
# # # #                   (0.6, 0.0, 0.0),
# # # #                   (0.8, 1.0, 1.0),
# # # #                   (1.0, 1.0, 1.0)),
# # # #         'green':((0.0, 0.0, 0.0),
# # # #                   (0.1, 0.0, 0.0),
# # # #                   (0.2, 0.0, 0.0),
# # # #                   (0.4, 1.0, 1.0),
# # # #                   (0.6, 1.0, 1.0),
# # # #                   (0.8, 1.0, 1.0),
# # # #                   (1.0, 0.0, 0.0)),
# # # #         'blue': ((0.0, 0.0, 0.0),
# # # #                   (0.1, 0.5, 0.5),
# # # #                   (0.2, 1.0, 1.0),
# # # #                   (0.4, 1.0, 1.0),
# # # #                   (0.6, 0.0, 0.0),
# # # #                   (0.8, 0.0, 0.0),
# # # #                   (1.0, 0.0, 0.0))}

# # # # my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)


# # # # original_screen_width = 1920  # Set this to your screen width
# # # # original_screen_height = 1080  # Set this to your screen height
# # # # scale_factor = 1.0  # Adjust as necessary

# # # # import tkinter as tk
# # # # from tkinter import ttk
# # # # from tkinter import messagebox
# # # # from matplotlib.figure import Figure
# # # # from matplotlib.gridspec import GridSpec
# # # # from matplotlib.colors import Normalize
# # # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # # import numpy as np


# # # # class App(tk.Tk):
# # # #     def __init__(self):
# # # #         super().__init__()
# # # #         self.title("Adjust Colormap Scale")
# # # #         self.configure(bg="black")

# # # #         # Style configuration for dark theme
# # # #         style = ttk.Style()
# # # #         style.theme_use("clam")
# # # #         style.configure("TButton", background="grey", foreground="white")
# # # #         style.configure("TFrame", background="black")
# # # #         style.configure("TLabel", background="black", foreground="white")
# # # #         style.configure("TCombobox", background="grey", foreground="white", fieldbackground="grey")
# # # #         style.configure("TScale", background="black", troughcolor="grey", sliderlength=30)
        
# # # #         # Main frame to hold canvas and sliders
# # # #         main_frame = ttk.Frame(self, style="TFrame")
# # # #         main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# # # #         # Create four matplotlib figures, each with six subplots in a single row
# # # #         self.fig1 = Figure(figsize=(5.6, 2), facecolor='black')
# # # #         gs1 = GridSpec(1, 7, width_ratios=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.015])
# # # #         self.ax1 = [self.fig1.add_subplot(gs1[0, i], facecolor='black') for i in range(6)]
# # # #         self.cbar_ax1 = self.fig1.add_subplot(gs1[0, 6], facecolor='black')

# # # #         self.fig2 = Figure(figsize=(5.6, 2), facecolor='black')
# # # #         gs2 = GridSpec(1, 7, width_ratios=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.015])
# # # #         self.ax2 = [self.fig2.add_subplot(gs2[0, i], facecolor='black') for i in range(6)]
# # # #         self.cbar_ax2 = self.fig2.add_subplot(gs2[0, 6], facecolor='black')

# # # #         self.fig3 = Figure(figsize=(5.6, 2), facecolor='black')
# # # #         gs3 = GridSpec(1, 7, width_ratios=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.015])
# # # #         self.ax3 = [self.fig3.add_subplot(gs3[0, i], facecolor='black') for i in range(6)]
# # # #         self.cbar_ax3 = self.fig3.add_subplot(gs3[0, 6], facecolor='black')

# # # #         self.fig4 = Figure(figsize=(5.6, 2), facecolor='black')
# # # #         gs4 = GridSpec(1, 7, width_ratios=[0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.015])
# # # #         self.ax4 = [self.fig4.add_subplot(gs4[0, i], facecolor='black') for i in range(6)]
# # # #         self.cbar_ax4 = self.fig4.add_subplot(gs4[0, 6], facecolor='black')

# # # #         # Load or generate test datasets
# # # #         self.data1 = np.rot90(np.load("K_1_test.npy"))
# # # #         self.data2 = np.rot90(np.load("K_2_test.npy"))
# # # #         self.data3 = np.rot90(np.load("K_1_test_2.npy"))
# # # #         self.data4 = np.rot90(np.load("K_2_test_2.npy"))
# # # #         self.data5 = np.rot90(np.load("V_T.npy"))

# # # #         # Select specific channels to display
# # # #         slices = [28, 42, 56, 70, 84, 98]
# # # #         self.channel_data1 = [self.data1[..., i] for i in slices]
# # # #         self.channel_data2 = [self.data2[..., i] for i in slices]
# # # #         self.channel_data3 = [self.data3[..., i] for i in slices]
# # # #         self.channel_data4 = [self.data4[..., i] for i in slices]
# # # #         self.channel_data5 = [self.data5[..., i] for i in slices]

# # # #         # Initialize normalization object
# # # #         self.norm = Normalize(vmin=0, vmax=2)

# # # #         # Define colormap
# # # #         self.cmap = my_cmap  # Replace with your colormap

# # # #         # Initialize image plots with the first dataset as default
# # # #         self.images1 = [
# # # #             self.ax1[i].imshow(self.channel_data1[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
# # # #             for i in range(6)
# # # #         ] 
# # # #         self.images2 = [
# # # #             self.ax2[i].imshow(self.channel_data2[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
# # # #             for i in range(6)
# # # #         ] 
# # # #         self.images3 = [
# # # #             self.ax3[i].imshow(self.channel_data3[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
# # # #             for i in range(6)
# # # #         ] 
# # # #         self.images4 = [
# # # #             self.ax4[i].imshow(self.channel_data4[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
# # # #             for i in range(6)
# # # #         ] 

# # # #         # Remove axis from each plot
# # # #         for ax in self.ax1 + self.ax2 + self.ax3 + self.ax4:
# # # #             ax.set_facecolor('black')
# # # #             ax.tick_params(axis='both', colors='white')
# # # #             ax.spines['bottom'].set_color('white')
# # # #             ax.spines['top'].set_color('white')
# # # #             ax.spines['right'].set_color('white')
# # # #             ax.spines['left'].set_color('white')
# # # #             ax.axis('off')

# # # #         # Create colorbars for all plots using the seventh subplot
# # # #         self.cbar1 = self.fig1.colorbar(self.images1[-1], cax=self.cbar_ax1)
# # # #         self.cbar1.set_label('ml/min/g', rotation=270, labelpad=15)
# # # #         self.cbar1.ax.yaxis.set_tick_params(color='white')
# # # #         self.cbar1.outline.set_edgecolor('white')
# # # #         self.cbar1.ax.yaxis.set_tick_params(labelcolor='white')

# # # #         self.cbar2 = self.fig2.colorbar(self.images2[-1], cax=self.cbar_ax2)
# # # #         self.cbar2.set_label('ml/min/g', rotation=270, labelpad=15)
# # # #         self.cbar2.ax.yaxis.set_tick_params(color='white')
# # # #         self.cbar2.outline.set_edgecolor('white')
# # # #         self.cbar2.ax.yaxis.set_tick_params(labelcolor='white')

# # # #         self.cbar3 = self.fig3.colorbar(self.images3[-1], cax=self.cbar_ax3)
# # # #         self.cbar3.set_label('ml/min/g', rotation=270, labelpad=15)
# # # #         self.cbar3.ax.yaxis.set_tick_params(color='white')
# # # #         self.cbar3.outline.set_edgecolor('white')
# # # #         self.cbar3.ax.yaxis.set_tick_params(labelcolor='white')

# # # #         self.cbar4 = self.fig4.colorbar(self.images4[-1], cax=self.cbar_ax4)
# # # #         self.cbar4.set_label('ml/min/g', rotation=270, labelpad=15)
# # # #         self.cbar4.ax.yaxis.set_tick_params(color='white')
# # # #         self.cbar4.outline.set_edgecolor('white')
# # # #         self.cbar4.ax.yaxis.set_tick_params(labelcolor='white')

# # # #         # Embed the figures in the Tk window
# # # #         self.canvas1 = FigureCanvasTkAgg(self.fig1, master=main_frame)
# # # #         self.canvas_widget1 = self.canvas1.get_tk_widget()
# # # #         self.canvas_widget1.grid(row=0, column=1, sticky="nsew")

# # # #         self.canvas2 = FigureCanvasTkAgg(self.fig2, master=main_frame)
# # # #         self.canvas_widget2 = self.canvas2.get_tk_widget()
# # # #         self.canvas_widget2.grid(row=1, column=1, sticky="nsew")

# # # #         self.canvas3 = FigureCanvasTkAgg(self.fig3, master=main_frame)
# # # #         self.canvas_widget3 = self.canvas3.get_tk_widget()
# # # #         self.canvas_widget3.grid(row=2, column=1, sticky="nsew")

# # # #         self.canvas4 = FigureCanvasTkAgg(self.fig4, master=main_frame)
# # # #         self.canvas_widget4 = self.canvas4.get_tk_widget()
# # # #         self.canvas_widget4.grid(row=3, column=1, sticky="nsew")

# # # #         # Frame for the sliders
# # # #         sliders_frame = ttk.Frame(main_frame, width=50, style="TFrame")
# # # #         sliders_frame.grid(row=0, column=2, rowspan=4, sticky="ns", padx=10, pady=100)

# # # #         # Create a vertical slider for the upper limit adjustment
# # # #         self.slider_vmax = ttk.Scale(sliders_frame, from_=2, to=0.01, orient='vertical', command=self.update_vmax, style="TScale")
# # # #         self.slider_vmax.set(2)
# # # #         ttk.Label(sliders_frame, text="Övre gräns", background="black", foreground="white").pack()
# # # #         self.slider_vmax.pack(expand=True, fill=tk.Y, pady=(0, 10))

# # # #         # Create frame for the first row controls
# # # #         row1_controls = ttk.Frame(main_frame, style="TFrame")
# # # #         row1_controls.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

# # # #         # Dropdown menu to select the dataset for the first row
# # # #         self.plot_var1 = tk.StringVar()
# # # #         self.plot_dropdown1 = ttk.Combobox(row1_controls, textvariable=self.plot_var1, state='readonly', width=15, style="TCombobox")
# # # #         self.plot_dropdown1['values'] = ("K1: Base line (mni space)", "K1: Base line (pat space)", "K1/K2: Base line (mni space)")
# # # #         self.plot_dropdown1.current(0)
# # # #         self.plot_dropdown1.grid(row=0, column=0, padx=5, pady=5)

# # # #         # Button to show the first row large
# # # #         self.show_large_button1 = ttk.Button(row1_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax1, self.cbar1), style="TButton")
# # # #         self.show_large_button1.grid(row=1, column=0, padx=5, pady=5)

# # # #         # Create frame for the second row controls
# # # #         row2_controls = ttk.Frame(main_frame, style="TFrame")
# # # #         row2_controls.grid(row=1, column=0, sticky="ns", padx=5, pady=5)

# # # #         # Dropdown menu to select the dataset for the second row
# # # #         self.plot_var2 = tk.StringVar()
# # # #         self.plot_dropdown2 = ttk.Combobox(row2_controls, textvariable=self.plot_var2, state='readonly', width=15, style="TCombobox")
# # # #         self.plot_dropdown2['values'] = ('K2 (1)', 'K2 (2)')
# # # #         self.plot_dropdown2.current(0)
# # # #         self.plot_dropdown2.grid(row=0, column=0, padx=5, pady=5)

# # # #         # Button to show the second row large
# # # #         self.show_large_button2 = ttk.Button(row2_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax2, self.cbar2), style="TButton")
# # # #         self.show_large_button2.grid(row=1, column=0, padx=5, pady=5)

# # # #         # Create frame for the third row controls
# # # #         row3_controls = ttk.Frame(main_frame, style="TFrame")
# # # #         row3_controls.grid(row=2, column=0, sticky="ns", padx=5, pady=5)

# # # #         # Dropdown menu to select the dataset for the third row
# # # #         self.plot_var3 = tk.StringVar()
# # # #         self.plot_dropdown3 = ttk.Combobox(row3_controls, textvariable=self.plot_var3, state='readonly', width=15, style="TCombobox")
# # # #         self.plot_dropdown3['values'] = ('3_wat1', '3_wat2')
# # # #         self.plot_dropdown3.current(0)
# # # #         self.plot_dropdown3.grid(row=0, column=0, padx=5, pady=5)

# # # #         # Button to show the third row large
# # # #         self.show_large_button3 = ttk.Button(row3_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax3, self.cbar3), style="TButton")
# # # #         self.show_large_button3.grid(row=1, column=0, padx=5, pady=5)

# # # #         # Create frame for the fourth row controls
# # # #         row4_controls = ttk.Frame(main_frame, style="TFrame")
# # # #         row4_controls.grid(row=3, column=0, sticky="ns", padx=5, pady=5)

# # # #         # Dropdown menu to select the dataset for the fourth row
# # # #         self.plot_var4 = tk.StringVar()
# # # #         self.plot_dropdown4 = ttk.Combobox(row4_controls, textvariable=self.plot_var4, state='readonly', width=15, style="TCombobox")
# # # #         self.plot_dropdown4['values'] = ('4_wat1', '4_2_wat1')
# # # #         self.plot_dropdown4.current(0)
# # # #         self.plot_dropdown4.grid(row=0, column=0, padx=5, pady=5)

# # # #         # Button to show the fourth row large
# # # #         self.show_large_button4 = ttk.Button(row4_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax4, self.cbar4), style="TButton")
# # # #         self.show_large_button4.grid(row=1, column=0, padx=5, pady=5)

# # # #         # Configure grid to expand properly
# # # #         main_frame.grid_columnconfigure(1, weight=1)
# # # #         main_frame.grid_rowconfigure(0, weight=1)
# # # #         main_frame.grid_rowconfigure(1, weight=1)
# # # #         main_frame.grid_rowconfigure(2, weight=1)
# # # #         main_frame.grid_rowconfigure(3, weight=1)

# # # #         self.fig1.tight_layout()
# # # #         self.fig2.tight_layout()
# # # #         self.fig3.tight_layout()
# # # #         self.fig4.tight_layout()
# # # #         self.canvas1.draw()
# # # #         self.canvas2.draw()
# # # #         self.canvas3.draw()
# # # #         self.canvas4.draw()

# # # #         # Bind dropdown change events
# # # #         self.plot_dropdown1.bind('<<ComboboxSelected>>', self.change_first_row)
# # # #         self.plot_dropdown2.bind('<<ComboboxSelected>>', self.change_second_row)
# # # #         self.plot_dropdown3.bind('<<ComboboxSelected>>', self.change_third_row)
# # # #         self.plot_dropdown4.bind('<<ComboboxSelected>>', self.change_fourth_row)

# # # #         # Bottom frame for buttons
# # # #         bottom_frame = ttk.Frame(self, style="TFrame")
# # # #         bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# # # #         # Inner frame to center buttons
# # # #         button_frame = ttk.Frame(bottom_frame, style="TFrame")
# # # #         button_frame.pack(side=tk.TOP, expand=True)

# # # #         # Create buttons for the button frame
# # # #         self.button_left = ttk.Button(button_frame, text="Left Button", command=self.left_button_action, style="TButton")
# # # #         self.button_left.pack(side=tk.LEFT, padx=20)

# # # #         self.button_middle = ttk.Button(button_frame, text="Middle Button", command=self.middle_button_action, style="TButton")
# # # #         self.button_middle.pack(side=tk.LEFT, padx=20)

# # # #         self.button_right = ttk.Button(button_frame, text="Right Button", command=self.right_button_action, style="TButton")
# # # #         self.button_right.pack(side=tk.LEFT, padx=20)

# # # #     def change_first_row(self, event):
# # # #         """Change the plot based on the selection from the first dropdown menu."""
# # # #         selection = self.plot_var1.get()
# # # #         if selection == "K1: Base line (mni space)":
# # # #             for i in range(6):
# # # #                 self.images1[i].set_data(self.channel_data1[i])
# # # #         elif selection == "K1: Base line (pat space)":
# # # #             for i in range(6):
# # # #                 self.images1[i].set_data(self.channel_data3[i])
# # # #         elif selection == "K1/K2: Base line (mni space)":
# # # #             for i in range(6):
# # # #                 self.images1[i].set_data(self.channel_data5[i])
# # # #         self.canvas1.draw()

# # # #     def change_second_row(self, event):
# # # #         """Change the plot based on the selection from the second dropdown menu."""
# # # #         selection = self.plot_var2.get()
# # # #         if selection == 'K2 (1)':
# # # #             for i in range(6):
# # # #                 self.images2[i].set_data(self.channel_data2[i])
# # # #         else:
# # # #             for i in range(6):
# # # #                 self.images2[i].set_data(self.channel_data4[i])
# # # #         self.canvas2.draw()

# # # #     def change_third_row(self, event):
# # # #         """Change the plot based on the selection from the third dropdown menu."""
# # # #         selection = self.plot_var3.get()
# # # #         if selection == '3_wat1':
# # # #             for i in range(6):
# # # #                 self.images3[i].set_data(self.channel_data3[i])
# # # #         else:
# # # #             for i in range(6):
# # # #                 self.images3[i].set_data(self.channel_data4[i])
# # # #         self.canvas3.draw()

# # # #     def change_fourth_row(self, event):
# # # #         """Change the plot based on the selection from the fourth dropdown menu."""
# # # #         selection = self.plot_var4.get()
# # # #         if selection == '4_wat1':
# # # #             for i in range(6):
# # # #                 self.images4[i].set_data(self.channel_data4[i])
# # # #         else:
# # # #             for i in range(6):
# # # #                 self.images4[i].set_data(self.channel_data5[i])
# # # #         self.canvas4.draw()

# # # #     def update_vmax(self, value):
# # # #         """Adjust the colormap normalization based on the upper limit slider."""
# # # #         self.norm.vmax = float(value)
# # # #         self.update_plots()

# # # #     def update_plots(self):
# # # #         """Update the normalization across all plots."""
# # # #         for img in self.images1 + self.images2 + self.images3 + self.images4:
# # # #             img.set_norm(self.norm)
# # # #         for colorbar in [self.cbar1, self.cbar2, self.cbar3, self.cbar4]:
# # # #             colorbar.update_normal(img)
# # # #         self.canvas1.draw()
# # # #         self.canvas2.draw()
# # # #         self.canvas3.draw()
# # # #         self.canvas4.draw()

# # # #     def show_large_image(self, axes, colorbar=None):
# # # #         """Open a new window to display a larger version of the images in the selected row with a colorbar (if provided)."""
# # # #         # Create a new window for displaying the large images
# # # #         large_image_window = tk.Toplevel(self)
# # # #         large_image_window.title("Large Images")
# # # #         fig = Figure(figsize=(16, 5), facecolor='black')
    
# # # #         # Adjust GridSpec depending on whether we have a colorbar
# # # #         if colorbar:
# # # #             gs = GridSpec(1, len(axes) + 1, width_ratios=[1] * len(axes) + [0.05])
# # # #         else:
# # # #             gs = GridSpec(1, len(axes), width_ratios=[1] * len(axes))
    
# # # #         # Plot each image in the new figure
# # # #         large_axes = []
# # # #         for i, axis in enumerate(axes):
# # # #             # Create a subplot for each image
# # # #             ax = fig.add_subplot(gs[0, i], facecolor='black')
            
# # # #             # Extract the data from the corresponding smaller plot
# # # #             img_data = axis.images[0].get_array()
            
# # # #             # Display the data in the large subplot
# # # #             im = ax.imshow(img_data, cmap=self.cmap, norm=self.norm, interpolation='bicubic')
# # # #             ax.axis('off')
            
# # # #             large_axes.append(im)
    
# # # #         # Add the colorbar to the figure if provided
# # # #         if colorbar:
# # # #             cbar_ax = fig.add_subplot(gs[0, len(axes)])
# # # #             cbar = fig.colorbar(large_axes[-1], cax=cbar_ax, orientation='vertical')
# # # #             cbar.set_label('ml/min/g', rotation=270, labelpad=15)
            
# # # #             # Set colorbar properties to match the theme
# # # #             cbar.ax.yaxis.set_tick_params(color='white')
# # # #             cbar.outline.set_edgecolor('white')
# # # #             cbar.ax.yaxis.set_tick_params(labelcolor='white')
    
# # # #         # Create a canvas to hold the figure and embed it in the new window
# # # #         canvas = FigureCanvasTkAgg(fig, master=large_image_window)
# # # #         canvas_widget = canvas.get_tk_widget()
# # # #         canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
# # # #         # Adjust the layout and draw the canvas
# # # #         fig.tight_layout()
# # # #         canvas.draw()



# # # #     def left_button_action(self):
# # # #         """Action for the left button."""
# # # #         messagebox.showinfo("Button Clicked", "Left Button was clicked")

# # # #     def middle_button_action(self):
# # # #         """Action for the middle button."""
# # # #         messagebox.showinfo("Button Clicked", "Middle Button was clicked")

# # # #     def right_button_action(self):
# # # #         """Action for the right button."""
# # # #         messagebox.showinfo("Button Clicked", "Right Button was clicked")

# # # # if __name__ == "__main__":
# # # #     app = App()
# # # #     app.mainloop()

# # import matplotlib
# # from matplotlib.colors import LinearSegmentedColormap
# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter import messagebox
# # from matplotlib.figure import Figure
# # from matplotlib.gridspec import GridSpec
# # from matplotlib.colors import Normalize
# # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # import numpy as np
# # import matplotlib.pyplot as plt

# # # Define the custom colormap
# # cdict = {'red': ((0.0, 0.0, 0.0),
# #                   (0.1, 0.5, 0.5),
# #                   (0.2, 0.0, 0.0),
# #                   (0.4, 0.2, 0.2),
# #                   (0.6, 0.0, 0.0),
# #                   (0.8, 1.0, 1.0),
# #                   (1.0, 1.0, 1.0)),
# #           'green': ((0.0, 0.0, 0.0),
# #                     (0.1, 0.0, 0.0),
# #                     (0.2, 0.0, 0.0),
# #                     (0.4, 1.0, 1.0),
# #                     (0.6, 1.0, 1.0),
# #                     (0.8, 1.0, 1.0),
# #                     (1.0, 0.0, 0.0)),
# #           'blue': ((0.0, 0.0, 0.0),
# #                   (0.1, 0.5, 0.5),
# #                   (0.2, 1.0, 1.0),
# #                   (0.4, 1.0, 1.0),
# #                   (0.6, 0.0, 0.0),
# #                   (0.8, 0.0, 0.0),
# #                   (1.0, 0.0, 0.0))}

# # my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', cdict, 256)

# # # Define the custom blue-white-red colormap
# # colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1, 1, 1), (1, 0, 0), (0.5, 0, 0)]
# # n_bins = 10
# # cmap_name = 'custom_blue_white_red'
# # custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# # def create_custom_figure(data_set, norm=None, figsize=(5.6, 2)):
# #     """Creates the custom figure using the provided data and returns it."""
# #     if data_set == 'SSP':
# #         # Load your 2D arrays
# #         first_values_yz_neg_x0 = np.rot90(np.rot90(np.rot90(np.load('first_values_yz_neg_x0.npy'))))
# #         first_values_yz_pos_x1 = np.flip(np.rot90(np.rot90(np.rot90(np.load('first_values_yz_pos_x1.npy')))), axis=1)
# #         first_values_yz_pos_x2 = np.rot90(np.rot90(np.rot90(np.load('first_values_yz_pos_x2.npy'))))
# #         first_values_yz_neg_x2 = np.flip(np.rot90(np.rot90(np.rot90(np.load('first_values_yz_neg_x2.npy')))), axis=1)
# #         first_values_xz_pos_y2 = np.rot90(np.rot90(np.rot90(np.load('first_values_xz_pos_y2.npy'))))
# #         first_values_xz_neg_y2 = np.rot90(np.rot90(np.rot90(np.load('first_values_xz_neg_y2.npy'))))
# #         data_list = [
# #             first_values_yz_neg_x0,
# #             first_values_yz_pos_x1,
# #             first_values_yz_pos_x2,
# #             first_values_yz_neg_x2,
# #             first_values_xz_pos_y2,
# #             first_values_xz_neg_y2
# #         ]

# #         # Create a figure with 1 row and 6 columns
# #         fig = Figure(figsize=figsize, facecolor='black')
# #         gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
# #         axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
# #         cbar_ax = fig.add_subplot(gs[0, 6])

# #         # Define the normalization if not provided
# #         if norm is None:
# #             norm = Normalize(vmin=0, vmax=2)

# #         # Plot each 2D array
# #         images = []
# #         for i, data in enumerate(data_list):
# #             ax = axs[i]
# #             im = ax.imshow(data, cmap=my_cmap, norm=norm, interpolation='bicubic')
# #             ax.axis('off')
# #             images.append(im)

# #         # Add a shared colorbar
# #         cbar = fig.colorbar(images[-1], cax=cbar_ax)
# #         cbar.set_label('Value', rotation=270, labelpad=15, color='white', fontsize=8)
# #         cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
# #         cbar.outline.set_edgecolor('white')

# #         # Adjust layout
# #         fig.tight_layout()

# #         return fig, images  # Return images for updating norm

# #     elif data_set == 'SSP Z-score':
# #         # Use the existing code (fig_get)
# #         last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6 = fig_get()
# #         all_figures = [last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6]

# #         # Create a new figure with 1 row and 6 columns
# #         fig = Figure(figsize=figsize, facecolor='black')
# #         gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
# #         axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
# #         cbar_ax = fig.add_subplot(gs[0, 6])

# #         # Loop over all the figures and plot them in subplots
# #         for i, figure in enumerate(all_figures):
# #             ax_new = axs[i]
# #             for ax_old in figure.axes:
# #                 for img in ax_old.images:
# #                     blended_image = img.get_array()
# #                     im = ax_new.imshow(blended_image, cmap=img.get_cmap(), alpha=img.get_alpha())
# #             ax_new.axis('off')

# #         # Add one shared colorbar for all subplots
# #         sm = plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=-5, vmax=5))
# #         cbar = fig.colorbar(sm, cax=cbar_ax, label='Z-score')
# #         cbar.ax.tick_params(labelsize=6, colors='white')
# #         cbar.set_label('Z-score', fontsize=8, color='white')
# #         cbar.outline.set_edgecolor('white')
# #         cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white')

# #         # Adjust layout
# #         fig.tight_layout()

# #         return fig, None  # No images to update norm

# #     else:
# #         # Handle other datasets if any
# #         pass

# # class App(tk.Tk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Adjust Colormap Scale")
# #         self.configure(bg="black")

# #         # Style configuration for dark theme
# #         style = ttk.Style()
# #         style.theme_use("clam")
# #         style.configure("TButton", background="grey", foreground="white")
# #         style.configure("TFrame", background="black")
# #         style.configure("TLabel", background="black", foreground="white")
# #         style.configure("TCombobox", background="grey", foreground="white", fieldbackground="grey")
# #         style.configure("TScale", background="black", troughcolor="grey", sliderlength=30)
        
# #         # Main frame to hold canvas and sliders
# #         main_frame = ttk.Frame(self, style="TFrame")
# #         main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# #         # Create three matplotlib figures, each with six subplots in a single row
# #         self.fig1 = Figure(figsize=(5.6, 2), facecolor='black')
# #         gs1 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig1)
# #         self.ax1 = [self.fig1.add_subplot(gs1[0, i]) for i in range(6)]
# #         self.cbar_ax1 = self.fig1.add_subplot(gs1[0, 6])

# #         self.fig2 = Figure(figsize=(5.6, 2), facecolor='black')
# #         gs2 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig2)
# #         self.ax2 = [self.fig2.add_subplot(gs2[0, i]) for i in range(6)]
# #         self.cbar_ax2 = self.fig2.add_subplot(gs2[0, 6])

# #         self.fig3 = Figure(figsize=(5.6, 2), facecolor='black')
# #         gs3 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig3)
# #         self.ax3 = [self.fig3.add_subplot(gs3[0, i]) for i in range(6)]
# #         self.cbar_ax3 = self.fig3.add_subplot(gs3[0, 6])

# #         # Initialize the fourth figure with datasets
# #         self.datasets_row4 = ['SSP', 'SSP Z-score']
# #         self.figures_row4 = {}
# #         self.images_row4 = {}

# #         # Create figures for all datasets
# #         self.norm_row4 = Normalize(vmin=0, vmax=2)
# #         for dataset_name in self.datasets_row4:
# #             fig, images = create_custom_figure(dataset_name, norm=self.norm_row4)
# #             self.figures_row4[dataset_name] = fig
# #             if images:
# #                 self.images_row4[dataset_name] = images  # Store images for updating norm

# #         # Set the default dataset
# #         self.current_dataset_row4 = 'SSP'  # Default dataset
# #         self.fig4 = self.figures_row4[self.current_dataset_row4]

# #         # Load or generate test datasets for the first three rows
# #         self.data1 = np.rot90(np.load("K_1_test.npy"))
# #         self.data2 = np.rot90(np.load("K_2_test.npy"))
# #         self.data3 = self.data1 / self.data2  # For the third row
# #         self.data4 = np.rot90(np.load("Z_brain.npy"))  # Z-score data
# #         self.data5 = np.rot90(np.load("K_1_test.npy"))
# #         self.data6 = np.rot90(np.load("K_2_test.npy"))

# #         # Select specific channels to display
# #         slices = [28, 42, 56, 70, 84, 98]
# #         self.channel_data1 = [self.data1[..., i] for i in slices]
# #         self.channel_data2 = [self.data2[..., i] for i in slices]
# #         self.channel_data3 = [self.data3[..., i] for i in slices]
# #         self.channel_data4 = [self.data4[..., i] for i in slices]
# #         self.channel_data5 = [self.data5[..., i] for i in slices]

# #         # Initialize normalization objects
# #         self.norm = Normalize(vmin=0, vmax=2)
# #         self.norm3 = Normalize(vmin=0, vmax=2)
# #         self.norm4 = Normalize(vmin=-5, vmax=5)  # For Z-score data

# #         # Define colormap
# #         self.cmap = my_cmap

# #         # Initialize image plots with the datasets
# #         self.images1 = [
# #             self.ax1[i].imshow(self.channel_data1[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
# #             for i in range(6)
# #         ] 
# #         self.images2 = [
# #             self.ax2[i].imshow(self.channel_data2[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
# #             for i in range(6)
# #         ] 
# #         self.images3 = [
# #             self.ax3[i].imshow(self.channel_data3[i], interpolation='nearest', norm=self.norm3, cmap='bwr') 
# #             for i in range(6)
# #         ] 

# #         # Remove axis from each plot
# #         for ax in self.ax1 + self.ax2 + self.ax3:
# #             ax.set_facecolor('black')
# #             ax.tick_params(axis='both', colors='white')
# #             ax.spines['bottom'].set_color('white')
# #             ax.spines['top'].set_color('white')
# #             ax.spines['right'].set_color('white')
# #             ax.spines['left'].set_color('white')
# #             ax.axis('off')

# #         # Create colorbars for the first three plots using the seventh subplot
# #         self.cbar1 = self.fig1.colorbar(self.images1[-1], cax=self.cbar_ax1)
# #         self.cbar1.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
# #         self.cbar1.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
# #         self.cbar1.outline.set_edgecolor('white')

# #         self.cbar2 = self.fig2.colorbar(self.images2[-1], cax=self.cbar_ax2)
# #         self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
# #         self.cbar2.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
# #         self.cbar2.outline.set_edgecolor('white')

# #         self.cbar3 = self.fig3.colorbar(self.images3[-1], cax=self.cbar_ax3)
# #         self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
# #         self.cbar3.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
# #         self.cbar3.outline.set_edgecolor('white')

# #         # Embed the figures in the Tk window
# #         self.canvas1 = FigureCanvasTkAgg(self.fig1, master=main_frame)
# #         self.canvas_widget1 = self.canvas1.get_tk_widget()
# #         self.canvas_widget1.grid(row=0, column=1, sticky="nsew")

# #         self.canvas2 = FigureCanvasTkAgg(self.fig2, master=main_frame)
# #         self.canvas_widget2 = self.canvas2.get_tk_widget()
# #         self.canvas_widget2.grid(row=1, column=1, sticky="nsew")

# #         self.canvas3 = FigureCanvasTkAgg(self.fig3, master=main_frame)
# #         self.canvas_widget3 = self.canvas3.get_tk_widget()
# #         self.canvas_widget3.grid(row=2, column=1, sticky="nsew")

# #         # For row 4, use the figure created based on the current dataset
# #         self.canvas4 = FigureCanvasTkAgg(self.fig4, master=main_frame)
# #         self.canvas_widget4 = self.canvas4.get_tk_widget()
# #         self.canvas_widget4.grid(row=3, column=1, sticky="nsew")

# #         # Frame for the sliders
# #         sliders_frame = ttk.Frame(main_frame, width=50, style="TFrame")
# #         sliders_frame.grid(row=0, column=2, rowspan=4, sticky="ns", padx=10, pady=100)

# #         # Create a vertical slider for the upper limit adjustment
# #         self.slider_vmax = ttk.Scale(sliders_frame, from_=2, to=0.01, orient='vertical', command=self.update_vmax, style="TScale")
# #         self.slider_vmax.set(2)
# #         ttk.Label(sliders_frame, text="Övre gräns", background="black", foreground="white").pack()
# #         self.slider_vmax.pack(expand=True, fill=tk.Y, pady=(0, 10))

# #         # Create frame for the first row controls
# #         row1_controls = ttk.Frame(main_frame, style="TFrame")
# #         row1_controls.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

# #         # Dropdown menu to select the dataset for the first row
# #         self.plot_var1 = tk.StringVar()
# #         self.plot_dropdown1 = ttk.Combobox(row1_controls, textvariable=self.plot_var1, state='readonly', width=25, style="TCombobox")
# #         self.plot_dropdown1['values'] = ("K1: Base line (mni space)", "K1: Base line (pat space)", "K1/K2: Base line (mni space)")
# #         self.plot_dropdown1.current(0)
# #         self.plot_dropdown1.grid(row=0, column=0, padx=5, pady=5)

# #         # Button to show the first row large
# #         self.show_large_button1 = ttk.Button(row1_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax1, self.cbar1), style="TButton")
# #         self.show_large_button1.grid(row=1, column=0, padx=5, pady=5)

# #         # Create frame for the second row controls
# #         row2_controls = ttk.Frame(main_frame, style="TFrame")
# #         row2_controls.grid(row=1, column=0, sticky="ns", padx=5, pady=5)

# #         # Dropdown menu to select the dataset for the second row
# #         self.plot_var2 = tk.StringVar()
# #         self.plot_dropdown2 = ttk.Combobox(row2_controls, textvariable=self.plot_var2, state='readonly', width=25, style="TCombobox")
# #         self.plot_dropdown2['values'] = ('K_2 (MNI space)', 'K_2 (pat space)')
# #         self.plot_dropdown2.current(0)
# #         self.plot_dropdown2.grid(row=0, column=0, padx=5, pady=5)

# #         # Button to show the second row large
# #         self.show_large_button2 = ttk.Button(row2_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax2, self.cbar2), style="TButton")
# #         self.show_large_button2.grid(row=1, column=0, padx=5, pady=5)

# #         # Create frame for the third row controls
# #         row3_controls = ttk.Frame(main_frame, style="TFrame")
# #         row3_controls.grid(row=2, column=0, sticky="ns", padx=5, pady=5)

# #         # Dropdown menu to select the dataset for the third row
# #         self.plot_var3 = tk.StringVar()
# #         self.plot_dropdown3 = ttk.Combobox(row3_controls, textvariable=self.plot_var3, state='readonly', width=25, style="TCombobox")
# #         self.plot_dropdown3['values'] = ('K_1/K_2', 'Z-score')
# #         self.plot_dropdown3.current(0)
# #         self.plot_dropdown3.grid(row=0, column=0, padx=5, pady=5)

# #         # Button to show the third row large
# #         self.show_large_button3 = ttk.Button(row3_controls, text="Visa stort", command=lambda: self.show_large_image(self.ax3, self.cbar3), style="TButton")
# #         self.show_large_button3.grid(row=1, column=0, padx=5, pady=5)

# #         # Create frame for the fourth row controls
# #         row4_controls = ttk.Frame(main_frame, style="TFrame")
# #         row4_controls.grid(row=3, column=0, sticky="ns", padx=5, pady=5)

# #         # Dropdown menu to select the dataset for the fourth row
# #         self.plot_var4 = tk.StringVar()
# #         self.plot_dropdown4 = ttk.Combobox(row4_controls, textvariable=self.plot_var4, state='readonly', width=25, style="TCombobox")
# #         self.plot_dropdown4['values'] = self.datasets_row4
# #         self.plot_dropdown4.current(0)
# #         self.plot_dropdown4.grid(row=0, column=0, padx=5, pady=5)

# #         # Button to show the fourth row large
# #         self.show_large_button4 = ttk.Button(row4_controls, text="Visa stort", command=lambda: self.show_large_image_fig4(), style="TButton")
# #         self.show_large_button4.grid(row=1, column=0, padx=5, pady=5)

# #         # Configure grid to expand properly
# #         main_frame.grid_columnconfigure(1, weight=1)
# #         main_frame.grid_rowconfigure(0, weight=1)
# #         main_frame.grid_rowconfigure(1, weight=1)
# #         main_frame.grid_rowconfigure(2, weight=1)
# #         main_frame.grid_rowconfigure(3, weight=1)

# #         self.fig1.tight_layout()
# #         self.fig2.tight_layout()
# #         self.fig3.tight_layout()
# #         self.fig4.tight_layout()
# #         self.canvas1.draw()
# #         self.canvas2.draw()
# #         self.canvas3.draw()
# #         self.canvas4.draw()

# #         # Bind dropdown change events
# #         self.plot_dropdown1.bind('<<ComboboxSelected>>', self.change_first_row)
# #         self.plot_dropdown2.bind('<<ComboboxSelected>>', self.change_second_row)
# #         self.plot_dropdown3.bind('<<ComboboxSelected>>', self.change_third_row)
# #         self.plot_dropdown4.bind('<<ComboboxSelected>>', self.change_fourth_row)

# #         # Bottom frame for buttons
# #         bottom_frame = ttk.Frame(self, style="TFrame")
# #         bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

# #         # Inner frame to center buttons
# #         button_frame = ttk.Frame(bottom_frame, style="TFrame")
# #         button_frame.pack(side=tk.TOP, expand=True)

# #         # Create buttons for the button frame
# #         self.button_left = ttk.Button(button_frame, text="Left Button", command=self.left_button_action, style="TButton")
# #         self.button_left.pack(side=tk.LEFT, padx=20)

# #         self.button_middle = ttk.Button(button_frame, text="Middle Button", command=self.middle_button_action, style="TButton")
# #         self.button_middle.pack(side=tk.LEFT, padx=20)

# #         self.button_right = ttk.Button(button_frame, text="Right Button", command=self.right_button_action, style="TButton")
# #         self.button_right.pack(side=tk.LEFT, padx=20)

# #     def change_first_row(self, event):
# #         """Change the plot based on the selection from the first dropdown menu."""
# #         selection = self.plot_var1.get()
# #         if selection == "K1: Base line (mni space)":
# #             for i in range(6):
# #                 self.images1[i].set_data(self.channel_data1[i])
# #         elif selection == "K1: Base line (pat space)":
# #             for i in range(6):
# #                 self.images1[i].set_data(self.channel_data3[i])
# #         elif selection == "K1/K2: Base line (mni space)":
# #             for i in range(6):
# #                 self.images1[i].set_data(self.channel_data5[i])
# #         self.canvas1.draw()

# #     def change_second_row(self, event):
# #         """Change the plot based on the selection from the second dropdown menu."""
# #         selection = self.plot_var2.get()
# #         if selection == 'K_2 (MNI space)':
# #             for i in range(6):
# #                 self.images2[i].set_data(self.channel_data2[i])
# #                 self.images2[i].set_cmap(self.cmap)
# #                 self.images2[i].set_norm(self.norm)
# #             self.cbar2.update_normal(self.images2[-1])
# #             self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
# #         else:
# #             for i in range(6):
# #                 self.images2[i].set_data(self.channel_data4[i])
# #                 self.images2[i].set_cmap(custom_cmap)
# #                 self.images2[i].set_norm(self.norm4)
# #             self.cbar2.update_normal(self.images2[-1])
# #             self.cbar2.set_label('Z-score', rotation=270, labelpad=8, color='white', fontsize=8)
# #         self.canvas2.draw()

# #     def change_third_row(self, event):
# #         """Change the plot based on the selection from the third dropdown menu."""
# #         selection = self.plot_var3.get()
# #         if selection == 'K_1/K_2':
# #             for i in range(6):
# #                 self.images3[i].set_data(self.channel_data3[i])
# #                 self.images3[i].set_cmap('bwr')
# #                 self.images3[i].set_norm(self.norm3)
# #             self.cbar3.update_normal(self.images3[-1])
# #             self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
# #         else:
# #             for i in range(6):
# #                 self.images3[i].set_data(self.channel_data4[i])
# #                 self.images3[i].set_cmap(custom_cmap)
# #                 self.images3[i].set_norm(self.norm4)
# #             self.cbar3.update_normal(self.images3[-1])
# #             self.cbar3.set_label('Z-score', rotation=270, labelpad=8, color='white', fontsize=8)
# #         self.canvas3.draw()

# #     def change_fourth_row(self, event):
# #         """Change the plot based on the selection from the fourth dropdown menu."""
# #         selection = self.plot_var4.get()
# #         self.current_dataset_row4 = selection
# #         # Get the preloaded figure
# #         self.fig4 = self.figures_row4[selection]
# #         # Update the canvas
# #         self.canvas4.get_tk_widget().destroy()
# #         self.canvas4 = FigureCanvasTkAgg(self.fig4, master=self.canvas_widget4.master)
# #         self.canvas_widget4 = self.canvas4.get_tk_widget()
# #         self.canvas_widget4.grid(row=3, column=1, sticky="nsew")
# #         self.canvas4.draw()

# #     def update_vmax(self, value):
# #         """Adjust the colormap normalization based on the upper limit slider."""
# #         vmax = float(value)
# #         self.norm.vmax = vmax
# #         self.norm_row4.vmax = vmax  # Update norm for SSP figures
# #         self.update_plots()

# #     def update_plots(self):
# #         """Update the normalization across plots that respond to the slider."""
# #         # Update images that use self.norm
# #         for img in self.images1:
# #             img.set_norm(self.norm)
# #         selection2 = self.plot_var2.get()
# #         if selection2 == 'K_2 (MNI space)':
# #             for img in self.images2:
# #                 img.set_norm(self.norm)
# #             self.cbar2.update_normal(self.images2[-1])
# #         # Update colorbars
# #         self.cbar1.update_normal(self.images1[-1])
# #         self.canvas1.draw()
# #         self.canvas2.draw()
# #         # Update SSP images if applicable
# #         if self.current_dataset_row4 == 'SSP':
# #             images = self.images_row4['SSP']
# #             for img in images:
# #                 img.set_norm(self.norm_row4)
# #             self.canvas4.draw()

# #     def show_large_image(self, axes, colorbar=None):
# #         """Open a new window to display a larger version of the images in the selected row with a colorbar (if provided)."""
# #         # Create a new window for displaying the large images
# #         large_image_window = tk.Toplevel(self)
# #         large_image_window.title("Large Images")
# #         fig = Figure(figsize=(16, 5), facecolor='black')
    
# #         # Adjust GridSpec depending on whether we have a colorbar
# #         if colorbar:
# #             gs = GridSpec(1, len(axes) + 1, width_ratios=[1] * len(axes) + [0.05], figure=fig)
# #         else:
# #             gs = GridSpec(1, len(axes), width_ratios=[1] * len(axes), figure=fig)
    
# #         # Plot each image in the new figure
# #         large_axes = []
# #         for i, axis in enumerate(axes):
# #             # Create a subplot for each image
# #             ax = fig.add_subplot(gs[0, i], facecolor='black')
            
# #             # Extract the data and norm from the corresponding smaller plot
# #             img_data = axis.images[0].get_array()
# #             norm = axis.images[0].norm
# #             cmap = axis.images[0].get_cmap()
            
# #             # Display the data in the large subplot
# #             im = ax.imshow(img_data, cmap=cmap, norm=norm, interpolation='bicubic')
# #             ax.axis('off')
            
# #             large_axes.append(im)
    
# #         # Add the colorbar to the figure if provided
# #         if colorbar:
# #             cbar_ax = fig.add_subplot(gs[0, len(axes)])
# #             cbar = fig.colorbar(large_axes[-1], cax=cbar_ax, orientation='vertical')
# #             cbar.set_label(colorbar.ax.get_ylabel(), rotation=270, labelpad=15, color='white')
            
# #             # Set colorbar properties to match the theme
# #             cbar.ax.yaxis.set_tick_params(color='white')
# #             cbar.outline.set_edgecolor('white')
# #             cbar.ax.yaxis.set_tick_params(labelcolor='white')
# #             cbar.ax.tick_params(labelsize=14, colors='white')
    
# #         # Create a canvas to hold the figure and embed it in the new window
# #         canvas = FigureCanvasTkAgg(fig, master=large_image_window)
# #         canvas_widget = canvas.get_tk_widget()
# #         canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
# #         # Adjust the layout and draw the canvas
# #         fig.tight_layout()
# #         canvas.draw()

# #     def show_large_image_fig4(self):
# #         """Display the large version of the fourth figure."""
# #         large_image_window = tk.Toplevel(self)
# #         large_image_window.title("Large Image")

# #         # Recreate the figure with a larger size
# #         if self.current_dataset_row4 == 'SSP':
# #             norm = self.norm_row4
# #         else:
# #             norm = None  # For 'SSP Z-score', norm is not used

# #         # Create the figure with larger size
# #         fig_large, _ = create_custom_figure(self.current_dataset_row4, norm=norm, figsize=(16, 5))

# #         # Create a canvas to hold the figure and embed it in the new window
# #         canvas = FigureCanvasTkAgg(fig_large, master=large_image_window)
# #         canvas_widget = canvas.get_tk_widget()
# #         canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# #         fig_large.tight_layout()
# #         canvas.draw()

# #     def left_button_action(self):
# #         """Action for the left button."""
# #         messagebox.showinfo("Button Clicked", "Left Button was clicked")

# #     def middle_button_action(self):
# #         """Action for the middle button."""
# #         messagebox.showinfo("Button Clicked", "Middle Button was clicked")

# #     def right_button_action(self):
# #         """Action for the right button."""
# #         messagebox.showinfo("Button Clicked", "Right Button was clicked")

# # from Brain_surface_z_score_test import fig_get

# # if __name__ == "__main__":
# #     # Now run the Tkinter application
# #     app = App()
# #     app.mainloop()

# import matplotlib
# from matplotlib.colors import LinearSegmentedColormap
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from matplotlib.figure import Figure
# from matplotlib.gridspec import GridSpec
# from matplotlib.colors import Normalize
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import numpy as np
# import matplotlib.pyplot as plt

# # Importing fig_get from Brain_surface_z_score_test
# from Brain_surface_z_score_test import fig_get

# # Define the custom colormaps
# cdict = {
#     'red': (
#         (0.0, 0.0, 0.0),
#         (0.1, 0.5, 0.5),
#         (0.2, 0.0, 0.0),
#         (0.4, 0.2, 0.2),
#         (0.6, 0.0, 0.0),
#         (0.8, 1.0, 1.0),
#         (1.0, 1.0, 1.0)
#     ),
#     'green': (
#         (0.0, 0.0, 0.0),
#         (0.1, 0.0, 0.0),
#         (0.2, 0.0, 0.0),
#         (0.4, 1.0, 1.0),
#         (0.6, 1.0, 1.0),
#         (0.8, 1.0, 1.0),
#         (1.0, 0.0, 0.0)
#     ),
#     'blue': (
#         (0.0, 0.0, 0.0),
#         (0.1, 0.5, 0.5),
#         (0.2, 1.0, 1.0),
#         (0.4, 1.0, 1.0),
#         (0.6, 0.0, 0.0),
#         (0.8, 0.0, 0.0),
#         (1.0, 0.0, 0.0)
#     )
# }

# my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap', cdict, 256)

# # Define the custom blue-white-red colormap
# colors = [(0, 0, 0.5), (0, 0, 1), (1, 1, 1), (1, 1, 1), (1, 0, 0), (0.5, 0, 0)]
# n_bins = 10
# cmap_name = 'custom_blue_white_red'
# custom_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=n_bins)

# def create_custom_figure(first_values_yz_neg_x0, first_values_yz_pos_x1, \
#                             first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#                             first_values_xz_neg_y2, last_figure_1, last_figure_2, last_figure_3, \
#                             last_figure_4, last_figure_5, last_figure_6, \
#                             data_set, norm=None, figsize=(5.6, 2)):
#     """Creates the custom figure using the provided data and returns it."""
#     if data_set == 'SSP':
#         # Load your 2D arrays
#         first_values_yz_neg_x0 = np.rot90(np.rot90(np.rot90(first_values_yz_neg_x0)))
#         first_values_yz_pos_x1 = np.flip(np.rot90(np.rot90(np.rot90(first_values_yz_pos_x1))), axis=1)
#         first_values_yz_pos_x2 = np.rot90(np.rot90(np.rot90(first_values_yz_pos_x2)))
#         first_values_yz_neg_x2 = np.flip(np.rot90(np.rot90(np.rot90(first_values_yz_neg_x2))), axis=1)
#         first_values_xz_pos_y2 = np.rot90(np.rot90(np.rot90(first_values_xz_pos_y2)))
#         first_values_xz_neg_y2 = np.rot90(np.rot90(np.rot90(first_values_xz_neg_y2)))
#         data_list = [
#             first_values_yz_neg_x0,
#             first_values_yz_pos_x1,
#             first_values_yz_pos_x2,
#             first_values_yz_neg_x2,
#             first_values_xz_pos_y2,
#             first_values_xz_neg_y2
#         ]

#         # Create a figure with 1 row and 6 columns
#         fig = Figure(figsize=figsize, facecolor='black')
#         gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
#         axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
#         cbar_ax = fig.add_subplot(gs[0, 6])

#         # Define the normalization if not provided
#         if norm is None:
#             norm = Normalize(vmin=0, vmax=2)

#         # Plot each 2D array
#         images = []
#         for i, data in enumerate(data_list):
#             ax = axs[i]
#             im = ax.imshow(data, cmap=my_cmap, norm=norm, interpolation='bicubic')
#             ax.axis('off')
#             images.append(im)

#         # Add a shared colorbar
#         cbar = fig.colorbar(images[-1], cax=cbar_ax)
#         cbar.set_label('Value', rotation=270, labelpad=15, color='white', fontsize=8)
#         cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
#         cbar.outline.set_edgecolor('white')

#         # Adjust layout
#         fig.tight_layout()

#         return fig, images  # Return images for updating norm

#     elif data_set == 'SSP Z-score':
#         # Use the existing code (fig_get)
#         # last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6 = fig_get()
#         all_figures = [last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6]

#         # Create a new figure with 1 row and 6 columns
#         fig = Figure(figsize=figsize, facecolor='black')
#         gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
#         axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
#         cbar_ax = fig.add_subplot(gs[0, 6])

#         # Loop over all the figures and plot them in subplots
#         for i, figure in enumerate(all_figures):
#             ax_new = axs[i]
#             for ax_old in figure.axes:
#                 for img in ax_old.images:
#                     blended_image = img.get_array()
#                     im = ax_new.imshow(blended_image, cmap=img.get_cmap(), alpha=img.get_alpha())
#             ax_new.axis('off')

#         # Add one shared colorbar for all subplots
#         sm = plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=-5, vmax=5))
#         cbar = fig.colorbar(sm, cax=cbar_ax, label='Z-score')
#         cbar.ax.tick_params(labelsize=6, colors='white')
#         cbar.set_label('Z-score', fontsize=8, color='white')
#         cbar.outline.set_edgecolor('white')
#         cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white')

#         # Adjust layout
#         fig.tight_layout()

#         return fig, None  # No images to update norm

#     else:
#         # Handle other datasets if any
#         pass


# class App(tk.Toplevel):
#     def __init__(self, transformed_K_1_1=None, transformed_K_2_1=None, Z_brain=None, K_1_reshape_list_1=None, \
#                     K_2_reshape_list_1=None, first_values_yz_neg_x0=None, first_values_yz_pos_x1=None, \
#                     first_values_yz_pos_x2=None, first_values_yz_neg_x2=None, first_values_xz_pos_y2=None, \
#                     first_values_xz_neg_y2=None, \
#                     last_figure_1=None, last_figure_2=None, last_figure_3=None, last_figure_4=None, \
#                     last_figure_5=None, last_figure_6=None, master=None, button_var=None):
#         """
#         Initializes the App window.

#         Args:
#             master (tk.Tk or tk.Toplevel): The parent window.
#             button_var (tk.StringVar): Variable to capture which button is pressed.
#         """
#         super().__init__(master)
#         self.button_var = button_var  # Store the reference to the StringVar
#         self.title("Adjust Colormap Scale")
#         self.configure(bg="black")
#         self.protocol("WM_DELETE_WINDOW", self.on_close)

#         # Style configuration for dark theme
#         style = ttk.Style()
#         style.theme_use("clam")
#         style.configure("TButton", background="grey", foreground="white")
#         style.configure("TFrame", background="black")
#         style.configure("TLabel", background="black", foreground="white")
#         style.configure("TCombobox", background="grey", foreground="white", fieldbackground="grey")
#         style.configure("TScale", background="black", troughcolor="grey", sliderlength=30)
        
#         # Main frame to hold canvas and sliders
#         main_frame = ttk.Frame(self, style="TFrame")
#         main_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         # Create three matplotlib figures, each with six subplots in a single row
#         self.fig1 = Figure(figsize=(5.6, 2), facecolor='black')
#         gs1 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig1)
#         self.ax1 = [self.fig1.add_subplot(gs1[0, i]) for i in range(6)]
#         self.cbar_ax1 = self.fig1.add_subplot(gs1[0, 6])

#         self.fig2 = Figure(figsize=(5.6, 2), facecolor='black')
#         gs2 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig2)
#         self.ax2 = [self.fig2.add_subplot(gs2[0, i]) for i in range(6)]
#         self.cbar_ax2 = self.fig2.add_subplot(gs2[0, 6])

#         self.fig3 = Figure(figsize=(5.6, 2), facecolor='black')
#         gs3 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig3)
#         self.ax3 = [self.fig3.add_subplot(gs3[0, i]) for i in range(6)]
#         self.cbar_ax3 = self.fig3.add_subplot(gs3[0, 6])

      
#         # Initialize the fourth figure with datasets
#         self.datasets_row4 = ['SSP', 'SSP Z-score']
#         self.figures_row4 = {}
#         self.images_row4 = {}

#         # Create figures for all datasets
#         self.norm_row4 = Normalize(vmin=0, vmax=2)
#         for dataset_name in self.datasets_row4:
#             fig, images = create_custom_figure(first_values_yz_neg_x0, first_values_yz_pos_x1, \
#             first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#             first_values_xz_neg_y2, last_figure_1, last_figure_2, last_figure_3, \
#             last_figure_4, last_figure_5, last_figure_6, \
#             dataset_name, norm=self.norm_row4)
#             self.figures_row4[dataset_name] = fig
#             if images:
#                 self.images_row4[dataset_name] = images  # Store images for updating norm

#         # Set the default dataset
#         self.current_dataset_row4 = 'SSP'  # Default dataset
#         self.fig4 = self.figures_row4[self.current_dataset_row4]

#         # Load or generate test datasets for the first three rows
#         try:
#             self.data1 = np.rot90(transformed_K_1_1)
#             self.data2 = np.rot90(transformed_K_2_1)
#             self.data3 = self.data1 / self.data2  # For the third row
#             self.data4 = np.rot90(Z_brain)  # Z-score data
#             self.data5 = np.rot90(np.rot90(np.rot90(K_1_reshape_list_1)))
#             self.data6 = np.rot90(np.rot90(np.rot90(K_2_reshape_list_1)))
#             self.data7 = self.data5 / self.data6
#         except FileNotFoundError as e:
#             print(f"Data file not found: {e}")
#             messagebox.showerror("Error", f"Data file not found: {e}")
#             self.destroy()
#             return

#         # Select specific channels to display
#         slices = [28, 42, 56, 70, 84, 98]
#         self.channel_data1 = [self.data1[..., i] for i in slices]
#         self.channel_data2 = [self.data2[..., i] for i in slices]
#         self.channel_data3 = [self.data3[..., i] for i in slices]
#         self.channel_data4 = [self.data4[..., i] for i in slices]
        
#         multi=np.shape(K_1_reshape_list_1)[2]/np.shape(transformed_K_1_1)[2]
#         slices_pat = [int(multi*28), int(multi*42), int(multi*56), int(multi*70), int(multi*84), int(multi*98)]
#         self.channel_data5 = [self.data5[..., i] for i in slices_pat]
#         self.channel_data6 = [self.data6[..., i] for i in slices_pat]
#         self.channel_data7 = [self.data7[..., i] for i in slices_pat]


#         # Initialize normalization objects
#         self.norm = Normalize(vmin=0, vmax=2)
#         self.norm3 = Normalize(vmin=0, vmax=2)
#         self.norm4 = Normalize(vmin=-5, vmax=5)  # For Z-score data

#         # Define colormap
#         self.cmap = my_cmap
#         self.cmap_BWR=custom_cmap

#         # Initialize image plots with the datasets
#         self.images1 = [
#             self.ax1[i].imshow(self.channel_data1[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
#             for i in range(6)
#         ] 
#         self.images2 = [
#             self.ax2[i].imshow(self.channel_data2[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap) 
#             for i in range(6)
#         ] 
#         self.images3 = [
#             self.ax3[i].imshow(self.channel_data3[i], interpolation='nearest', norm=self.norm3, cmap='bwr') 
#             for i in range(6)
#         ] 
        
#         # Remove axis from each plot and set facecolor
#         for ax in self.ax1 + self.ax2 + self.ax3:
#             ax.set_facecolor('black')
#             ax.tick_params(axis='both', colors='white')
#             ax.spines['bottom'].set_color('white')
#             ax.spines['top'].set_color('white')
#             ax.spines['right'].set_color('white')
#             ax.spines['left'].set_color('white')
#             ax.axis('off')

#         # Create colorbars for the first three plots using the seventh subplot
#         self.cbar1 = self.fig1.colorbar(self.images1[-1], cax=self.cbar_ax1)
#         self.cbar1.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
#         self.cbar1.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
#         self.cbar1.outline.set_edgecolor('white')

#         self.cbar2 = self.fig2.colorbar(self.images2[-1], cax=self.cbar_ax2)
#         self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
#         self.cbar2.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
#         self.cbar2.outline.set_edgecolor('white')

#         self.cbar3 = self.fig3.colorbar(self.images3[-1], cax=self.cbar_ax3)
#         self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
#         self.cbar3.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
#         self.cbar3.outline.set_edgecolor('white')

#         # Embed the figures in the Tk window
#         self.canvas1 = FigureCanvasTkAgg(self.fig1, master=main_frame)
#         self.canvas_widget1 = self.canvas1.get_tk_widget()
#         self.canvas_widget1.grid(row=0, column=1, sticky="nsew")

#         self.canvas2 = FigureCanvasTkAgg(self.fig2, master=main_frame)
#         self.canvas_widget2 = self.canvas2.get_tk_widget()
#         self.canvas_widget2.grid(row=1, column=1, sticky="nsew")

#         self.canvas3 = FigureCanvasTkAgg(self.fig3, master=main_frame)
#         self.canvas_widget3 = self.canvas3.get_tk_widget()
#         self.canvas_widget3.grid(row=2, column=1, sticky="nsew")

#         # For row 4, use the figure created based on the current dataset
#         self.canvas4 = FigureCanvasTkAgg(self.fig4, master=main_frame)
#         self.canvas_widget4 = self.canvas4.get_tk_widget()
#         self.canvas_widget4.grid(row=3, column=1, sticky="nsew")

#         # Frame for the sliders
#         sliders_frame = ttk.Frame(main_frame, width=50, style="TFrame")
#         sliders_frame.grid(row=0, column=2, rowspan=4, sticky="ns", padx=10, pady=100)

#         # Create a vertical slider for the upper limit adjustment
#         self.slider_vmax = ttk.Scale(
#             sliders_frame, 
#             from_=2, 
#             to=0.01, 
#             orient='vertical', 
#             command=self.update_vmax, 
#             style="TScale"
#         )
#         self.slider_vmax.set(2)
#         ttk.Label(sliders_frame, text="Övre gräns", background="black", foreground="white").pack()
#         self.slider_vmax.pack(expand=True, fill=tk.Y, pady=(0, 10))

#         # Create frame for the first row controls
#         row1_controls = ttk.Frame(main_frame, style="TFrame")
#         row1_controls.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

#         # Dropdown menu to select the dataset for the first row
#         self.plot_var1 = tk.StringVar()
#         self.plot_dropdown1 = ttk.Combobox(
#             row1_controls, 
#             textvariable=self.plot_var1, 
#             state='readonly', 
#             width=25, 
#             style="TCombobox"
#         )
#         self.plot_dropdown1['values'] = (
#             "K1: Base line (mni space)", 
#             "K1: Base line (pat space)"
#         )
#         self.plot_dropdown1.current(0)
#         self.plot_dropdown1.grid(row=0, column=0, padx=5, pady=5)

#         # Button to show the first row large
#         self.show_large_button1 = ttk.Button(
#             row1_controls, 
#             text="Visa stort", 
#             command=lambda: self.show_large_image(self.ax1, self.cbar1), 
#             style="TButton"
#         )
#         self.show_large_button1.grid(row=1, column=0, padx=5, pady=5)

#         # Create frame for the second row controls
#         row2_controls = ttk.Frame(main_frame, style="TFrame")
#         row2_controls.grid(row=1, column=0, sticky="ns", padx=5, pady=5)

#         # Dropdown menu to select the dataset for the second row
#         self.plot_var2 = tk.StringVar()
#         self.plot_dropdown2 = ttk.Combobox(
#             row2_controls, 
#             textvariable=self.plot_var2, 
#             state='readonly', 
#             width=25, 
#             style="TCombobox"
#         )
#         self.plot_dropdown2['values'] = ('K_2 (MNI space)', 'K_2 (pat space)')
#         self.plot_dropdown2.current(0)
#         self.plot_dropdown2.grid(row=0, column=0, padx=5, pady=5)

#         # Button to show the second row large
#         self.show_large_button2 = ttk.Button(
#             row2_controls, 
#             text="Visa stort", 
#             command=lambda: self.show_large_image(self.ax2, self.cbar2), 
#             style="TButton"
#         )
#         self.show_large_button2.grid(row=1, column=0, padx=5, pady=5)

#         # Create frame for the third row controls
#         row3_controls = ttk.Frame(main_frame, style="TFrame")
#         row3_controls.grid(row=2, column=0, sticky="ns", padx=5, pady=5)

#         # Dropdown menu to select the dataset for the third row
#         self.plot_var3 = tk.StringVar()
#         self.plot_dropdown3 = ttk.Combobox(
#             row3_controls, 
#             textvariable=self.plot_var3, 
#             state='readonly', 
#             width=25, 
#             style="TCombobox"
#         )
#         self.plot_dropdown3['values'] = ('K_1/K_2', 'Z-score',  
#         "K1/K2: Base line (mni space)")
#         self.plot_dropdown3.current(0)
#         self.plot_dropdown3.grid(row=0, column=0, padx=5, pady=5)

#         # Button to show the third row large
#         self.show_large_button3 = ttk.Button(
#             row3_controls, 
#             text="Visa stort", 
#             command=lambda: self.show_large_image(self.ax3, self.cbar3), 
#             style="TButton"
#         )
#         self.show_large_button3.grid(row=1, column=0, padx=5, pady=5)

#         # Create frame for the fourth row controls
#         row4_controls = ttk.Frame(main_frame, style="TFrame")
#         row4_controls.grid(row=3, column=0, sticky="ns", padx=5, pady=5)

#         # Dropdown menu to select the dataset for the fourth row
#         self.plot_var4 = tk.StringVar()
#         self.plot_dropdown4 = ttk.Combobox(
#             row4_controls, 
#             textvariable=self.plot_var4, 
#             state='readonly', 
#             width=25, 
#             style="TCombobox"
#         )
#         self.plot_dropdown4['values'] = self.datasets_row4
#         self.plot_dropdown4.current(0)
#         self.plot_dropdown4.grid(row=0, column=0, padx=5, pady=5)

#         # Button to show the fourth row large
#         self.show_large_button4 = ttk.Button(
#             row4_controls, 
#             text="Visa stort", 
#             command=lambda: self.show_large_image_fig4(first_values_yz_neg_x0, first_values_yz_pos_x1, \
#             first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#             first_values_xz_neg_y2, last_figure_1, last_figure_2, last_figure_3, \
#             last_figure_4, last_figure_5, last_figure_6), 
#             style="TButton"
#         )
#         self.show_large_button4.grid(row=1, column=0, padx=5, pady=5)

#         # Configure grid to expand properly
#         main_frame.grid_columnconfigure(1, weight=1)
#         main_frame.grid_rowconfigure(0, weight=1)
#         main_frame.grid_rowconfigure(1, weight=1)
#         main_frame.grid_rowconfigure(2, weight=1)
#         main_frame.grid_rowconfigure(3, weight=1)

#         self.fig1.tight_layout()
#         self.fig2.tight_layout()
#         self.fig3.tight_layout()
#         self.fig4.tight_layout()
#         self.canvas1.draw()
#         self.canvas2.draw()
#         self.canvas3.draw()
#         self.canvas4.draw()

#         # Bind dropdown change events
#         self.plot_dropdown1.bind('<<ComboboxSelected>>', self.change_first_row)
#         self.plot_dropdown2.bind('<<ComboboxSelected>>', self.change_second_row)
#         self.plot_dropdown3.bind('<<ComboboxSelected>>', self.change_third_row)
#         self.plot_dropdown4.bind('<<ComboboxSelected>>', self.change_fourth_row)

#         # Bottom frame for buttons
#         bottom_frame = ttk.Frame(self, style="TFrame")
#         bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

#         # Inner frame to center buttons
#         button_frame = ttk.Frame(bottom_frame, style="TFrame")
#         button_frame.pack(side=tk.TOP, expand=True)

#         # Create buttons for the button frame
#         self.button_left = ttk.Button(
#             button_frame, 
#             text="Left Button", 
#             command=self.left_button_action, 
#             style="TButton"
#         )
#         self.button_left.pack(side=tk.LEFT, padx=20)

#         self.button_middle = ttk.Button(
#             button_frame, 
#             text="Middle Button", 
#             command=self.middle_button_action, 
#             style="TButton"
#         )
#         self.button_middle.pack(side=tk.LEFT, padx=20)

#         self.button_right = ttk.Button(
#             button_frame, 
#             text="Right Button", 
#             command=self.right_button_action, 
#             style="TButton"
#         )
#         self.button_right.pack(side=tk.LEFT, padx=20)

#         # **Add Window Management Commands Here**
#         self.deiconify()           # Ensure the window is not minimized or hidden
#         self.lift()                # Bring the window to the top
#         self.focus_force()         # Focus on the App window
#         self.grab_set()            # Make the App window modal (optional but recommended)
#         self.update_idletasks()    # Process any pending idle tasks
#         self.update()              # Force an update to render all widgets

#         # **Release the grab to make the window interactive**
#         self.grab_release()

#     def on_close(self):
#         """Handle the window close event."""
#         print("App window is closing.")
#         if self.button_var:
#             self.button_var.set("Closed")  # Optionally set a value indicating closure
#         self.destroy()
#         if self.master:
#             self.master.quit()  # Ensure the application exits when App window is closed

#     def left_button_action(self):
#         """Action for the left button."""
#         if self.button_var:
#             self.button_var.set("Left")
#         self.destroy()

#     def middle_button_action(self):
#         """Action for the middle button."""
#         if self.button_var:
#             self.button_var.set("Middle")
#         self.destroy()

#     def right_button_action(self):
#         """Action for the right button."""
#         if self.button_var:
#             self.button_var.set("Right")
#         self.destroy()

#     def change_first_row(self, event):
#         """Change the plot based on the selection from the first dropdown menu."""
#         selection = self.plot_var1.get()
#         print(f"First row selection changed to: {selection}")
#         if selection == "K1: Base line (mni space)":
#             for i in range(6):
#                 self.images1[i].set_data(self.channel_data1[i])
#         elif selection == "K1: Base line (pat space)":
#             for i in range(6):
#                 self.images1[i].set_data(self.channel_data5[i])
        
#         self.canvas1.draw()

#     def change_second_row(self, event):
#         """Change the plot based on the selection from the second dropdown menu."""
#         selection = self.plot_var2.get()
#         print(f"Second row selection changed to: {selection}")
#         if selection == 'K_2 (MNI space)':
#             for i in range(6):
#                 self.images2[i].set_data(self.channel_data2[i])
#                 self.images2[i].set_cmap(self.cmap)
#                 self.images2[i].set_norm(self.norm)
#             self.cbar2.update_normal(self.images1[-1])
#             self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
#         elif selection == 'K_2 (pat space)':
#             for i in range(6):
#                 self.images2[i].set_data(self.channel_data6[i])
#                 self.images2[i].set_cmap(self.cmap)
#                 self.images2[i].set_norm(self.norm)
#             self.cbar2.update_normal(self.images1[-1])
#             self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
#         elif selection == "K1/K2: Base line (mni space)":
#             for i in range(6):
#                 self.images1[i].set_data(self.channel_data5[i])
#         self.canvas2.draw()
        

#     def change_third_row(self, event):
#         """Change the plot based on the selection from the third dropdown menu."""
#         selection = self.plot_var3.get()
#         print(f"Third row selection changed to: {selection}")
#         if selection == 'K_1/K_2':
#             for i in range(6):
#                 self.images3[i].set_data(self.channel_data3[i])
#                 self.images3[i].set_cmap('bwr')
#                 self.images3[i].set_norm(self.norm3)
#             self.cbar3.update_normal(self.images3[-1])
#             self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
#         elif selection == 'Z-score':
#             for i in range(6):
#                 self.images3[i].set_data(self.channel_data4[i])
#                 self.images3[i].set_cmap(custom_cmap)
#                 self.images3[i].set_norm(self.norm4)
#             self.cbar3.update_normal(self.images3[-1])
#             self.cbar3.set_label('Z-score', rotation=270, labelpad=8, color='white', fontsize=8)
#         elif selection == 'K_1/K_2 (pat space)':
#             for i in range(6):
#                 self.images3[i].set_data(self.channel_data7[i])
#                 self.images3[i].set_cmap('bwr')
#                 self.images3[i].set_norm(self.norm3)
#             self.cbar3.update_normal(self.images3[-1])
#             self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
#         self.canvas3.draw()

#     def change_fourth_row(self, event):
#         """Change the plot based on the selection from the fourth dropdown menu."""
#         selection = self.plot_var4.get()
#         print(f"Fourth row selection changed to: {selection}")
#         self.current_dataset_row4 = selection
#         # Get the preloaded figure
#         self.fig4 = self.figures_row4[selection]
#         # Update the canvas
#         self.canvas4.get_tk_widget().destroy()
#         self.canvas4 = FigureCanvasTkAgg(self.fig4, master=self.canvas_widget4.master)
#         self.canvas_widget4 = self.canvas4.get_tk_widget()
#         self.canvas_widget4.grid(row=3, column=1, sticky="nsew")
#         self.canvas4.draw()

#     def update_vmax(self, value):
#         """Adjust the colormap normalization based on the upper limit slider."""
#         vmax = float(value)
#         print(f"Updating vmax to: {vmax}")
#         self.norm.vmax = vmax
#         self.norm_row4.vmax = vmax  # Update norm for SSP figures
#         self.update_plots()

#     def update_plots(self):
#         """Update the normalization across plots that respond to the slider."""
#         print("Updating plots with new normalization.")
#         # Update images that use self.norm
#         for img in self.images1:
#             img.set_norm(self.norm)
#         selection2 = self.plot_var2.get()
#         if selection2 == 'K_2 (MNI space)':
#             for img in self.images2:
#                 img.set_norm(self.norm)
#             self.cbar2.update_normal(self.images2[-1])
#         # Update colorbars
#         self.cbar1.update_normal(self.images1[-1])
#         self.canvas1.draw()
#         self.canvas2.draw()
#         # Update SSP images if applicable
#         if self.current_dataset_row4 == 'SSP':
#             images = self.images_row4['SSP']
#             for img in images:
#                 img.set_norm(self.norm_row4)
#             self.canvas4.draw()

#     def show_large_image(self, axes, colorbar=None):
#         """Open a new window to display a larger version of the images in the selected row with a colorbar (if provided)."""
#         print("Opening large image window...")
#         # Create a new window for displaying the large images
#         large_image_window = tk.Toplevel(self)
#         large_image_window.title("Large Images")
#         large_image_window.configure(bg="black")
#         fig = Figure(figsize=(16, 5), facecolor='black')
    
#         # Adjust GridSpec depending on whether we have a colorbar
#         if colorbar:
#             gs = GridSpec(1, len(axes) + 1, width_ratios=[1] * len(axes) + [0.05], figure=fig)
#         else:
#             gs = GridSpec(1, len(axes), width_ratios=[1] * len(axes), figure=fig)
    
#         # Plot each image in the new figure
#         large_axes = []
#         for i, axis in enumerate(axes):
#             # Create a subplot for each image
#             ax = fig.add_subplot(gs[0, i], facecolor='black')
            
#             # Extract the data and norm from the corresponding smaller plot
#             img_data = axis.images[0].get_array()
#             norm = axis.images[0].norm
#             cmap = axis.images[0].get_cmap()
            
#             # Display the data in the large subplot
#             im = ax.imshow(img_data, cmap=cmap, norm=norm, interpolation='bicubic')
#             ax.axis('off')
            
#             large_axes.append(im)
    
#         # Add the colorbar to the figure if provided
#         if colorbar:
#             cbar_ax = fig.add_subplot(gs[0, len(axes)])
#             cbar = fig.colorbar(large_axes[-1], cax=cbar_ax, orientation='vertical')
#             cbar.set_label(colorbar.ax.get_ylabel(), rotation=270, labelpad=15, color='white')
            
#             # Set colorbar properties to match the theme
#             cbar.ax.yaxis.set_tick_params(color='white')
#             cbar.outline.set_edgecolor('white')
#             cbar.ax.yaxis.set_tick_params(labelcolor='white')
#             cbar.ax.tick_params(labelsize=14, colors='white')
    
#         # Create a canvas to hold the figure and embed it in the new window
#         canvas = FigureCanvasTkAgg(fig, master=large_image_window)
#         canvas_widget = canvas.get_tk_widget()
#         canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
#         # Adjust the layout and draw the canvas
#         fig.tight_layout()
#         canvas.draw()

#     def show_large_image_fig4(self, first_values_yz_neg_x0, first_values_yz_pos_x1, \
#     first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#     first_values_xz_neg_y2, last_figure_1, last_figure_2, last_figure_3, \
#     last_figure_4, last_figure_5, last_figure_6):
#         """Display the large version of the fourth figure."""
#         print("Opening large image for figure 4...")
#         large_image_window = tk.Toplevel(self)
#         large_image_window.title("Large Image")
#         large_image_window.configure(bg="black")

#         # Recreate the figure with a larger size
#         if self.current_dataset_row4 == 'SSP':
#             norm = self.norm_row4
#         else:
#             norm = None  # For 'SSP Z-score', norm is not used

#         # Create the figure with larger size
#         fig_large, _ = create_custom_figure(self.current_dataset_row4, first_values_yz_neg_x0, first_values_yz_pos_x1, \
#         first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#         first_values_xz_neg_y2, last_figure_1, last_figure_2, last_figure_3, \
#         last_figure_4, last_figure_5, last_figure_6, self.current_dataset_row4, norm=norm, figsize=(16, 5))

#         # Create a canvas to hold the figure and embed it in the new window
#         canvas = FigureCanvasTkAgg(fig_large, master=large_image_window)
#         canvas_widget = canvas.get_tk_widget()
#         canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

#         fig_large.tight_layout()
#         canvas.draw()

# def open_app_window(initial_window, button_var, \
#                         transformed_K_1_1, transformed_K_2_1, Z_brain, K_1_reshape_list_1, \
#                         K_2_reshape_list_1, first_values_yz_neg_x0, first_values_yz_pos_x1, \
#                         first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#                         first_values_xz_neg_y2, \
#                         neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2):
#     """
#     Hides the initial_window and opens the App window as a new top-level window.

#     Args:
#         initial_window (tk.Tk or tk.Toplevel): The window to be hidden.
#         button_var (tk.StringVar): Variable to capture which button is pressed.

#     Returns:
#         App: An instance of the App window.
#     """
#     print("Opening App window...")
#     initial_window.withdraw()  # Hide the initial window instead of destroying it
#     print("Initial window hidden.")

#     # Create the App window as a Toplevel instance, passing the button_var
#     app = App(transformed_K_1_1, transformed_K_2_1, Z_brain, K_1_reshape_list_1, \
#     K_2_reshape_list_1, first_values_yz_neg_x0, first_values_yz_pos_x1, \
#     first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2, \
#     first_values_xz_neg_y2, \
#     neg_x0, pos_x1, pos_x2, neg_x2, pos_y2, neg_y2, master=initial_window, button_var=button_var)
#     print("App window created.")
    
#     return app



# # # Example usage:
# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     root.geometry("1200x800")  # Set a default size
# #     open_app_window(root)
# #     root.mainloop()


# # # If you want to run the app directly
# # if __name__ == "__main__":
# #     hej=1
# #     root = tk.Tk()
# #     root.withdraw()  # Hide the root window
# #     app_window = open_app_window(root, hej)
# #     app_window.mainloop()
    
# # def open_app_window(master, data1, data2, data3, data4, data5, data6, first_values_yz_neg_x0, first_values_yz_pos_x1, first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_yz_pos_y2, first_values_yz_neg_y2, \
# #                     last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6):
# #     app = App(master)
# #     return appa
    
# # def open_app_window(master, data1, data2, data3, data4, data5, data6, first_values_yz_neg_x0, first_values_yz_pos_x1, \
# #                     first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_yz_pos_y2, first_values_yz_neg_y2, \
# #                     last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6):
# #     print("open_app_window called")
# #     app = App(master,
# #               data1, data2, data3, data4, data5, data6,
# #               first_values_yz_neg_x0, first_values_yz_pos_x1,
# #               first_values_yz_pos_x2, first_values_yz_neg_x2,
# #               first_values_yz_pos_y2, first_values_yz_neg_y2,
# #               last_figure_1, last_figure_2, last_figure_3,
# #               last_figure_4, last_figure_5, last_figure_6)
# #     print("App instance created")
# #     return app

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

def create_custom_figure(first_values_yz_neg_x0, first_values_yz_pos_x1,
                         first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2,
                         first_values_xz_neg_y2, last_figure_1, last_figure_2, last_figure_3,
                         last_figure_4, last_figure_5, last_figure_6,
                         regions_first_values_yz_neg_x0, regions_first_values_yz_pos_x1, 
                         regions_first_values_yz_pos_x2, regions_first_values_yz_neg_x2,
                         regions_first_values_xz_pos_y2, regions_first_values_xz_neg_y2,
                         data_set, norm=None, fig=None):
    """Creates or updates the custom figure using the provided data and returns it."""
    print('-----', data_set, '-----------')
    if fig is None:
        fig = Figure(facecolor='black')
    else:
        fig.clear()

    if data_set == 'SSP':
        # Rotate the data arrays if necessary
        data_list = [
            np.rot90(np.rot90(np.rot90(first_values_yz_neg_x0))),
            np.rot90(np.rot90(np.rot90(first_values_yz_pos_x1))),
            np.rot90(np.rot90(np.rot90(first_values_yz_pos_x2))),
            np.rot90(np.rot90(np.rot90(first_values_yz_neg_x2))),
            np.rot90(np.rot90(np.rot90(first_values_xz_pos_y2))),
            np.rot90(np.rot90(np.rot90(first_values_xz_neg_y2)))
        ]

        # Create a figure with 1 row and 6 columns
        gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
        axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
        cbar_ax = fig.add_subplot(gs[0, 6])

        # Define the normalization if not provided
        if norm is None:
            norm = Normalize(vmin=0, vmax=2)

        # Plot each 2D array
        images = []
        for i, data in enumerate(data_list):
            ax = axs[i]
            im = ax.imshow(data, cmap=my_cmap, norm=norm, interpolation='bicubic')
            ax.axis('off')
            ax.set_aspect('equal')
            images.append(im)

        # Add a shared colorbar
        cbar = fig.colorbar(images[-1], cax=cbar_ax)
        cbar.set_label('Value', rotation=270, labelpad=15, color='white', fontsize=8)
        cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
        cbar.outline.set_edgecolor('white')

        # Adjust layout
        fig.tight_layout()

        return images  # Return images for updating norm

    elif data_set == 'SSP Z-score':
        # Use the existing figures
        all_figures = [last_figure_1, last_figure_2, last_figure_3, last_figure_4, last_figure_5, last_figure_6]

        # Create a figure with 1 row and 6 columns
        gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
        axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
        cbar_ax = fig.add_subplot(gs[0, 6])

        # Loop over all the figures and plot them in subplots
        for i, figure in enumerate(all_figures):
            ax_new = axs[i]
            for ax_old in figure.axes:
                for img in ax_old.images:
                    blended_image = img.get_array()
                    im = ax_new.imshow(blended_image, cmap=img.get_cmap(), alpha=img.get_alpha())
            ax_new.axis('off')
            ax_new.set_aspect('equal')

        # Add one shared colorbar
        sm = plt.cm.ScalarMappable(cmap=custom_cmap, norm=plt.Normalize(vmin=-5, vmax=5))
        cbar = fig.colorbar(sm, cax=cbar_ax)
        cbar.set_label('Z-score', rotation=270, labelpad=15, fontsize=8, color='white')
        cbar.ax.tick_params(labelsize=6, colors='white')
        cbar.outline.set_edgecolor('white')
        cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white')

        # Adjust layout
        fig.tight_layout()

        return None  # No images to update norm
    elif data_set == 'SSP regions':
        print('----- hit ------------')
        # Rotate the data arrays if necessary
        data_list = [
            np.rot90(np.rot90(np.rot90(regions_first_values_yz_neg_x0))),
            np.rot90(np.rot90(np.rot90(regions_first_values_yz_pos_x1))),
            np.rot90(np.rot90(np.rot90(regions_first_values_yz_pos_x2))),
            np.rot90(np.rot90(np.rot90(regions_first_values_yz_neg_x2))),
            np.rot90(np.rot90(np.rot90(regions_first_values_xz_pos_y2))),
            np.rot90(np.rot90(np.rot90(regions_first_values_xz_neg_y2)))
        ]

        # Create a figure with 1 row and 6 columns
        gs = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=fig)
        axs = [fig.add_subplot(gs[0, i]) for i in range(6)]
        cbar_ax = fig.add_subplot(gs[0, 6])

        # Define the normalization if not provided
        if norm is None:
            norm = Normalize(vmin=0, vmax=2)

        # Plot each 2D array
        images = []
        for i, data in enumerate(data_list):
            ax = axs[i]
            im = ax.imshow(data, cmap=custom_cmap, norm=plt.Normalize(vmin=-5, vmax=5))
            ax.axis('off')
            ax.set_aspect('equal')
            images.append(im)

        # Add a shared colorbar
        cbar = fig.colorbar(images[-1], cax=cbar_ax)
        cbar.set_label('Value', rotation=270, labelpad=15, color='white', fontsize=8)
        cbar.ax.yaxis.set_tick_params(color='white', labelcolor='white', labelsize=6)
        cbar.outline.set_edgecolor('white')

        # Adjust layout
        fig.tight_layout()

        return None  # Return images for updating norm

    else:
        # Handle other datasets if any
        pass

class App(tk.Toplevel):
    def __init__(self, transformed_K_1_1=None, transformed_K_2_1=None, Z_brain=None, K_1_reshape_list_1=None,
                 K_2_reshape_list_1=None, first_values_yz_neg_x0=None, first_values_yz_pos_x1=None,
                 first_values_yz_pos_x2=None, first_values_yz_neg_x2=None, first_values_xz_pos_y2=None,
                 first_values_xz_neg_y2=None,
                 last_figure_1=None, last_figure_2=None, last_figure_3=None, last_figure_4=None,
                 last_figure_5=None, last_figure_6=None, 
                 regions_first_values_yz_neg_x0=None, regions_first_values_yz_pos_x1=None, 
                 regions_first_values_yz_pos_x2=None, regions_first_values_yz_neg_x2=None, 
                 regions_first_values_xz_pos_y2=None, regions_first_values_xz_neg_y2=None,
                 master=None, button_var=None):
        """
        Initializes the App window.

        Args:
            master (tk.Tk or tk.Toplevel): The parent window.
            button_var (tk.StringVar): Variable to capture which button is pressed.
        """
        super().__init__(master)
        self.state('zoomed')
        self.button_var = button_var  # Store the reference to the StringVar
        self.title("Adjust Colormap Scale")
        self.configure(bg="black")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # Configure the grid layout for the App window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Store data arrays as instance variables
        self.first_values_yz_neg_x0 = first_values_yz_neg_x0
        self.first_values_yz_pos_x1 = first_values_yz_pos_x1
        self.first_values_yz_pos_x2 = first_values_yz_pos_x2
        self.first_values_yz_neg_x2 = first_values_yz_neg_x2
        self.first_values_xz_pos_y2 = first_values_xz_pos_y2
        self.first_values_xz_neg_y2 = first_values_xz_neg_y2
        self.last_figure_1 = last_figure_1
        self.last_figure_2 = last_figure_2
        self.last_figure_3 = last_figure_3
        self.last_figure_4 = last_figure_4
        self.last_figure_5 = last_figure_5
        self.last_figure_6 = last_figure_6
        self.regions_first_values_yz_neg_x0 = regions_first_values_yz_neg_x0
        self.regions_first_values_yz_pos_x1 = regions_first_values_yz_pos_x1
        self.regions_first_values_yz_pos_x2 = regions_first_values_yz_pos_x2
        self.regions_first_values_yz_neg_x2 = regions_first_values_yz_neg_x2
        self.regions_first_values_xz_pos_y2 = regions_first_values_xz_pos_y2
        self.regions_first_values_xz_neg_y2 = regions_first_values_xz_neg_y2

        # Style configuration for dark theme
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", background="grey", foreground="white")
        style.configure("TFrame", background="black")
        style.configure("TLabel", background="black", foreground="white")
        style.configure("TCombobox", background="grey", foreground="white", fieldbackground="grey")
        style.configure("TScale", background="black", troughcolor="grey", sliderlength=30)

        # Main frame to hold canvas and sliders
        self.main_frame = ttk.Frame(self, style="TFrame")
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Bottom frame for buttons
        bottom_frame = ttk.Frame(self, style="TFrame")
        bottom_frame.grid(row=1, column=0, sticky="ew")

        # Configure grid weights to make main_frame expand
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Configure grid weights for main_frame
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(2, weight=1)
        self.main_frame.grid_rowconfigure(3, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)

        # Create figures without specifying figsize (let them scale automatically)
        self.fig1 = Figure(facecolor='black')
        gs1 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig1)
        self.ax1 = [self.fig1.add_subplot(gs1[0, i]) for i in range(6)]
        self.cbar_ax1 = self.fig1.add_subplot(gs1[0, 6])

        self.fig2 = Figure(facecolor='black')
        gs2 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig2)
        self.ax2 = [self.fig2.add_subplot(gs2[0, i]) for i in range(6)]
        self.cbar_ax2 = self.fig2.add_subplot(gs2[0, 6])

        self.fig3 = Figure(facecolor='black')
        gs3 = GridSpec(1, 7, width_ratios=[1]*6 + [0.05], figure=self.fig3)
        self.ax3 = [self.fig3.add_subplot(gs3[0, i]) for i in range(6)]
        self.cbar_ax3 = self.fig3.add_subplot(gs3[0, 6])

        # Initialize the fourth figure with datasets
        self.datasets_row4 = ['SSP', 'SSP Z-score', 'SSP regions']
        self.fig4 = Figure(facecolor='black')
        self.images_row4 = {}

        # Initialize normalization object for SSP
        self.norm_row4 = Normalize(vmin=0, vmax=2)

        # Set the default dataset
        self.current_dataset_row4 = 'SSP'  # Default dataset

        # Create the initial figure for row 4
        images = create_custom_figure(
            self.first_values_yz_neg_x0, self.first_values_yz_pos_x1, self.first_values_yz_pos_x2,
            self.first_values_yz_neg_x2, self.first_values_xz_pos_y2, self.first_values_xz_neg_y2,
            self.last_figure_1, self.last_figure_2, self.last_figure_3,
            self.last_figure_4, self.last_figure_5, self.last_figure_6,
            self.regions_first_values_yz_neg_x0, self.regions_first_values_yz_pos_x1, 
            self.regions_first_values_yz_pos_x2, self.regions_first_values_yz_neg_x2,
            self.regions_first_values_xz_pos_y2, self.regions_first_values_xz_neg_y2,
            self.current_dataset_row4, norm=self.norm_row4, fig=self.fig4
        )
        self.images_row4[self.current_dataset_row4] = images

        # Load or generate test datasets for the first three rows
        try:
            self.data1 = np.rot90(transformed_K_1_1)
            self.data2 = np.rot90(transformed_K_2_1)
            self.data3 = self.data1 / self.data2  # For the third row
            self.data4 = np.rot90(Z_brain)  # Z-score data
            self.data5 = np.rot90(np.rot90(np.rot90(K_1_reshape_list_1)))
            self.data6 = np.rot90(np.rot90(np.rot90(K_2_reshape_list_1)))
            self.data7 = self.data5 / self.data6
        except FileNotFoundError as e:
            print(f"Data file not found: {e}")
            messagebox.showerror("Error", f"Data file not found: {e}")
            self.destroy()
            return

        # Select specific channels to display
        slices = [28, 42, 56, 70, 84, 98]
        self.channel_data1 = [self.data1[..., i] for i in slices]
        self.channel_data2 = [self.data2[..., i] for i in slices]
        self.channel_data3 = [self.data3[..., i] for i in slices]
        self.channel_data4 = [self.data4[..., i] for i in slices]

        multi = np.shape(K_1_reshape_list_1)[2] / np.shape(transformed_K_1_1)[2]
        slices_pat = [int(multi*28), int(multi*42), int(multi*56), int(multi*70), int(multi*84), int(multi*98)]
        self.channel_data5 = [self.data5[..., i] for i in slices_pat]
        self.channel_data6 = [self.data6[..., i] for i in slices_pat]
        self.channel_data7 = [self.channel_data5[i] / self.channel_data6[i] for i in range(len(self.channel_data5))]

        # Initialize normalization objects
        self.norm = Normalize(vmin=0, vmax=2)
        self.norm3 = Normalize(vmin=0, vmax=2)
        self.norm4 = Normalize(vmin=-5, vmax=5)  # For Z-score data

        # Define colormap
        self.cmap = my_cmap
        self.cmap_BWR = custom_cmap

        # Initialize image plots with the datasets
        self.images1 = [
            self.ax1[i].imshow(self.channel_data1[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap)
            for i in range(6)
        ]
        self.images2 = [
            self.ax2[i].imshow(self.channel_data2[i], interpolation='bicubic', norm=self.norm, cmap=self.cmap)
            for i in range(6)
        ]
        self.images3 = [
            self.ax3[i].imshow(self.channel_data3[i], interpolation='nearest', norm=self.norm3, cmap='bwr')
            for i in range(6)
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
            # Fix aspect ratio
            ax.set_aspect('equal')

        # Create colorbars for the first three plots using the seventh subplot
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

        # Embed the figures in the Tk window
        self.canvas1 = FigureCanvasTkAgg(self.fig1, master=self.main_frame)
        self.canvas_widget1 = self.canvas1.get_tk_widget()
        self.canvas_widget1.grid(row=0, column=1, sticky="nsew")

        self.canvas2 = FigureCanvasTkAgg(self.fig2, master=self.main_frame)
        self.canvas_widget2 = self.canvas2.get_tk_widget()
        self.canvas_widget2.grid(row=1, column=1, sticky="nsew")

        self.canvas3 = FigureCanvasTkAgg(self.fig3, master=self.main_frame)
        self.canvas_widget3 = self.canvas3.get_tk_widget()
        self.canvas_widget3.grid(row=2, column=1, sticky="nsew")

        # For row 4, use the figure created based on the current dataset
        self.canvas4 = FigureCanvasTkAgg(self.fig4, master=self.main_frame)
        self.canvas_widget4 = self.canvas4.get_tk_widget()
        self.canvas_widget4.grid(row=3, column=1, sticky="nsew")

        # Frame for the sliders
        sliders_frame = ttk.Frame(self.main_frame, width=50, style="TFrame")
        sliders_frame.grid(row=0, column=2, rowspan=4, sticky="ns", padx=10, pady=10)
        self.main_frame.grid_columnconfigure(2, weight=0)

        # Create a vertical slider for the upper limit adjustment
        self.slider_vmax = ttk.Scale(
            sliders_frame,
            from_=2,
            to=0.01,
            orient='vertical',
            command=self.update_vmax,
            style="TScale"
        )
        self.slider_vmax.set(2)
        ttk.Label(sliders_frame, text="Övre gräns", background="black", foreground="white").pack()
        self.slider_vmax.pack(expand=True, fill=tk.Y, pady=(0, 10))

        # Create frame for the first row controls
        row1_controls = ttk.Frame(self.main_frame, style="TFrame")
        row1_controls.grid(row=0, column=0, sticky="ns", padx=5, pady=5)
        self.main_frame.grid_columnconfigure(0, weight=0)

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
            "K1: Base line (mni space)",
            "K1: Base line (pat space)"
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
        row2_controls = ttk.Frame(self.main_frame, style="TFrame")
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
        self.plot_dropdown2['values'] = ('K_2 (MNI space)', 'K_2 (pat space)')
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
        row3_controls = ttk.Frame(self.main_frame, style="TFrame")
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
        self.plot_dropdown3['values'] = ('K_1/K_2', 'Z-score',
                                         'K_1/K_2 (pat space)')
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

        # Create frame for the fourth row controls
        row4_controls = ttk.Frame(self.main_frame, style="TFrame")
        row4_controls.grid(row=3, column=0, sticky="ns", padx=5, pady=5)

        # Dropdown menu to select the dataset for the fourth row
        self.plot_var4 = tk.StringVar()
        self.plot_dropdown4 = ttk.Combobox(
            row4_controls,
            textvariable=self.plot_var4,
            state='readonly',
            width=25,
            style="TCombobox"
        )
        self.plot_dropdown4['values'] = self.datasets_row4
        self.plot_dropdown4.current(0)
        self.plot_dropdown4.grid(row=0, column=0, padx=5, pady=5)

        # Button to show the fourth row large
        self.show_large_button4 = ttk.Button(
            row4_controls,
            text="Visa stort",
            command=self.show_large_image_fig4,
            style="TButton"
        )
        self.show_large_button4.grid(row=1, column=0, padx=5, pady=5)

        self.fig1.tight_layout()
        self.fig2.tight_layout()
        self.fig3.tight_layout()
        self.fig4.tight_layout()
        self.canvas1.draw()
        self.canvas2.draw()
        self.canvas3.draw()
        self.canvas4.draw()

        # Bind dropdown change events
        self.plot_dropdown1.bind('<<ComboboxSelected>>', self.change_first_row)
        self.plot_dropdown2.bind('<<ComboboxSelected>>', self.change_second_row)
        self.plot_dropdown3.bind('<<ComboboxSelected>>', self.change_third_row)
        self.plot_dropdown4.bind('<<ComboboxSelected>>', self.change_fourth_row)

        # Inner frame to center buttons
        button_frame = ttk.Frame(bottom_frame, style="TFrame")
        button_frame.pack(side=tk.TOP, expand=True)

        # Create buttons for the button frame
        self.button_left = ttk.Button(
            button_frame,
            text="Spara som .nii",
            command=self.left_button_action,
            style="TButton"
        )
        self.button_left.pack(side=tk.LEFT, padx=20)

        self.button_middle = ttk.Button(
            button_frame,
            text="Spara som dicom",
            command=self.middle_button_action,
            style="TButton"
        )
        self.button_middle.pack(side=tk.LEFT, padx=20)

        self.button_right = ttk.Button(
            button_frame,
            text="Ny pat",
            command=self.right_button_action,
            style="TButton"
        )
        self.button_right.pack(side=tk.LEFT, padx=20)

        # **Add Window Management Commands Here**
        self.deiconify()           # Ensure the window is not minimized or hidden
        self.lift()                # Bring the window to the top
        self.focus_force()         # Focus on the App window
        self.grab_set()            # Make the App window modal (optional but recommended)
        self.update_idletasks()    # Process any pending idle tasks
        self.update()              # Force an update to render all widgets

        # **Release the grab to make the window interactive**
        self.grab_release()

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
        # array3=np.rot90(np.rot90(np.transpose(np.rot90(np.rot90(self.data3, axes=(1,2)), axes=(1,2)), (1,0,2))))

        affine_matrix = np.eye(4)
        arrays=[array1, array2]
        filenames=['K_1.nii', 'K_2.nii']
        save_as_nifti(arrays, filenames, affine=affine_matrix)
        # self.destroy()

    def middle_button_action(self):
        """Action for the middle button."""
        if self.button_var:
            self.button_var.set("Middle")
        # self.destroy()

    def right_button_action(self):
        """Action for the right button."""
        if self.button_var:
            self.button_var.set("Right")
        # self.destroy()

    def change_first_row(self, event):
        """Change the plot based on the selection from the first dropdown menu."""
        selection = self.plot_var1.get()
        print(f"First row selection changed to: {selection}")
        if selection == "K1: Base line (mni space)":
            for i in range(6):
                self.images1[i].set_data(self.channel_data1[i])
        elif selection == "K1: Base line (pat space)":
            for i in range(6):
                self.images1[i].set_data(self.channel_data5[i])

        self.canvas1.draw()

    def change_second_row(self, event):
        """Change the plot based on the selection from the second dropdown menu."""
        selection = self.plot_var2.get()
        print(f"Second row selection changed to: {selection}")
        if selection == 'K_2 (MNI space)':
            for i in range(6):
                self.images2[i].set_data(self.channel_data2[i])
                self.images2[i].set_cmap(self.cmap)
                self.images2[i].set_norm(self.norm)
            self.cbar2.update_normal(self.images2[-1])
            self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
        elif selection == 'K_2 (pat space)':
            for i in range(6):
                self.images2[i].set_data(self.channel_data6[i])
                self.images2[i].set_cmap(self.cmap)
                self.images2[i].set_norm(self.norm)
            self.cbar2.update_normal(self.images2[-1])
            self.cbar2.set_label('ml/min/g', rotation=270, labelpad=8, color='white', fontsize=8)
        self.canvas2.draw()

    def change_third_row(self, event):
        """Change the plot based on the selection from the third dropdown menu."""
        selection = self.plot_var3.get()
        print(f"Third row selection changed to: {selection}")
        if selection == 'K_1/K_2':
            for i in range(6):
                self.images3[i].set_data(self.channel_data3[i])
                self.images3[i].set_cmap('bwr')
                self.images3[i].set_norm(self.norm3)
            self.cbar3.update_normal(self.images3[-1])
            self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
        elif selection == 'Z-score':
            for i in range(6):
                self.images3[i].set_data(self.channel_data4[i])
                self.images3[i].set_cmap(custom_cmap)
                self.images3[i].set_norm(self.norm4)
            self.cbar3.update_normal(self.images3[-1])
            self.cbar3.set_label('Z-score', rotation=270, labelpad=8, color='white', fontsize=8)
        elif selection == 'K_1/K_2 (pat space)':
            for i in range(6):
                self.images3[i].set_data(self.channel_data7[i])
                self.images3[i].set_cmap('bwr')
                self.images3[i].set_norm(self.norm3)
            self.cbar3.update_normal(self.images3[-1])
            self.cbar3.set_label('Value', rotation=270, labelpad=8, color='white', fontsize=8)
        self.canvas3.draw()

    def change_fourth_row(self, event):
        """Change the plot based on the selection from the fourth dropdown menu."""
        selection = self.plot_var4.get()
        print(f"Fourth row selection changed to: {selection}")
        self.current_dataset_row4 = selection

        if self.current_dataset_row4 == 'SSP':
            norm = self.norm_row4
        else:
            norm = None  # For 'SSP Z-score', norm is not used

        # Update the figure in place
        images = create_custom_figure(
            self.first_values_yz_neg_x0, self.first_values_yz_pos_x1, self.first_values_yz_pos_x2,
            self.first_values_yz_neg_x2, self.first_values_xz_pos_y2, self.first_values_xz_neg_y2,
            self.last_figure_1, self.last_figure_2, self.last_figure_3,
            self.last_figure_4, self.last_figure_5, self.last_figure_6,
            self.regions_first_values_yz_neg_x0, self.regions_first_values_yz_pos_x1, 
            self.regions_first_values_yz_pos_x2, self.regions_first_values_yz_neg_x2,
            self.regions_first_values_xz_pos_y2, self.regions_first_values_xz_neg_y2,
            self.current_dataset_row4, norm=norm, fig=self.fig4
        )

        # Update the stored images
        if images:
            self.images_row4[self.current_dataset_row4] = images

        self.canvas4.draw()

    def update_vmax(self, value):
        """Adjust the colormap normalization based on the upper limit slider."""
        vmax = float(value)
        print(f"Updating vmax to: {vmax}")
        self.norm.vmax = vmax
        self.norm_row4.vmax = vmax  # Update norm for SSP figures
        self.update_plots()

    def update_plots(self):
        """Update the normalization across plots that respond to the slider."""
        print("Updating plots with new normalization.")
        # Update images that use self.norm
        for img in self.images1:
            img.set_norm(self.norm)
        selection2 = self.plot_var2.get()
        if selection2 in ['K_2 (MNI space)', 'K_2 (pat space)']:
            for img in self.images2:
                img.set_norm(self.norm)
            self.cbar2.update_normal(self.images2[-1])
        # Update colorbars
        self.cbar1.update_normal(self.images1[-1])
        self.canvas1.draw()
        self.canvas2.draw()
        # Update SSP images if applicable
        if self.current_dataset_row4 == 'SSP':
            images = self.images_row4['SSP']
            for img in images:
                img.set_norm(self.norm_row4)
            self.canvas4.draw()

    def show_large_image(self, axes, colorbar=None):
        """Open a new window to display a larger version of the images in the selected row with a colorbar (if provided)."""
        print("Opening large image window...")
        # Create a new window for displaying the large images
        large_image_window = tk.Toplevel(self)
        large_image_window.title("Large Images")
        large_image_window.configure(bg="black")
        fig = Figure(figsize=(16, 5), facecolor='black')

        # Adjust GridSpec depending on whether we have a colorbar
        if colorbar:
            gs = GridSpec(1, len(axes) + 1, width_ratios=[1] * len(axes) + [0.05], figure=fig)
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
            im = ax.imshow(img_data, cmap=cmap, norm=norm, interpolation='bicubic')
            ax.axis('off')
            # Fix aspect ratio
            ax.set_aspect('equal')

            large_axes.append(im)

        # Add the colorbar to the figure if provided
        if colorbar:
            cbar_ax = fig.add_subplot(gs[0, len(axes)])
            cbar = fig.colorbar(large_axes[-1], cax=cbar_ax, orientation='vertical')
            cbar.set_label(colorbar.ax.get_ylabel(), rotation=270, labelpad=15, color='white', fontsize=12)

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

    def show_large_image_fig4(self):
        """Display the large version of the fourth figure."""
        print("Opening large image for figure 4...")
        large_image_window = tk.Toplevel(self)
        large_image_window.title("Large Image")
        large_image_window.configure(bg="black")

        # Create the figure with larger size
        fig_large = Figure(figsize=(16, 5), facecolor='black')

        if self.current_dataset_row4 == 'SSP':
            norm = self.norm_row4
        else:
            norm = None  # For 'SSP Z-score', norm is not used

        # Create the figure anew
        create_custom_figure(
            self.first_values_yz_neg_x0, self.first_values_yz_pos_x1, self.first_values_yz_pos_x2,
            self.first_values_yz_neg_x2, self.first_values_xz_pos_y2, self.first_values_xz_neg_y2,
            self.last_figure_1, self.last_figure_2, self.last_figure_3,
            self.last_figure_4, self.last_figure_5, self.last_figure_6,
            self.regions_first_values_yz_neg_x0, self.regions_first_values_yz_pos_x1, 
            self.regions_first_values_yz_pos_x2, self.regions_first_values_yz_neg_x2,
            self.regions_first_values_xz_pos_y2, self.regions_first_values_xz_neg_y2,
            self.current_dataset_row4, norm=norm, fig=fig_large
        )

        # Create a canvas to hold the figure and embed it in the new window
        canvas = FigureCanvasTkAgg(fig_large, master=large_image_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        fig_large.tight_layout()
        canvas.draw()

def open_app_window(initial_window, button_var,
                    transformed_K_1_1, transformed_K_2_1, Z_brain, K_1_reshape_list_1,
                    K_2_reshape_list_1, first_values_yz_neg_x0, first_values_yz_pos_x1,
                    first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2,
                    first_values_xz_neg_y2,
                    last_figure_1, last_figure_2, last_figure_3,
                    last_figure_4, last_figure_5, last_figure_6, 
                    regions_first_values_yz_neg_x0, regions_first_values_yz_pos_x1, 
                    regions_first_values_yz_pos_x2, regions_first_values_yz_neg_x2,
                    regions_first_values_xz_pos_y2, regions_first_values_xz_neg_y2):
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
    app = App(transformed_K_1_1, transformed_K_2_1, Z_brain, K_1_reshape_list_1,
              K_2_reshape_list_1, first_values_yz_neg_x0, first_values_yz_pos_x1,
              first_values_yz_pos_x2, first_values_yz_neg_x2, first_values_xz_pos_y2,
              first_values_xz_neg_y2,
              last_figure_1, last_figure_2, last_figure_3,
              last_figure_4, last_figure_5, last_figure_6,
              regions_first_values_yz_neg_x0, regions_first_values_yz_pos_x1, 
              regions_first_values_yz_pos_x2, regions_first_values_yz_neg_x2, 
              regions_first_values_xz_pos_y2, regions_first_values_xz_neg_y2, 
              master=initial_window, button_var=button_var)
    print("App window created.")

    return app
