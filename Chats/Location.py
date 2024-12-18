class Location:
    def __init__(self, LK: str, Greater: 'Location' = None):
        self.LK = LK
        self.Name = ""
        self.Greater = Greater
        
        # A location can have lesser locations within it (e.g., "Back Yard").
        self.Lesser = []
        
        # If part of a "Greater" location, inherit its base safety.
        self.BaseSafety = Greater.BaseSafety if Greater else 0  # 0 = Safe, 1 = Unsafe
        
        self.Safety = self.BaseSafety
        self.CombatStatus = 0  # 0 = No combat, 1-99 = Turn order if combat is active
        
        # List of creatures, each represented as [Creature, Turn Order].
        self.Creatures = []  

    def creature_enters(self, creature):
        """Add a creature to the location."""
        turn_order = len(self.Creatures) + 1
        self.Creatures.append([creature, turn_order])

    def creature_leaves(self, creature):
        """Remove a creature from the location."""
        for entry in self.Creatures:
            if entry[0] == creature:  # Check if the creature matches.
                self.Creatures.remove(entry)
                break
        else:
            print(f"Creature {creature} not found in location {self.LK}.")
        
        # Update turn orders after removal to maintain sequential order.
        self._update_turn_order()

    def set_turn_order(self, creature, new_order):
        """Manually set a specific turn order for a creature."""
        # Check if the creature exists
        for entry in self.Creatures:
            if entry[0] == creature:
                entry[1] = new_order  # Set the new turn order
                break
        else:
            print(f"Creature {creature} not found in location {self.LK}.")
            return
        
        # Sort creatures by their turn order
        self.Creatures.sort(key=lambda x: x[1])
        
        # Reassign turn orders to ensure consistency (no gaps or duplicates)
        self._update_turn_order()

    def _update_turn_order(self):
        """Update turn order after a creature leaves or reordering."""
        for idx, entry in enumerate(self.Creatures, start=1):
            entry[1] = idx  # Reassign turn orders sequentially.

    def __str__(self):
        """String representation of the location and its creatures."""
        creatures_info = ", ".join(f"{creature[0]}(Turn: {creature[1]})" for creature in self.Creatures)
        return f"Location {self.LK} - Creatures: [{creatures_info}]"
