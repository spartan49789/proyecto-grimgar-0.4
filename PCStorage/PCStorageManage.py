import pickle
import os

PC_LIST_FILE = "PC.pkl"

def save_pc_list(pc_list):
    with open(PC_LIST_FILE, "wb") as file:
        pickle.dump(pc_list, file)

def load_pc_list():
    if os.path.exists(PC_LIST_FILE):
        with open(PC_LIST_FILE, "rb") as file:
            pc_list = pickle.load(file)
    else:
        pc_list = []

    return pc_list