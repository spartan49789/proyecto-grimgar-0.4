import tkinter as tk
from tkinter import messagebox
import pickle
import os

from Admin import Admin_menu
from SaveAndLoadShit import save_user_list, load_user_list
from Chats.User import User, AsignedPC
from PCStorage.PCAsignment import start_pc_creation
from EnterAsCharacter import enter_as_character

# Log in functionality
def login_verify(username, password, user_list):

    for user in user_list:
        if user.Name == username:
            if user.Password == password:
                return user
            else:
                return None
    return None

# Sign up functionality
def create_user(username, password1, password2, user_list):

    if password1 != password2:
        return "Passwords do not match!"
    if password1== "" or password2== "" or username == "":
        return "Introduce something"

    for user in user_list:
        if user.Name == username:
            return "Username already exists!"

    new_user = User(len(user_list) + 1)
    new_user.Name = username
    new_user.Password = password1
    user_list.append(new_user)
    save_user_list(user_list)
    return "User created successfully!"

# GUI setup
def main_window():
    user_list = load_user_list()
    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()

    def toggle_fullscreen(event=None):
        is_fullscreen = window.attributes("-fullscreen")
        window.attributes("-fullscreen", not is_fullscreen)

    def adaptive_font(widget, height_ratio):
        widget_height = widget.winfo_height()
        font_size = int(widget_height * height_ratio)
        widget.config(font=("Arial", font_size))

    def show_login():
        clear_window()
        tk.Label(window, text="Username:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
        username_entry = tk.Entry(window)
        username_entry.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.05)

        tk.Label(window, text="Password:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
        password_entry = tk.Entry(window, show="*")
        password_entry.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.05)

        def verify_login(event=None):
            username = username_entry.get()
            password = password_entry.get()
            user = login_verify(username, password, user_list)
            if user:
                messagebox.showinfo("Login Success", f"Welcome, {user.Name}!")
                show_user_menu(user)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        verify_button = tk.Button(window, text="Verify", command=verify_login)
        verify_button.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.05)

        cancel_button = tk.Button(window, text="Cancel", command=main_window)
        cancel_button.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.05)

        window.bind("<Return>", verify_login)

    def show_signup():
        clear_window()
        tk.Label(window, text="Create Username:").place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.05)
        username_entry = tk.Entry(window)
        username_entry.place(relx=0.4, rely=0.25, relwidth=0.2, relheight=0.05)

        tk.Label(window, text="Password:").place(relx=0.4, rely=0.3, relwidth=0.2, relheight=0.05)
        password1_entry = tk.Entry(window, show="*")
        password1_entry.place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.05)

        tk.Label(window, text="Confirm Password:").place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.05)
        password2_entry = tk.Entry(window, show="*")
        password2_entry.place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.05)

        def verify_signup(event=None):
            username = username_entry.get()
            password1 = password1_entry.get()
            password2 = password2_entry.get()
            result = create_user(username, password1, password2, user_list)
            if result == "User created successfully!":
                messagebox.showinfo("Success", result)
                show_login()
            else:
                messagebox.showerror("Error", result)

        verify_button = tk.Button(window, text="Verify", command=verify_signup)
        verify_button.place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.05)

        cancel_button = tk.Button(window, text="Cancel", command=main_window)
        cancel_button.place(relx=0.4, rely=0.65, relwidth=0.2, relheight=0.05)

        window.bind("<Return>", verify_signup)

    def show_user_menu(user):
        clear_window()

        # Button dimensions
        button_width = 0.3
        button_height = 0.1

        # Centering buttons
        x_center = 0.35

        if user.SecurityLevel <= 0:
            tk.Button(window, text="Manage Users").place(relx=x_center, rely=0.2, relwidth=button_width, relheight=button_height)
        if user.SecurityLevel <= 1:
            tk.Button(window, text="Manage Game", command=lambda: Admin_menu(window, user, show_user_menu, user_list)).place(relx=x_center, rely=0.35, relwidth=button_width, relheight=button_height)
        if user.SecurityLevel <= 3:
            tk.Button(window, text="Direct Messages").place(relx=x_center, rely=0.5, relwidth=button_width, relheight=button_height)

            # PC buttons
            pc_frame = tk.Frame(window, bg=window.cget("bg"))
            pc_frame.place(relx=x_center, rely=0.65, relwidth=button_width, relheight=button_height)

            for i in range(3):  # Loop over the 3 possible PCs
                if user.PCs[i]:
                    tk.Button(
                        pc_frame,
                        text=user.PCs[i].Name,
                        command=lambda i=i: enter_as_character(window, user, i, show_user_menu)
                    ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                else:
                    tk.Button(
                        pc_frame,
                        text="Empty Slot",
                        command=lambda i=i: start_pc_creation(window, user, i, show_user_menu, user_list)
                    ).pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        if user.SecurityLevel <= 2:
            tk.Button(window, text="Enter as a Narrator").place(relx=x_center, rely=0.8, relwidth=button_width, relheight=button_height)

        logoff_button = tk.Button(window, text="Log Off", command=main_window)
        logoff_button.place(relx=0.9, rely=0.05, relwidth=0.1, relheight=0.05)

        info_button = tk.Button(window, text="Info")
        info_button.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.1)

        settings_button = tk.Button(window, text="Settings")
        settings_button.place(relx=0.1, rely=0.05, relwidth=0.1, relheight=0.1)

    clear_window()
    tk.Button(window, text="Log In", command=show_login).place(relx=0.4, rely=0.35, relwidth=0.2, relheight=0.05)
    tk.Button(window, text="Sign Up", command=show_signup).place(relx=0.4, rely=0.45, relwidth=0.2, relheight=0.05)
    tk.Button(window, text="Exit", command=window.quit).place(relx=0.4, rely=0.55, relwidth=0.2, relheight=0.05)

    window.bind("<Escape>", toggle_fullscreen)

    

# Main application window
window = tk.Tk()
window.title("User Login System")
window.geometry("300x200")
window.configure(bg="black")
window.attributes("-fullscreen", True)
main_window()
window.mainloop()