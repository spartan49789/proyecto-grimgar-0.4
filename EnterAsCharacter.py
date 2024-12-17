import tkinter as tk
from tkinter import messagebox
import pickle
import os
from PCStorage.PCStorageManage import save_pc_list, load_pc_list

def uniquePC(Asigned):
    pc_list = load_pc_list()
    for pc in pc_list:
        if Asigned.CK == pc.CN and Asigned.Name == pc.Name:
            return pc

def enter_as_character(window, user, slot):
    Asigned = user.PCs[slot]
    PC = uniquePC(Asigned)

    main_frame = tk.Frame(window)

    left_frame = tk.Frame(main_frame, bg="grey")
    left_frame.pack(side="left", fill="y", padx=5)

    center_frame = tk.Frame(main_frame, bg="darkgrey")
    center_frame.pack(side="center", fill="y", padx=5)

    right_frame = tk.Frame(main_frame, bg="grey")
    center_frame.pack(side="right", fill="y", padx=5)
