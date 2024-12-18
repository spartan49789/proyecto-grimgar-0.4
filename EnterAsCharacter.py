import tkinter as tk
from tkinter import messagebox
import pickle
import os

from Chats.Message import Message
from SaveAndLoadShit import save_pc_list, load_pc_list, load_chat_list

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

    # Sample chat list
    chats = load_chat_list()

    # Update the left frame with chat buttons
    update_chat_buttons(left_frame, chats, lambda chat: enter_chat(chat, center_frame))

    def update_chat_buttons(left_frame, chats, enter_chat_callback):
        """Populate the left frame with buttons for each Roleplay chat."""
        for widget in left_frame.winfo_children():
            widget.destroy()  # Clear existing buttons

        for chat in chats:
            if chat['type'] == "Roleplay":  # Only create buttons for Roleplay chats
                button = tk.Button(left_frame, text=chat['name'], 
                                command=lambda chat=chat: enter_chat_callback(chat))
                button.pack(fill=tk.X, pady=5)

    def enter_chat(chat):
        """Handle entering a selected chat."""
        # Add code to display the chat in the center frame
        pass


def enter_chat(chat, center_frame):
    """Handle entering a selected chat."""
    display_chat_messages(center_frame, chat)
    send_message(center_frame, chat, sender="Character Name")

def display_chat_messages(center_frame, chat):
    """Display all messages for the selected chat in the center frame."""
    # Clear previous messages
    for widget in center_frame.winfo_children():
        widget.destroy()

    # Text widget for displaying messages
    message_display = tk.Text(center_frame, wrap=tk.WORD, height=20, width=50)
    message_display.pack(padx=5, pady=5)

    # Insert messages into the Text widget
    for message in chat['messages']:
        message_display.insert(tk.END, f"{message.Time} - {message.Sender}: {message.Body}\n")

    message_display.config(state=tk.DISABLED)  # Make the text widget read-only

def send_message(center_frame, chat, sender):
    """Send a message from the character to the selected chat."""
    # Entry widget for message input
    message_entry = tk.Entry(center_frame, width=40)
    message_entry.pack(padx=5, pady=5)

    def on_send():
        """Handle the message sending."""
        message_body = message_entry.get()
        if message_body.strip():  # Ensure the message isn't empty
            new_message = Message(MK=len(chat['messages']) + 1, 
                                  Sender=sender, 
                                  Chat=chat['name'], 
                                  Body=message_body)
            chat['messages'].append(new_message)
            display_chat_messages(center_frame, chat)  # Refresh message display

    # Bind the "Enter" key to send the message
    message_entry.bind("<Return>", lambda event: on_send())
    send_button = tk.Button(center_frame, text="Send", command=on_send)
    send_button.pack(pady=5)
