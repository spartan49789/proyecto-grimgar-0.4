import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from SaveAndLoadShit import save_Location_list, load_Location_list, save_chat_list, load_chat_list, load_pc_list, save_pc_list
import pickle
import os

from Chats.Chats import Chat
from Chats.Message import Message
from Chats.Location import Location



def Admin_menu(window, user, show_user_menu, user_list):
    location_list = load_Location_list()
    chat_list = load_chat_list()
    """Admin menu that includes a button to manage chats."""
    for widget in window.winfo_children():
        widget.destroy()

    button_width = 0.2
    x_center = 0.4

    # Chat Management Button
    tk.Button(
        window,
        text="Chat Management",
        command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.3, relwidth=button_width, relheight=0.1)

    # Go Back Button
    tk.Button(
        window,
        text="Go Back",
        command=lambda: show_user_menu(user)
    ).place(relx=x_center, rely=0.5, relwidth=button_width, relheight=0.1)

    # Exit Button
    tk.Button(
        window,
        text="Exit",
        command=window.quit
    ).place(relx=x_center, rely=0.7, relwidth=button_width, relheight=0.1)


def Chat_Management_Menu(window, user, show_user_menu, user_list):
    """Menu for managing chats."""
    location_list = load_Location_list()
    chat_list = load_chat_list()

    for widget in window.winfo_children():
        widget.destroy()

    button_width = 0.25
    x_center = 0.35

    # Create Location Chat
    tk.Button(
        window,
        text="Create Location Chat",
        command=lambda: create_location_chat(window, location_list, chat_list, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.2, relwidth=button_width, relheight=0.1)

    # Create Group Chat
    tk.Button(
        window,
        text="Create Group Chat",
        command=lambda: create_group_chat(window, user_list, chat_list, user, show_user_menu)
    ).place(relx=x_center, rely=0.35, relwidth=button_width, relheight=0.1)

    # Create Info Chat
    tk.Button(
        window,
        text="Create Info Chat",
        command=lambda: create_info_chat(window, user_list, chat_list, user, show_user_menu)
    ).place(relx=x_center, rely=0.5, relwidth=button_width, relheight=0.1)

    # View Chats
    tk.Button(
        window,
        text="View Chats",
        command=lambda: view_chats(window, chat_list, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.65, relwidth=button_width, relheight=0.1)

    # Go Back Button
    tk.Button(
        window,
        text="Go Back",
        command=lambda: Admin_menu(window, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=0.8, relwidth=button_width, relheight=0.1)




def create_location_chat(window, location_list, chat_list, user, show_user_menu, user_list):
    """Create a new location and its associated chat."""
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

        # Link Roleplay Chat to Location
        new_chat = Chat(len(chat_list) + 1, new_location)
        new_chat.Topic = "Roleplay"
        chat_list.append(new_chat)
        save_chat_list(chat_list)
        save_Location_list(location_list)

        messagebox.showinfo("Success", f"Location '{location_name}' and its chat were created!")
        Chat_Management_Menu(window, user, show_user_menu, user_list)

    tk.Button(window, text="Create", command=create).pack()
    tk.Button(window, text="Cancel", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)).pack()


def create_group_chat(window, user_list, chat_list, user, show_user_menu):
    """Create a group chat."""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Enter Group Chat Name:").pack()
    group_name_entry = tk.Entry(window)
    group_name_entry.pack()

    def create():
        group_name = group_name_entry.get()
        new_chat = Chat(len(chat_list) + 1)
        new_chat.Topic = "Group"
        new_chat.Users = user_list  # Add all users to the group chat
        chat_list.append(new_chat)
        save_chat_list(chat_list)

        messagebox.showinfo("Success", f"Group chat '{group_name}' was created!")
        Chat_Management_Menu(window, user, show_user_menu, user_list)

    tk.Button(window, text="Create", command=create).pack()
    tk.Button(window, text="Cancel", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)).pack()



def create_info_chat(window, user_list, chat_list, user, show_user_menu):
    """Create an information chat."""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Enter Info Chat Name:").pack()
    info_name_entry = tk.Entry(window)
    info_name_entry.pack()

    def create():
        info_name = info_name_entry.get()
        new_chat = Chat(len(chat_list) + 1)
        new_chat.Topic = "Info"
        new_chat.Users = [u for u in user_list if u.SecurityLevel <= 1]  # Restrict to specific users
        chat_list.append(new_chat)

        messagebox.showinfo("Success", f"Info chat '{info_name}' was created!")
        save_chat_list(chat_list)
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
        """Display chat details in the right frame and messages in center."""
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

            tk.Label(msg_frame, text=message.Content, width=40, anchor="w").pack(side="left", fill="x")
            tk.Button(msg_frame, text="Delete", command=lambda msg=message: delete_message(msg, chat)).pack(side="right")

        # Update right frame with chat details
        tk.Label(right_frame, text=f"Topic: {chat.Topic}", anchor="w").pack(fill="x")
        tk.Label(right_frame, text=f"Users: {', '.join([user.Username for user in chat.Users])}", anchor="w").pack(fill="x")
        # Additional chat settings (for example, modify topic)
        tk.Button(right_frame, text="Change Topic", command=lambda: change_chat_topic(chat)).pack(fill="x")
        tk.Button(right_frame, text="Add User", command=lambda: add_user_to_chat(chat, user_list, PC_list)).pack(fill="x")

    def change_chat_topic(chat):
        """Change the topic of the selected chat."""
        new_topic = simpledialog.askstring("Change Topic", "Enter new topic:")
        if new_topic:
            chat.Topic = new_topic
            messagebox.showinfo("Success", "Topic changed successfully.")
            display_chat_details(chat)

    def add_user_to_chat(chat, user_list, PC_list):
        """Add a user or PC to the chat."""
        if chat.Topic == "Info":
            # Select from PCs list
            selected_pc = simpledialog.askstring("Add PC", "Enter PC code to add:")
            if selected_pc:
                pc_to_add = next((pc for pc in PC_list if pc.CN == selected_pc), None)
                if pc_to_add:
                    chat.Users.append(pc_to_add.CHK)  # Append PC's CHK
                    messagebox.showinfo("Success", f"PC {selected_pc} added to the chat.")
                    display_chat_details(chat)
                else:
                    messagebox.showerror("Error", "PC not found!")
        else:
            # Select from User list
            selected_user = simpledialog.askstring("Add User", "Enter username to add:")
            if selected_user:
                user_to_add = next((u for u in user_list if u.Username == selected_user), None)
                if user_to_add:
                    chat.Users.append(user_to_add.UK)  # Append User's UK
                    messagebox.showinfo("Success", f"User {selected_user} added to the chat.")
                    display_chat_details(chat)
                else:
                    messagebox.showerror("Error", "User not found!")

    def delete_message(message, chat):
        chat.Messages.remove(message)
        messagebox.showinfo("Success", "Message deleted successfully.")
        display_chat_details(chat)

    def show_chat(chat):
        display_chat_details(chat)

    # Left frame buttons to select a chat
    for chat in chat_list:
        button = tk.Button(left_frame, text=f"Chat ID: {chat.CK}", command=lambda chat=chat: show_chat(chat))
        button.pack(fill="x", pady=5)

    # Add Go Back Button at the bottom of the left frame
    go_back_button = tk.Button(left_frame, text="Go Back", command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list))
    go_back_button.pack(side="bottom", fill="x", pady=10)

    # Update scrollregion after adding all messages
    message_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))


