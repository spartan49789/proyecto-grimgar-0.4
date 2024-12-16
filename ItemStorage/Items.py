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
        #6- Holder
        #7- Ammo - Light Bolt - Heavy Bolt - Light Arrow - Heavy Arrow
        self.Type2 = 0
        self.Space = [] # Where they go
        self.Weight = 0

        self.DB = 0
        self.maxDB = 0
        
        self.StorageTypes = [] #Storage of type1 and type2
        self.StorageStats = [] #Stats for storage slots
        self.StorageMax = 0 #For Storage Maximum (calculated when equipped)
        self.Storage = []

        self.DamageTypes = []
        self.ItemDEFBonus = 0
        self.ItemPHYATKBonus = 0
        self.ItemMAGATKBonus = 0
        self.RangeStats = []
        self.ReloadTime = 0
        self.ManaBack = 0
        self.SpellSlots = 0
        self.Spells = []