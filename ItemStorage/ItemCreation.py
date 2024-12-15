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