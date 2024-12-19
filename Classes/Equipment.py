class Equipment:
    def __init__(self, CN):
        self.CN = CN

        self.Head = None
        self.Shoulder = None
        self.Chest = None
        self.Arms = None
        self.Legs = None

        self.Extra = None
        self.Hand1 = None
        self.Hand2 = None

        self.DamageTypes = []
        self.DMGBonus = 0
        self.DEFBonus = 0
        self.RangeStats = []
        self.manaBack = 0
        self.MagDMGBonus = 0
        self.SpellSlots =0
        self.StoredSpells = []

    def equip(self, item, backpack):
        for slot in item.Space:
            current_item = getattr(self, slot)
            if current_item is None:
                setattr(self, slot, item)
                backpack.Items.remove(item)
                self.update_bonuses(item, equip=True)
                return f"{item.Name} equipped in {slot}."
            else:
                return f"{slot} is occupied. Do you want to swap items?"

    def swap(self, item, slot, backpack):
        """Swap the currently equipped item with a new one."""
        current_item = getattr(self, slot)
        setattr(self, slot, item)
        backpack.Items.remove(item)
        backpack.Items.append(current_item)
        self.update_bonuses(current_item, equip=False)
        self.update_bonuses(item, equip=True)
        return f"Swapped {current_item.Name} with {item.Name} in {slot}."

    def unequip(self, slot, backpack):
        """Unequip an item from the specified slot."""
        item = getattr(self, slot)
        if item:
            setattr(self, slot, None)
            backpack.Items.append(item)
            self.update_bonuses(item, equip=False)
            return f"{item.Name} unequipped from {slot}."
        return f"No item to unequip in {slot}."

    def update_bonuses(self):
        self.DamageTypes = self.Hand1.DamageTypes
        self.DMGBonus = self.Hand1.ItemPHYATKBonus + self.Hand2.ItemPHYATKBonus
        self.DEFBonus = self.Head.ItemDEFBonus + self.Chest.ItemDEFBonus+ self.Arms.ItemDEFBonus+ self.Legs.ItemDEFBonus+ self.Shoulder.ItemDEFBonus+ self.Hand2.ItemDEFBonus
        self.RangeStats = self.Hand1.RangeStats
        self.manaBack = self.Hand1.ManaBack
        self.MagDMGBonus = self.Hand1.ItemMAGATKBonus
        self.SpellSlots = self.Hand1.SpellSlots
        self.StoredSpells = self.Hand1.Spells