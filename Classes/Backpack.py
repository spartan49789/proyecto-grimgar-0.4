from Classes.Money import Money
import tkinter as tk

class Backpack:
    def __init__(self, Creature):
        self.CN = Creature.CN
        self.Money = Money(self.CN)
        self.maxW = Creature.Status.STR*3
        self.W = 0
        self.Items = []
        
    def ShowInfo(self, frame):

        # Clear the frame
        for widget in frame.winfo_children():
            widget.destroy()

        # Money Frame
        Money_frame = tk.Frame(frame)
        Money_frame.pack(fill="x", pady=10)

        # Center-align columns in Money_frame
        Money_frame.grid_columnconfigure(0, weight=1)
        Money_frame.grid_columnconfigure(1, weight=1)
        Money_frame.grid_columnconfigure(2, weight=1)

        # Coin Names
        Coin_names = ["Copper", "Silver", "Gold"]
        for col, coin_name in enumerate(Coin_names):
            tk.Label(Money_frame, text=coin_name, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=5)

        Coin_values = [self.Money.Copper, self.Money.Silver, self.Money.Gold]
        for col, coin_value in enumerate(Coin_values):
            tk.Label(
                Money_frame,
                text=coin_value,
                font=("Arial", 12),
                anchor="center",  # Center-align text in the label
                justify="center"  # Justify text centrally
            ).grid(row=1, column=col, padx=5)

        info_frame = tk.Frame(frame)
        info_frame.pack(fill="x", pady=5)  # Ensure it appears by packing it
        tk.Label(
            info_frame,
            text=f"Weight: {self.W}/{self.maxW}Kg",
            font=("Arial", 12),
            anchor="center",  # Center-align text in the label
            justify="center"  # Justify text centrally
        ).pack(anchor="center", padx=10)  # Align label to the center of the frame


        # Item Frame
        item_frame = tk.Frame(frame)
        item_frame.pack(fill="both", expand=True)

        # Show Item List
        self.show_item_list(item_frame)

    def show_item_list(self, item_frame):
        # Clear the item_frame
        for widget in item_frame.winfo_children():
            widget.destroy()
        # Create a Listbox for items
        listbox = tk.Listbox(item_frame, height=10)
        listbox.pack(side="left", fill="both", expand=True)

        # Add scrollbar
        scrollbar = tk.Scrollbar(item_frame, orient="vertical", command=listbox.yview)
        scrollbar.pack(side="right", fill="y")
        listbox.config(yscrollcommand=scrollbar.set)

        # Populate the Listbox with item names
        for idx, item in enumerate(self.Items):
            listbox.insert(idx, item.Name)

        # Bind the selection event to display item details
        listbox.bind("<<ListboxSelect>>", lambda event: self.show_item_info(item_frame, listbox.curselection()))

    def show_item_info(self, item_frame, selection):
        """Display the selected item's information."""
        if not selection:
            return  # No item selected

        # Get the selected item
        selected_index = selection[0]
        selected_item = self.Items[selected_index]

        # Clear the item_frame
        for widget in item_frame.winfo_children():
            widget.destroy()

        tk.Label(item_frame, text=f"Name: {selected_item.Name}", font=("Arial", 12, "bold")).pack(anchor="w")
        tk.Label(item_frame, text=f"Description: {selected_item.Description}", font=("Arial", 10)).pack(anchor="w")

        # Get the item type text
        TypeText = getItemText(selected_item)
        tk.Label(item_frame, text=f"Type: {TypeText}", font=("Arial", 10)).pack(anchor="w")
        tk.Label(item_frame, text=f"Weight: {selected_item.Weight}", font=("Arial", 10)).pack(anchor="w")

        # Show "Equip" button if Type1 > 1
        if selected_item.Type1 > 1:
            equip_button = tk.Button(
                item_frame,
                text="Equip",
                font=("Arial", 12),
                command=lambda: self.equip_item(selected_item, item_frame)
            )
            equip_button.pack(pady=5)

        # Add a back button to return to the item list
        back_button = tk.Button(
            item_frame,
            text="← Back",
            font=("Arial", 12),
            command=lambda: self.show_item_list(item_frame)
        )
        back_button.pack(pady=10)

    def equip_item(self, item, frame):
        """Attempt to equip an item."""
        if not item.Space:
            return  # Item can't be equipped
        if len(item.Space) == 1:
            # Single-slot item
            slot = item.Space[0]
            message = self.owner.Equipment.equip(item, self)
            if "occupied" in message:
                self.handle_swap(item, slot, frame)
            else:
                self.show_message(frame, message)
        else:
            # Multi-slot item: Let the user choose
            self.show_slot_choice(item, frame)

    def handle_swap(self, item, slot, frame):
        """Prompt user to swap items."""
        def swap_action():
            message = self.owner.Equipment.swap(item, slot, self)
            self.show_message(frame, message)
        def cancel_action():
            self.show_message(frame, "Swap canceled.")

        # Add buttons for "Swap" and "Cancel" in the UI
        swap_button = tk.Button(frame, text="Swap", command=swap_action)
        swap_button.pack(pady=5)
        cancel_button = tk.Button(frame, text="Cancel", command=cancel_action)
        cancel_button.pack(pady=5)

    def show_slot_choice(self, item, frame):
        """Display slot options for multi-slot items."""
        def equip_in_slot(slot):
            message = self.owner.Equipment.equip(item, self)
            self.show_message(frame, message)

        for slot in item.Space:
            button = tk.Button(frame, text=f"Equip in {slot}", command=lambda s=slot: equip_in_slot(s))
            button.pack(pady=5)

    def show_message(self, frame, message):
        """Display a message in the frame."""
        for widget in frame.winfo_children():
            widget.destroy()
        tk.Label(frame, text=message, font=("Arial", 12)).pack(pady=10)

def getItemText(selected_item):
    TypeText = ""

    if selected_item.Type1 == 2:  # Armor
        if selected_item.Type2 == 1:
            TypeText = "Light Armor"
        elif selected_item.Type2 == 2:
            TypeText = "Medium Armor"
        elif selected_item.Type2 == 3:
            TypeText = "Heavy Armor"
        elif selected_item.Type2 == 4:
            TypeText = "Shield"

    elif selected_item.Type1 == 3:  # Melee Weapons
        if selected_item.Type2 == 1:
            TypeText = "Light Weapon"
        elif selected_item.Type2 == 2:
            TypeText = "Medium Weapon"
        elif selected_item.Type2 == 3:
            TypeText = "Heavy Weapon"
        elif selected_item.Type2 == 4:
            TypeText = "Polearm"

    elif selected_item.Type1 == 4:  # Ranged Weapons
        if selected_item.Type2 == 1:
            TypeText = "Light Bow"
        elif selected_item.Type2 == 2:
            TypeText = "Heavy Bow"
        elif selected_item.Type2 == 3:
            TypeText = "Light Crossbow"
        elif selected_item.Type2 == 4:
            TypeText = "Heavy Crossbow"

    elif selected_item.Type1 == 5:  # Arcane Focus
        if selected_item.Type2 == 1:
            TypeText = "Wand"
        elif selected_item.Type2 == 2:
            TypeText = "Staff"
        elif selected_item.Type2 == 3:
            TypeText = "Orb"

    elif selected_item.Type1 == 6:  # Holders
        if selected_item.Type2 == 1:
            TypeText = "Holder"

    elif selected_item.Type1 == 7:  # Ammo
        if selected_item.Type2 == 1:
            TypeText = "Light Arrow"
        elif selected_item.Type2 == 2:
            TypeText = "Heavy Arrow"
        elif selected_item.Type2 == 3:
            TypeText = "Light Bolt"
        elif selected_item.Type2 == 4:
            TypeText = "Heavy Bolt"

    return TypeText