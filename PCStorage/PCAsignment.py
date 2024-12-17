from tkinter import *
from tkinter import messagebox
from Classes.PC import PC
from PCStorage.PCStorageManage import save_pc_list, load_pc_list

def start_pc_creation(window, user, pc_slot_index, save_user_list, show_user_menu):
    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    ChK = len(load_pc_list())+1
    # Title
    Label(window, text="PC Creation", font=("Arial", 20)).place(relx=0.4, rely=0.1, relwidth=0.3, relheight=0.1)

    # PC Name Entry
    Label(window, text="Enter PC Name:").place(relx=0.35, rely=0.3, relwidth=0.2, relheight=0.05)
    name_entry = Entry(window)
    name_entry.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.05)

    # Race Selection
    Label(window, text="Select Race:").place(relx=0.35, rely=0.4, relwidth=0.2, relheight=0.05)
    race_var = StringVar(window)
    race_var.set("Human")  # Default race
    races = ["Human", "Elf", "Orc", "Lizardman", "Centaur", "Dragon", "Young Dragon", "Wyvern"]
    race_dropdown = OptionMenu(window, race_var, *races)
    race_dropdown.place(relx=0.5, rely=0.4, relwidth=0.2, relheight=0.05)

    # Function to create a PC
    def create_pc():
        pc_name = name_entry.get().strip()
        pc_race = race_var.get()

        if not pc_name:
            messagebox.showerror("Error", "PC name cannot be empty!")
            return

        # Create a new PC and assign it
        new_pc = PC(ChK)
        new_pc.Creature.Name = pc_name
        new_pc.Creature.Race = pc_race
        new_pc.Creature.RefreshRM()

        user.PCs[pc_slot_index] = new_pc.AsignPC()
        save_pc_list()  # Save the updated user list
        messagebox.showinfo("Success", f"PC '{pc_name}' created successfully!")
        show_user_menu(user)  # Return to the user menu

    # Create PC Button
    Button(window, text="Create PC", command=create_pc).place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.05)

    # Cancel Button
    Button(window, text="Cancel", command=lambda: show_user_menu(user)).place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.05)