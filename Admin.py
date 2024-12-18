import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from SaveAndLoadShit import save_Location_list, load_Location_list, save_chat_list, load_chat_list
import pickle
import os

from Chats.Chats import Chat
from Chats.Message import Message
from Chats.Location import Location

def Admin_menu(window, user, show_user_menu, user_list):
    location_list = load_Location_list()
    chat_list = load_chat_list()
    # Clear the current window
    for widget in window.winfo_children():
        widget.destroy()

    # Button layout
    button_width = 0.2
    button_height = 0.1

    # Center positions
    center_x = 0.4
    center_y = 0.3
    y_spacing = 0.15

    # Helper function to create a new location and linked chat
    def create_location():
        # Prompt for location details
        location_name = simpledialog.askstring("Create Location", "Enter the new location name:")
        if not location_name:
            messagebox.showerror("Error", "Location name cannot be empty!")
            return

        parent_location_name = simpledialog.askstring("Parent Location", "Enter the parent location name (or leave empty for none):")
        parent_location = None
        if parent_location_name:
            # Check if the parent location exists
            parent_location = next((loc for loc in location_list if loc.LK == parent_location_name), None)
            if not parent_location:
                messagebox.showerror("Error", "Parent location not found!")
                return

        # Create the new location
        new_location = Location(location_name, parent_location)
        location_list.append(new_location)

        # Link a Roleplay chat to the location
        new_chat = Chat(CK=len(chat_list) + 1, Location=new_location)
        new_chat.Topic = "Roleplay"
        chat_list.append(new_chat)

        messagebox.showinfo("Success", f"Location '{location_name}' and linked Roleplay chat created successfully!")

    # Helper function to create a group chat
    def create_group_chat():
        chat_name = simpledialog.askstring("Create Group Chat", "Enter the new group chat name:")
        if not chat_name:
            messagebox.showerror("Error", "Chat name cannot be empty!")
            return

        # Create a new group chat
        new_chat = Chat(CK=len(chat_list) + 1)
        new_chat.Topic = "Group"
        new_chat.Users = user_list  # Add all users to the group chat
        chat_list.append(new_chat)

        messagebox.showinfo("Success", f"Group chat '{chat_name}' created successfully!")

    # Helper function to create an information chat
    def create_info_chat():
        chat_name = simpledialog.askstring("Create Info Chat", "Enter the new info chat name:")
        if not chat_name:
            messagebox.showerror("Error", "Chat name cannot be empty!")
            return

        # Create a new info chat
        new_chat = Chat(CK=len(chat_list) + 1)
        new_chat.Topic = "Info"
        new_chat.Users = [u for u in user_list if u.SecurityLevel <= 1]  # Add only users with SecurityLevel 1 and 0
        chat_list.append(new_chat)

        messagebox.showinfo("Success", f"Info chat '{chat_name}' created successfully!")

    # Admin Menu Buttons
    tk.Button(
        window,
        text="Create New Location",
        command=create_location
    ).place(relx=center_x - 0.25, rely=0.2, relwidth=button_width, relheight=button_height)

    tk.Button(
        window,
        text="Create Group Chat",
        command=create_group_chat
    ).place(relx=center_x + 0.25, rely=0.2, relwidth=button_width, relheight=button_height)

    tk.Button(
        window,
        text="Create Info Chat",
        command=create_info_chat
    ).place(relx=center_x, rely=0.35, relwidth=button_width, relheight=button_height)

    # Go Back button
    tk.Button(
        window,
        text="Go Back",
        command=lambda: show_user_menu(user)
    ).place(relx=center_x - 0.25, rely=center_y + y_spacing, relwidth=button_width, relheight=button_height)

    # Exit button
    tk.Button(
        window,
        text="Exit",
        command=window.quit
    ).place(relx=center_x + 0.25, rely=center_y + y_spacing, relwidth=button_width, relheight=button_height)