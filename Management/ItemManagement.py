import tkinter as tk
from tkinter import messagebox
from Classes.ItemStorage.Items import Item
from Classes.ItemStorage.ItemCreation import CreateItem, CreateArmor, CreateFood, CreateIngredient

def ItemManagementMenu(window, user, show_user_menu):
    for widget in window.winfo_children():
        widget.destroy()

    button_width = 0.2
    x_center = 0.4

    # Create buttons for each item type
    tk.Button(
        window,
        text="Create Item",
        command=lambda: create_item_screen(window)
    ).place(relx=x_center, rely=0.2, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Create Food",
        command=lambda: create_food_screen(window)
    ).place(relx=x_center, rely=0.3, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Create Ingredient",
        command=lambda: create_ingredient_screen(window)
    ).place(relx=x_center, rely=0.4, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Create Armor",
        command=lambda: create_armor_screen(window)
    ).place(relx=x_center, rely=0.5, relwidth=button_width, relheight=0.1)

    # Exit Button to go back to the main menu
    tk.Button(
        window,
        text="Go Back",
        command=lambda: show_user_menu(user)
    ).place(relx=x_center, rely=0.6, relwidth=button_width, relheight=0.1)

    tk.Button(
        window,
        text="Exit",
        command=window.quit
    ).place(relx=x_center, rely=0.7, relwidth=button_width, relheight=0.1)

def create_item_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

    # Create a new item object
    new_item = Item(IN=1)  # Create a new item with a unique ID

    # Label and entry for item name
    tk.Label(window, text="Item Name:").place(relx=0.3, rely=0.2)
    name_entry = tk.Entry(window)
    name_entry.place(relx=0.5, rely=0.2, relwidth=0.4)

    # Label and entry for item description
    tk.Label(window, text="Description:").place(relx=0.3, rely=0.3)
    description_entry = tk.Entry(window)
    description_entry.place(relx=0.5, rely=0.3, relwidth=0.4)

    # Label and entry for item weight
    tk.Label(window, text="Weight (Kg):").place(relx=0.3, rely=0.4)
    weight_entry = tk.Entry(window)
    weight_entry.place(relx=0.5, rely=0.4, relwidth=0.4)

    # Label and entry for item quantity
    tk.Label(window, text="Quantity:").place(relx=0.3, rely=0.5)
    quantity_entry = tk.Entry(window)
    quantity_entry.place(relx=0.5, rely=0.5, relwidth=0.4)

    def submit_item():
        new_item.Name = name_entry.get()
        new_item.Description = description_entry.get()
        new_item.Weight = float(weight_entry.get())
        new_item.Quantity = int(quantity_entry.get())
        
        # Call the existing item creation function
        CreateItem(new_item)
        
        messagebox.showinfo("Success", f"Item '{new_item.Name}' created successfully!")

    # Submit button to create the item
    tk.Button(window, text="Submit", command=submit_item).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    
    # Back button
    tk.Button(window, text="Back", command=lambda: ItemManagementMenu(window, None, None)).place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.1)

def create_food_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

    # Create a new food item object
    new_item = Item(IN=2)  # Create a new food item

    # Label and entry for item name
    tk.Label(window, text="Food Name:").place(relx=0.3, rely=0.2)
    name_entry = tk.Entry(window)
    name_entry.place(relx=0.5, rely=0.2, relwidth=0.4)

    # Label and entry for food weight
    tk.Label(window, text="Weight (Kg):").place(relx=0.3, rely=0.3)
    weight_entry = tk.Entry(window)
    weight_entry.place(relx=0.5, rely=0.3, relwidth=0.4)

    # Label and entry for durability
    tk.Label(window, text="Durability (days):").place(relx=0.3, rely=0.4)
    durability_entry = tk.Entry(window)
    durability_entry.place(relx=0.5, rely=0.4, relwidth=0.4)

    def submit_food():
        new_item.Name = name_entry.get()
        new_item.Weight = float(weight_entry.get())
        new_item.DB = int(durability_entry.get())
        new_item.maxDB = new_item.DB
        
        # Call the existing food creation function
        CreateFood(new_item)

        messagebox.showinfo("Success", f"Food '{new_item.Name}' created successfully!")

    # Submit button to create the food
    tk.Button(window, text="Submit", command=submit_food).place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.1)
    
    # Back button
    tk.Button(window, text="Back", command=lambda: ItemManagementMenu(window, None, None)).place(relx=0.7, rely=0.6, relwidth=0.2, relheight=0.1)

def create_armor_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

    # Create a new armor item object
    new_item = Item(IN=3)  # Create a new armor item

    # Label and entry for armor name
    tk.Label(window, text="Armor Name:").place(relx=0.3, rely=0.2)
    name_entry = tk.Entry(window)
    name_entry.place(relx=0.5, rely=0.2, relwidth=0.4)

    # Label and entry for armor weight
    tk.Label(window, text="Weight (Kg):").place(relx=0.3, rely=0.3)
    weight_entry = tk.Entry(window)
    weight_entry.place(relx=0.5, rely=0.3, relwidth=0.4)

    # Label and entry for durability
    tk.Label(window, text="Durability:").place(relx=0.3, rely=0.4)
    durability_entry = tk.Entry(window)
    durability_entry.place(relx=0.5, rely=0.4, relwidth=0.4)

    # Label and entry for defense bonus
    tk.Label(window, text="Defense Bonus:").place(relx=0.3, rely=0.5)
    defense_bonus_entry = tk.Entry(window)
    defense_bonus_entry.place(relx=0.5, rely=0.5, relwidth=0.4)

    def submit_armor():
        new_item.Name = name_entry.get()
        new_item.Weight = float(weight_entry.get())
        new_item.DB = int(durability_entry.get())
        new_item.maxDB = new_item.DB
        new_item.ItemDEFBonus = int(defense_bonus_entry.get())
        
        # Call the existing armor creation function
        CreateArmor(new_item)

        messagebox.showinfo("Success", f"Armor '{new_item.Name}' created successfully!")

    # Submit button to create the armor
    tk.Button(window, text="Submit", command=submit_armor).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    
    # Back button
    tk.Button(window, text="Back", command=lambda: ItemManagementMenu(window, None, None)).place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.1)

def create_ingredient_screen(window):
    for widget in window.winfo_children():
        widget.destroy()

    # Create a new ingredient item object
    new_item = Item(IN=4)  # Create a new ingredient item

    # Label and entry for ingredient name
    tk.Label(window, text="Ingredient Name:").place(relx=0.3, rely=0.2)
    name_entry = tk.Entry(window)
    name_entry.place(relx=0.5, rely=0.2, relwidth=0.4)

    # Label and entry for ingredient weight
    tk.Label(window, text="Weight (Kg):").place(relx=0.3, rely=0.3)
    weight_entry = tk.Entry(window)
    weight_entry.place(relx=0.5, rely=0.3, relwidth=0.4)

    # Label and entry for ingredient quantity
    tk.Label(window, text="Quantity:").place(relx=0.3, rely=0.4)
    quantity_entry = tk.Entry(window)
    quantity_entry.place(relx=0.5, rely=0.4, relwidth=0.4)

    # Label and entry for ingredient purity (example attribute for ingredients)
    tk.Label(window, text="Purity (%):").place(relx=0.3, rely=0.5)
    purity_entry = tk.Entry(window)
    purity_entry.place(relx=0.5, rely=0.5, relwidth=0.4)

    def submit_ingredient():
        new_item.Name = name_entry.get()
        new_item.Weight = float(weight_entry.get())
        new_item.Quantity = int(quantity_entry.get())
        new_item.Purity = float(purity_entry.get())
        
        # Call the existing ingredient creation function
        CreateIngredient(new_item)

        messagebox.showinfo("Success", f"Ingredient '{new_item.Name}' created successfully!")

    # Submit button to create the ingredient
    tk.Button(window, text="Submit", command=submit_ingredient).place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)
    
    # Back button
    tk.Button(window, text="Back", command=lambda: ItemManagementMenu(window, None, None)).place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.1)

