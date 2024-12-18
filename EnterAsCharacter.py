import tkinter as tk
from Chats.Message import Message
from SaveAndLoadShit import load_pc_list, load_chat_list
from Classes.PC import ShowSheet

def uniquePC(Assigned):
    pc_list = load_pc_list()
    for pc in pc_list:
        if Assigned.CK == pc.Creature.CN and Assigned.Name == pc.Creature.Name:
            return pc
        
def enter_as_character(window, user, slot, show_user_menu):
    Assigned = user.PCs[slot]
    PC = uniquePC(Assigned)

    # Clear the window
    for widget in window.winfo_children():
        widget.destroy()

    # Main Frame setup
    main_frame = tk.Frame(window, bg="grey17")
    main_frame.pack(fill="both", expand=True)

    # Left Frame (20%)
    left_frame = tk.Frame(main_frame, bg="grey")
    left_frame.pack(side=tk.LEFT, fill="y", padx=5, pady=5)

    # Center Frame (50%)
    center_frame = tk.Frame(main_frame, bg="darkgrey")
    center_frame.pack(side=tk.LEFT, fill="both", expand=True, padx=5, pady=5)

    # Right Frame (30%)
    right_frame = tk.Frame(main_frame, bg="grey")
    right_frame.pack(side=tk.LEFT, fill="y", padx=5, pady=5)

    # Load chats
    chats = load_chat_list()
    ShowSheet(PC, right_frame)
    # Update the left frame with chat buttons
    update_chat_buttons(left_frame, chats, lambda chat: enter_chat(chat, center_frame, PC), show_user_menu, user)

def update_chat_buttons(left_frame, chats, enter_chat_callback, show_user_menu, user):
    """Populate the left frame with buttons for each Roleplay chat."""
    for widget in left_frame.winfo_children():
        widget.destroy()  # Clear existing buttons

    for chat in chats:
        if chat.Topic == "Roleplay":  # Only show Roleplay chats
            button = tk.Button(left_frame, text=chat.Name, command=lambda chat=chat: enter_chat_callback(chat))
            button.pack(fill=tk.X, pady=5)

    go_back_button = tk.Button(left_frame, text="Go Back", command=lambda: show_user_menu(user))
    go_back_button.pack(side=tk.BOTTOM, fill=tk.X, padx=5, pady=5)

def enter_chat(chat, center_frame, PC):
    """Handle entering a selected chat."""
    # Clear the center frame before displaying the new chat
    for widget in center_frame.winfo_children():
        widget.destroy()
    
    # Display Chat Name Label at the Top
    chat_name_label = tk.Label(center_frame, text=chat.Name, font=("Arial", 16, "bold"), bg="darkgrey", fg="black")
    chat_name_label.pack(fill=tk.X, pady=5)

    # Display chat messages and input box
    display_chat_messages(center_frame, chat)
    send_message(center_frame, chat, sender=PC.Creature.Name)

def display_chat_messages(center_frame, chat):
    """Display all messages for the selected chat in the center frame."""
    # Clear previous messages
    for widget in center_frame.winfo_children():
        widget.destroy()

    # Text widget for displaying messages
    message_display = tk.Text(center_frame, wrap=tk.WORD, height=20, width=50)
    message_display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    # Insert messages into the Text widget
    for message in chat.Messages:
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
            new_message = Message(
                MK=len(chat.Messages) + 1, 
                Sender=sender, 
                Chat=chat.Name, 
                Body=message_body
            )
            chat.Messages.append(new_message)
            display_chat_messages(center_frame, chat)  # Refresh message display
            message_entry.delete(0, tk.END)  # Clear the entry field

    # Bind the "Enter" key to send the message
    message_entry.bind("<Return>", lambda event: on_send())
    send_button = tk.Button(center_frame, text="Send", command=on_send)
    send_button.pack(pady=5)

def adjust_window(window):
    """Ensure the frames take up full height and are properly proportioned."""
    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
    window.update_idletasks()


