from Items import Item

def CreateItem(new_Item):
    new_Item.Weight = int(input("Introduce the weight (Kg): "))
    new_Item.Quantity = int(input("Introduce the quantity: "))

def CreateFood(new_Item):
    new_Item.Weight = int(input("Introduce the weight (Kg): "))
    new_Item.Quantity = int(input("Introduce the quantity: "))
    new_Item.DB = int(input("Introduce the Durability (in days): "))
    new_Item.maxDB = new_Item.DB 

def CreateIngredient(new_Item):
    new_Item.Weight = int(input("Introduce the weight (Kg): "))
    new_Item.Quantity = int(input("Introduce the quantity: "))
    new_Item.DB = int(input("Introduce the Durability (in days): "))
    new_Item.maxDB = new_Item.DB 

def CreateArmor(new_Item): #Shields included
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemDEFBonus = int(input("Introduce the Item Defense Bonus: "))
    Response = int(input("Where does it go? \n1. Helmet \n2.Shoulders \n3. Chest \n4. Arms \n5. Legs \n 6. Shield"))

    if Response == 1:
        new_Item.Space = ["Helmet"]
    elif Response == 2:
        new_Item.Space = ["Shoulders"]
    elif Response == 3:
        new_Item.Space = ["Chest"]
    elif Response == 4:
        new_Item.Space = ["Arms"]
    elif Response == 5:
        new_Item.Space = ["Legs"]
    elif Response == 6:
        new_Item.Space = ["Hand 2", "Extra"]

def CreateLightMelee(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    new_Item.DamageTypes = ["Piercing"]
    new_Item.Space = ["Hand 2", "Hand 1"]
    new_Item.RangeStats = [1]

def CreateMediumMelee(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    Response = int(input("Blunt weapon? \n0. No\n1. Yes"))
    if Response ==1:
        new_Item.DamageTypes = ["Blunt"]
    else:
        new_Item.DamageTypes = ["Slashing", "Piercing"]
    new_Item.Space = ["Hand 2", "Hand 1"]
    new_Item.RangeStats = [1]

def CreateHeavyMelee(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    Response = int(input("Blunt weapon? \n0. No\n1. Yes"))
    if Response ==1:
        new_Item.DamageTypes = ["Blunt"]
    else:
        new_Item.DamageTypes = ["Slashing", "Piercing"]
    new_Item.Space = ["Hand 1"]
    new_Item.RangeStats = [1]

def CreatePoleWeapons(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    new_Item.DamageTypes = ["Piercing"]
    new_Item.Space = ["Hand 1"]
    new_Item.RangeStats = [2]

def CreateLightBow (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    #Damage Type decided by the Arrows
    new_Item.ReloadTime = 0
    new_Item.Space = ["Hand 1"]
    new_Item.RangeStats = [10, "DEX"]

def CreateHeavyBow (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    #Damage Type decided by the Arrows
    new_Item.ReloadTime = 1
    new_Item.Space = ["Hand 1"]
    new_Item.RangeStats = [20, "DEX"]

def CreateLightCrossBow (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    #Damage Type decided by the Arrows
    new_Item.ReloadTime = 1
    new_Item.Space = ["Hand 2", "Hand 1"]
    new_Item.RangeStats = ["DEX", "STR"]

def CreateHeavyCrossBow (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Attack Bonus: "))
    #Damage Type decided by the Arrows
    new_Item.ReloadTime = 2
    new_Item.Space = ["Hand 1"]
    new_Item.RangeStats = [5, "DEX", "STR"]

def CreateStaff (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ManaBack = int(input("Introduce the Mana Back Bonus: "))
    new_Item.Space = ["Hand 1"]

def CreateWand (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemMAGATKBonus = int(input("Introduce the Magic Damage Bonus: "))
    new_Item.Space = ["Hand 1"]

def CreateOrb (new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.SpellSlots = int(input("Introduce the Spell Slots: "))
    new_Item.Space = ["Hand 1"]

def CreateHolder (new_Item):
    new_Item.Weight = 0.5
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    Res1 = int(input("Introduce the first Type (>1)"))
    new_Item.StorageTypes.append(Res1)
    Res2 = int(input("Introduce the second Type"))
    new_Item.StorageTypes.append(Res2)

    if Res1 == 2:
        if Res2 == 1:
            new_Item.StorageStats = [2, "DEX"]
            new_Item.StorageMax = 1
        elif Res2 == 2:
            new_Item.StorageStats = [1]
            new_Item.StorageMax = 1
        elif Res2 == 3:
            new_Item.StorageStats = [1]
            new_Item.StorageMax = 1
        elif Res2 == 4:
            new_Item.StorageStats = [2]
            new_Item.StorageMax = 1
    if Res1 == 3:
        if Res2 == 1:
            new_Item.StorageStats = [2, "DEX"]
            new_Item.StorageMax = 12 #When equipped add 2xDEX
        elif Res2 == 2:
            new_Item.StorageStats = ["DEX"]
            new_Item.StorageMax = 12 #When equipped add DEX
        elif Res2 == 3:
            new_Item.StorageStats = ["STR", "DEX"]
            new_Item.StorageMax = 12 #When equipped add DEX
        elif Res2 == 4:
            new_Item.StorageStats = ["STR"]
            new_Item.FillStorageMaxed = 12 #When equipped add STR

def CreateAmmo (new_Item):
    new_Item.Weight = 0.1
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB
    Response = int(input("Blunt Ammo? \n0. No\n1. Yes"))
    if Response ==1:
        new_Item.DamageTypes = ["Blunt"]
    else:
        new_Item.DamageTypes = ["Piercing"]
    