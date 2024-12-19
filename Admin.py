import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from SaveAndLoadShit import save_Location_list, load_Location_list, save_chat_list, load_chat_list, load_pc_list, save_pc_list
import pickle
import os


def Admin_menu(window, user, show_user_menu, user_list):
    from Management.ChatManagement import Chat_Management_Menu
    from Management.ItemManagement import ItemManagementMenu
    location_list = load_Location_list()
    chat_list = load_chat_list()
    for widget in window.winfo_children():
        widget.destroy()

    button_width = 0.2
    x_center = 0.4
    x_left = 0.2
    x_right = 0.6
    y_top = 0.2
    y_gap = 0.1

    # Manage Chats button at the center
    tk.Button(
        window,
        text="Manage Chats",
        command=lambda: Chat_Management_Menu(window, user, show_user_menu, user_list)
    ).place(relx=x_center, rely=y_top, relwidth=button_width, relheight=0.1)

    # Manage Creatures, Manage Items, Manage Characters buttons
    tk.Button(
        window,
        text="Manage Creatures",
        command=lambda: manage_creatures(window, user, show_user_menu, user_list)
    ).place(relx=x_left, rely=y_top + y_gap, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Manage Items",
        command=lambda: ItemManagementMenu(window, user, show_user_menu)
    ).place(relx=x_center, rely=y_top + y_gap, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Manage Characters",
        command=lambda: manage_characters(window, user, show_user_menu, user_list)
    ).place(relx=x_right, rely=y_top + y_gap, relwidth=button_width, relheight=0.1)

    # Go Back and Exit buttons side by side at the bottom
    tk.Button(
        window,
        text="Go Back",
        command=lambda: show_user_menu(user)
    ).place(relx=x_left, rely=y_top + 3 * y_gap, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Exit",
        command=window.quit
    ).place(relx=x_right, rely=y_top + 3 * y_gap, relwidth=button_width, relheight=0.1)


def manage_characters(window, user, show_user_menu, user_list):
    """Function to manage characters."""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Character Management").pack()
    # Add character management logic here, such as listing characters or adding new characters.
    tk.Button(window, text="Go Back", command=lambda: Admin_menu(window, user, show_user_menu, user_list)).pack()

def manage_creatures(window, user, show_user_menu, user_list):
    """Function to manage creatures."""
    for widget in window.winfo_children():
        widget.destroy()

    tk.Label(window, text="Creature Management").pack()
    # Add creature management logic here, such as listing creatures or adding new creatures.
    tk.Button(window, text="Go Back", command=lambda: Admin_menu(window, user, show_user_menu, user_list)).pack()

