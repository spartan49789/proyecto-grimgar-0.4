class Item:
    def __init__(self, IN):
        self.IN = IN
        self.Name = ""
        self.Description = ""
        self.Type1 = 0
        #1- Miscelaneous - Items (Rope, Stones, etc) - Food - Ingredients
        #2- Armor - Light - Medium - Heavy - Shield
        #3- Melee Weapon - Light - Medium - Heavy - Polearm
        #4- Ranged Weapon - Light Bow - Heavy Bow - Light Crossbow - Heavy Crossbow
        #5- Focus - Wand - Staff - Orb
        #6- Wores - Backpacks - AmmoStorage
        self.Type2 = 0
        self.Space = [] # Where they go
        self.Weight = 0

        self.DB = 0
        self.maxDB = 0

        self.Stats = [] # When ranged decide range and when AmmoStorage decides how much
        self.Filled = 0 #For AmmoStorage
        self.Quantity = 0
        
        self.ItemDEFBonus = 0
        self.ItemPHYATKBonus = 0
        self.ItemMAGATKBonus = 0
        self.Range = 0
        self.ReloadTime = 0
        self.ManaBack = 0
        self.SpellSlots = 0
        self.Spells = []