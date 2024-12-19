import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from SaveAndLoadShit import save_Location_list, load_Location_list, save_chat_list, load_chat_list, load_pc_list, save_pc_list

import pickle
import os

from Chats.Chats import Chat
from Chats.Message import Message
from Chats.Location import Location

def saveChat(chat, chat_list):
    chat_list[chat.CK] = chat
    save_chat_list(chat_list)

def Access_Admin_menu(window, user, show_user_menu, user_list):
    from Admin import Admin_menu
    Admin_menu(window, user, show_user_menu, user_list)

def Chat_Management_Menu(window, user, show_user_menu, user_list):
    location_list = load_Location_list()
    chat_list = load_chat_list()

    for widget in window.winfo_children():
        widget.destroy()

    button_width = 0.25
    x_center = 0.35

    tk.Button(
        window,
        text="Create Location Chat",
        command=lambda: create_location_chat(window, location_list, chat_list, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.2, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Create Group Chat",
        command=lambda: create_group_chat(window, user_list, chat_list, user, show_user_menu)
    ).place(relx=x_center, rely=0.35, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Create Info Chat",
        command=lambda: create_info_chat(window, user_list, chat_list, user, show_user_menu)
    ).place(relx=x_center, rely=0.5, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="View Chats",
        command=lambda: view_chats(window, chat_list, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.65, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Go Back",
        command=lambda: Access_Admin_menu(window, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.8, relwidth=button_width, relheight=0.1)

def create_location_chat(window, location_list, chat_list, user, show_user_menu, user_list):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Enter Location Name:").pack()
    location_name_entry = tk.Entry(window)
    location_name_entry.pack()

    tk.Label(window, text="Select Parent Location (if any):").pack()
    parent_location = tk.StringVar(window)
    parent_location.set("None")
    parent_menu = tk.OptionMenu(window, parent_location, *["None"] + [loc.LK for loc in location_list])
    parent_menu.pack()

    def create():
        location_name = location_name_entry.get()
        parent_lk = parent_location.get()
        parent_loc = next((loc for loc in location_list if loc.LK == parent_lk), None)

        new_location = Location(location_name, parent_loc)
        location_list.append(new_location)

        new_chat = Chat(len(chat_list) + 1, location_name, new_location)
        new_chat.Topic = "Roleplay"
        chat_list.append(new_chat)

        save_chat_list(chat_list)
        save_Location_list(location_list)

        messagebox.showinfo("Success", f"Location '{location_name}' and its chat were created!")
        Chat_Management_Menu(window, user, show_user_menu, user_list)

    tk.Button(window, text="Create", command=create).pack()
    tk.Button(window, text="Cancel", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)).pack()

def create_group_chat(window, user_list, chat_list, user, show_user_menu):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Enter Group Chat Name:").pack()
    group_name_entry = tk.Entry(window)
    group_name_entry.pack()

    def create():
        group_name = group_name_entry.get()
        new_chat = Chat(len(chat_list) + 1, group_name)
        new_chat.Topic = "Group"
        new_chat.Users = user_list
        chat_list.append(new_chat)
        save_chat_list(chat_list)

        messagebox.showinfo("Success", f"Group chat '{group_name}' was created!")
        Chat_Management_Menu(window, user, show_user_menu, user_list)

    tk.Button(window, text="Create", command=create).pack()
    tk.Button(window, text="Cancel", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)).pack()

def create_info_chat(window, user_list, chat_list, user, show_user_menu):
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Enter Info Chat Name:").pack()
    info_name_entry = tk.Entry(window)
    info_name_entry.pack()

    def create():
        info_name = info_name_entry.get()
        new_chat = Chat(len(chat_list) + 1, info_name)
        new_chat.Topic = "Info"
        new_chat.Users = [u for u in user_list if u.SecurityLevel <= 1]
        chat_list.append(new_chat)
        save_chat_list(chat_list)

        messagebox.showinfo("Success", f"Info chat '{info_name}' was created!")
        Chat_Management_Menu(window, user, show_user_menu, user_list)

    tk.Button(window, text="Create", command=create).pack()
    tk.Button(window, text="Cancel", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)).pack()

def view_chats(window, chat_list, user, show_user_menu, user_list):
    PC_list = load_pc_list()
    """View chats grouped by type with dynamic layout."""
    for widget in window.winfo_children():
        widget.destroy()

    # Create three frames: left, center, right
    left_frame = tk.Frame(window)
    left_frame.configure(bg="gray17")
    left_frame.place(relwidth=0.3, relheight=1.0, relx=0, rely=0)

    center_frame = tk.Frame(window)
    center_frame.configure(bg="gray17")
    center_frame.place(relwidth=0.5, relheight=1.0, relx=0.3, rely=0)

    right_frame = tk.Frame(window)
    right_frame.configure(bg="gray17")
    right_frame.place(relwidth=0.2, relheight=1.0, relx=0.8, rely=0)

    # Create a canvas in center frame for scrolling messages
    canvas = tk.Canvas(center_frame)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar = tk.Scrollbar(center_frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.config(yscrollcommand=scrollbar.set)

    # Frame within canvas to hold messages
    message_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=message_frame, anchor="nw")

    # Variable to hold the currently selected chat
    current_chat = None

    def display_chat_details(chat):
        nonlocal current_chat
        current_chat = chat

        # Clear current frames
        for widget in message_frame.winfo_children():
            widget.destroy()

        for widget in right_frame.winfo_children():
            widget.destroy()

        # Show chat messages in center
        for i, message in enumerate(chat.Messages):
            msg_frame = tk.Frame(message_frame)
            msg_frame.pack(fill="x", pady=5)

            tk.Label(msg_frame, text=message.Sender+": "+message.Body, width=40, anchor="w").pack(side="left", fill="x")
            tk.Button(msg_frame, text="Delete", command=lambda msg=message: delete_message(msg, chat)).pack(side="right")

        # Update right frame with chat details
        tk.Label(right_frame, text=f"Topic: {chat.Topic}", anchor="w").pack(fill="x")
        tk.Label(right_frame, text=f"Users: {', '.join([user.Name for user in chat.Users])}", anchor="w").pack(fill="x")

        # Add User/PC button (based on chat type)
        tk.Label(right_frame, text="Select User or PC to Add:").pack(fill="x", pady=5)

        user_pc_listbox = tk.Listbox(right_frame)

        if chat.Topic == "Roleplay":
            # Only show PCs if the chat is Roleplay
            for pc in PC_list:
                user_pc_listbox.insert(tk.END, f"{pc.Creature.CN} {pc.Creature.Name}")  # Display PC CN and Name
        else:
            # Show users if the chat is not Roleplay
            for user in user_list:
                user_pc_listbox.insert(tk.END, f"{user.UK} {user.Name}")  # Display User CN and Name

        user_pc_listbox.pack(fill="x", pady=5)

        def add_user_pc():
            selected = user_pc_listbox.get(tk.ACTIVE)

            # Split to get CN and Name for users/PCs
            selected_parts = selected.split(" ", 1)
            selected_cn = selected_parts[0]
            selected_name = selected_parts[1] if len(selected_parts) > 1 else None

            # Check if it's a user or PC
            if selected_cn in [user.UK for user in user_list]:
                # It's a user
                user_to_add = next((u for u in user_list if u.UK == selected_cn), None)
                if user_to_add and user_to_add not in chat.Users:  # Ensure user is not already added
                    chat.Users.append(user_to_add)
                    saveChat(chat, chat_list)
                    messagebox.showinfo("Success", f"User {selected_cn} {selected_name} added to the chat.")
                else:
                    messagebox.showerror("Error", "User already added or not found!")
            elif selected_cn in [pc.Creature.CN for pc in PC_list]:
                # It's a PC and the topic is Roleplay
                if chat.Topic == "Roleplay":
                    pc_to_add = next((pc for pc in PC_list if pc.Creature.CN == selected_cn), None)
                    if pc_to_add and pc_to_add not in chat.Users:  # Ensure PC is not already added
                        chat.Users.append(pc_to_add)
                        saveChat(chat, chat_list)
                        messagebox.showinfo("Success", f"PC {selected_cn} {selected_name} added to the chat.")
                    else:
                        messagebox.showerror("Error", "PC already added or not found!")
                else:
                    messagebox.showerror("Error", "Only PCs can be added to a Roleplay chat.")
            else:
                messagebox.showerror("Error", "Selected user or PC not found!")

            user_pc_listbox.delete(user_pc_listbox.curselection())  # Remove selected user/PC from the list

        tk.Button(right_frame, text="Add Selected", command=add_user_pc).pack(fill="x", pady=5)

        # Change Chat Type Section
        tk.Label(right_frame, text="Select Chat Type:").pack(fill="x", pady=5)

        chat_type_listbox = tk.Listbox(right_frame)
        chat_type_listbox.insert(tk.END, "Info")
        chat_type_listbox.insert(tk.END, "Group")
        chat_type_listbox.insert(tk.END, "Roleplay")
        chat_type_listbox.pack(fill="x", pady=5)

        def change_chat_type():
            selected_type = chat_type_listbox.get(tk.ACTIVE)
            if selected_type:
                chat.Topic = selected_type
                saveChat(chat, chat_list)
                messagebox.showinfo("Success", f"Chat type changed to {selected_type}.")
                display_chat_details(chat)

        tk.Button(right_frame, text="Change Type", command=change_chat_type).pack(fill="x", pady=5)

        # Delete Chat Button
        def delete_chat():
            confirm = messagebox.askyesno("Delete Chat", f"Are you sure you want to delete the chat '{chat.Name}'?")
            if confirm:
                chat_list.remove(chat)  # Remove chat from the list
                save_chat_list(chat_list)  # Save the updated chat list to file
                messagebox.showinfo("Success", f"Chat '{chat.Name}' deleted successfully.")
                view_chats(window, chat_list, user, show_user_menu, user_list)  # Refresh the chat list

        tk.Button(right_frame, text="Delete Chat", command=delete_chat).pack(fill="x", pady=5)

    def delete_message(message, chat):
        """Delete a message from the chat."""
        chat.Messages.remove(message)
        saveChat(chat, chat_list)
        messagebox.showinfo("Success", "Message deleted successfully.")
        display_chat_details(chat)

    def show_chat(chat):
        """Display the selected chat."""
        display_chat_details(chat)

    # Left frame buttons to select a chat
    for chat in chat_list:
        button = tk.Button(left_frame, text=chat.Name, command=lambda chat=chat: show_chat(chat))
        button.pack(fill="x", pady=5)

    # Add Go Back Button at the bottom of the left frame
    go_back_button = tk.Button(left_frame, text="Go Back", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list))
    go_back_button.pack(side="bottom", fill="x", pady=10)

    # Update scrollregion after adding all messages
    message_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))