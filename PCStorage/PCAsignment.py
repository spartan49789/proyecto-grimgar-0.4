from tkinter import *
from tkinter import messagebox
from Classes.PC import PC
from PCStorage.PCStorageManage import save_pc_list, load_pc_list
import tkinter as tk
import time

def start_pc_creation(window, user, pc_slot_index, show_user_menu):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()
    pc_list = load_pc_list()
    ChK = len(pc_list) + 1
    # Title
    Label(window, text="PC Creation", font=("Arial", 20)).place(relx=0.4, rely=0.05, relwidth=0.3, relheight=0.1)  # Moved title up

    # PC Name Entry
    Label(window, text="Enter PC Name:").place(relx=0.35, rely=0.2, relwidth=0.2, relheight=0.05)  # Moved label up
    name_entry = Entry(window)
    name_entry.place(relx=0.5, rely=0.2, relwidth=0.2, relheight=0.05)  # Moved entry up

    # Stat points
    stats = {
        "STR": 1.0,
        "CON": 1.0,
        "DEX": 1.0,
        "INT": 1.0,
        "WIS": 1.0,
        "CHA": 1.0
    }
    free_points = 2

    # Update the stat and free points, ensuring we don't go below zero for both stats and free points
    def update_stat(stat_name, amount):
        nonlocal free_points
        # Check valid conditions for updating stat and free points
        if stats[stat_name] + amount >= 1 and (free_points - amount >= 0 or amount < 0):  # Allow going down to 0 if needed
            stats[stat_name] += amount
            free_points -= amount
            # Ensure free points do not go below 0
            if free_points < 0:
                free_points = 0
            stat_labels[stat_name].config(text=f"{stat_name}: {stats[stat_name]:.2f}")
            free_points_label.config(text=f"Free Points: {free_points:.2f}")
            
            # Enable the create PC button when free points are exactly zero
            if free_points == 0:
                create_pc_button.config(state=tk.NORMAL)
            else:
                create_pc_button.config(state=tk.DISABLED)

    # Function to handle long-press for faster stat adjustment
    def hold_stat_button(stat_name, amount):
        nonlocal free_points
        update_stat(stat_name, amount)
        while free_points > 0 if amount > 0 else free_points < 2:
            update_stat(stat_name, amount)
            time.sleep(0.1)  # Adjust the speed of the update

    stat_labels = {}
    for idx, stat_name in enumerate(stats.keys()):
        # Display stat name and value
        stat_labels[stat_name] = Label(window, text=f"{stat_name}: {stats[stat_name]:.2f}")
        stat_labels[stat_name].place(relx=0.35, rely=0.3 + idx * 0.08, relwidth=0.2, relheight=0.05)  # Reduced vertical space
        
        # Increase and decrease buttons for each stat
        increase_button = Button(window, text="+", command=lambda sn=stat_name: update_stat(sn, 0.05), width=2, height=1)
        increase_button.place(relx=0.6, rely=0.3 + idx * 0.08, relwidth=0.05, relheight=0.05)

        decrease_button = Button(window, text="-", command=lambda sn=stat_name: update_stat(sn, -0.05), width=2, height=1)
        decrease_button.place(relx=0.65, rely=0.3 + idx * 0.08, relwidth=0.05, relheight=0.05)

        # Bind holding buttons for faster adjustments
        increase_button.bind("<Button-1>", lambda event, sn=stat_name: hold_stat_button(sn, 0.05))
        decrease_button.bind("<Button-1>", lambda event, sn=stat_name: hold_stat_button(sn, -0.05))

    # Free Points Label
    free_points_label = Label(window, text=f"Free Points: {free_points:.2f}")
    free_points_label.place(relx=0.35, rely=0.75, relwidth=0.2, relheight=0.05)

    # Function to create a PC
    def create_pc():
        pc_name = name_entry.get().strip()

        if not pc_name:
            messagebox.showerror("Error", "PC name cannot be empty!")
            return

        # Create a new PC and assign it
        new_pc = PC(ChK)
        new_pc.Creature.Name = pc_name
        new_pc.Creature.RefreshRM()

        # Assign the stats to the PC
        new_pc.Creature.Status.STR = stats["STR"]
        new_pc.Creature.Status.CON = stats["CON"]
        new_pc.Creature.Status.DEX = stats["DEX"]
        new_pc.Creature.Status.INT = stats["INT"]
        new_pc.Creature.Status.WIS = stats["WIS"]
        new_pc.Creature.Status.CHA = stats["CHA"]

        pc_list.append(new_pc)

        user.PCs[pc_slot_index] = new_pc.AsignPC()
        
        save_pc_list(pc_list)  # Save the updated user list
        messagebox.showinfo("Success", f"PC '{pc_name}' created successfully!")
        show_user_menu(user)  # Return to the user menu

    # Create PC Button (Initially disabled)
    create_pc_button = Button(window, text="Create PC", command=create_pc, state=tk.DISABLED)
    create_pc_button.place(relx=0.4, rely=0.85, relwidth=0.2, relheight=0.05)

    # Cancel Button
    Button(window, text="Cancel", command=lambda: show_user_menu(user)).place(relx=0.4, rely=0.95, relwidth=0.2, relheight=0.05)
