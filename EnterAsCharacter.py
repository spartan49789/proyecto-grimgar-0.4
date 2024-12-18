import tkinter as tk
from tkinter import messagebox
import pickle
import os

from SaveAndLoadShit import save_pc_list, load_pc_list

def uniquePC(Asigned):
    pc_list = load_pc_list()
    for pc in pc_list:
        if Asigned.CK == pc.Creature.CN and Asigned.Name == pc.Creature.Name:
            return pc

def enter_as_character(window, user, slot, show_user_menu):
    Asigned = user.PCs[slot]
    PC = uniquePC(Asigned)

    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Main Frame setup
    main_frame = tk.Frame(window)
    main_frame.grid(row=0, column=0, sticky="nsew")

    # Configure the window grid to expand
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # Set column proportions
    main_frame.grid_columnconfigure(0, weight=2)  # Left frame (20%)
    main_frame.grid_columnconfigure(1, weight=5)  # Center frame (50%)
    main_frame.grid_columnconfigure(2, weight=3)  # Right frame (30%)
    main_frame.grid_rowconfigure(0, weight=1)  # Row fills the full height

    # Left Frame (20%)
    left_frame = tk.Frame(main_frame, bg="grey")
    left_frame.grid(row=0, column=0, sticky="ns", padx=5)

    # Go Back Button (bottom of left frame)
    go_back_button = tk.Button(left_frame, text="Go Back", command=lambda: show_user_menu(user))
    go_back_button.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

    # Center Frame (50%)
    center_frame = tk.Frame(main_frame, bg="darkgrey")
    center_frame.grid(row=0, column=1, sticky="nsew", padx=5)

    # Right Frame (30%)
    right_frame = tk.Frame(main_frame, bg="grey")
    right_frame.grid(row=0, column=2, sticky="ns", padx=5)

