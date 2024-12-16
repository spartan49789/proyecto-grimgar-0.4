import tkinter as tk
from tkinter import messagebox
import pickle
import os

# User class
class User:
    def __init__(self, UK):
        self.UK = UK
        self.Name = ""
        self.Password = ""
        self.SecurityLevel = 0  # 0: Owner, 1: Admin, 2: Narrator, 3: Player
        self.PCs = [None, None, None]  # Placeholder for PCs

# Load or initialize user list
USER_LIST_FILE = "user_list.pkl"

if os.path.exists(USER_LIST_FILE):
    with open(USER_LIST_FILE, "rb") as file:
        user_list = pickle.load(file)
else:
    user_list = []

# Helper functions
def save_user_list():
    with open(USER_LIST_FILE, "wb") as file:
        pickle.dump(user_list, file)

# Log in functionality
def login_verify(username, password):
    for user in user_list:
        if user.Name == username:
            if user.Password == password:
                return user
            else:
                return None
    return None

# Sign up functionality
def create_user(username, password1, password2):
    if password1 != password2:
        return "Passwords do not match!"

    for user in user_list:
        if user.Name == username:
            return "Username already exists!"

    new_user = User(len(user_list) + 1)
    new_user.Name = username
    new_user.Password = password1
    user_list.append(new_user)
    save_user_list()
    return "User created successfully!"

# GUI setup
def main_window():
    def clear_window():
        for widget in window.winfo_children():
            widget.destroy()

    def show_login():
        clear_window()
        tk.Label(window, text="Username:").pack()
        username_entry = tk.Entry(window)
        username_entry.pack()

        tk.Label(window, text="Password:").pack()
        password_entry = tk.Entry(window, show="*")
        password_entry.pack()

        def verify_login(event=None):
            username = username_entry.get()
            password = password_entry.get()
            user = login_verify(username, password)
            if user:
                messagebox.showinfo("Login Success", f"Welcome, {user.Name}!")
                show_user_menu(user)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")

        verify_button = tk.Button(window, text="Verify", command=verify_login)
        verify_button.pack()
        window.bind("<Return>", verify_login)

    def show_signup():
        clear_window()
        tk.Label(window, text="Create Username:").pack()
        username_entry = tk.Entry(window)
        username_entry.pack()

        tk.Label(window, text="Password:").pack()
        password1_entry = tk.Entry(window, show="*")
        password1_entry.pack()

        tk.Label(window, text="Confirm Password:").pack()
        password2_entry = tk.Entry(window, show="*")
        password2_entry.pack()

        def verify_signup(event=None):
            username = username_entry.get()
            password1 = password1_entry.get()
            password2 = password2_entry.get()
            result = create_user(username, password1, password2)
            if result == "User created successfully!":
                messagebox.showinfo("Success", result)
                show_login()
            else:
                messagebox.showerror("Error", result)

        verify_button = tk.Button(window, text="Verify", command=verify_signup)
        verify_button.pack()
        window.bind("<Return>", verify_signup)

    def show_user_menu(user):
        clear_window()

        # Create buttons based on SecurityLevel
        if user.SecurityLevel <= 0:
            tk.Button(window, text="Manage Users").pack()
        if user.SecurityLevel <= 1:
            tk.Button(window, text="Manage Game").pack()
        if user.SecurityLevel <= 3:
            tk.Button(window, text="Direct Messages").pack()

            pc_frame = tk.Frame(window)
            pc_frame.pack()

            # PC buttons with checks for None
            pc1_label = user.PCs[0].Name if user.PCs[0] else "PC1"
            tk.Button(pc_frame, text=pc1_label).pack(side=tk.LEFT)

            pc2_label = user.PCs[1].Name if user.PCs[1] else "PC2"
            tk.Button(pc_frame, text=pc2_label).pack(side=tk.LEFT)

            pc3_label = user.PCs[2].Name if user.PCs[2] else "PC3"
            tk.Button(pc_frame, text=pc3_label).pack(side=tk.LEFT)

        if user.SecurityLevel <= 2:
            tk.Button(window, text="Enter as a Narrator").pack()

        tk.Button(window, text="Information").pack()

    # Initial buttons
    clear_window()
    tk.Button(window, text="Log In", command=show_login).pack()
    tk.Button(window, text="Sign Up", command=show_signup).pack()

# Main application window
window = tk.Tk()
window.title("User Login System")
window.geometry("300x200")
main_window()
window.mainloop()

