import pickle
import os
from Items import Item
from ItemCreation import *

def save_list_to_pkl(file_name, data_list):
    """Save a list to a .pkl file."""
    with open(file_name, "wb") as file:
        pickle.dump(data_list, file)
    print(f"List has been saved to {file_name}.")

def load_list_from_pkl(file_name):
    """Load a list from a .pkl file."""
    if not os.path.exists(file_name):
        print(f"Error: {file_name} does not exist.")
        return None
    with open(file_name, "rb") as file:
        data_list = pickle.load(file)
    print(f"List has been loaded from {file_name}.")
    return data_list

def create_new_item():
    item_list = load_list_from_pkl()
    i=0
    for item in item_list:
        i +=1

    IN = i
    new_Item = Item(IN)
    new_Item.Name = input("Insert the Name: ")
    new_Item.Description = input("Insert the Description: ")
    new_Item.Type1 = int(input("Insert the first type (1-7)"))
    new_Item.Type2 = int(input("Insert the second type (1-4)"))

# Usage example
if __name__ == "__main__":
    create_new_item()
