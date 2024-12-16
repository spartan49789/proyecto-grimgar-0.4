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
    else:
        new_Item.Space = []

def CreateLightMelee(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Defense Bonus: "))
    new_Item.DamageTypes = ["Piercing"]
    new_Item.Range = 1

def CreateMediumMelee(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Defense Bonus: "))
    Response = int(input("Blunt weapon? \n0. No\n1. Yes"))
    if Response ==1:
        new_Item.DamageTypes = ["Blunt"]
    else:
        new_Item.DamageTypes = ["Slashing", "Piercing"]
    new_Item.Range = 1

def CreateHeavyMelee(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Defense Bonus: "))
    Response = int(input("Blunt weapon? \n0. No\n1. Yes"))
    if Response ==1:
        new_Item.DamageTypes = ["Blunt"]
    else:
        new_Item.DamageTypes = ["Slashing", "Piercing"]
    new_Item.Range = 1

def CreatePoleWeapons(new_Item):
    new_Item.Weight = int(input("Introduce the weight(Kg): "))
    new_Item.DB = int(input("Introduce the Durability: "))
    new_Item.maxDB = new_Item.DB 
    new_Item.ItemPHYATKBonus = int(input("Introduce the Item Defense Bonus: "))
    new_Item.Range = 2
