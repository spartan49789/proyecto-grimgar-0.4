import os
import pickle

USER_LIST_FILE = "user_list.pkl"

def load_user_list():
    if os.path.exists(USER_LIST_FILE):
        with open(USER_LIST_FILE, "rb") as file:
            user_list = pickle.load(file)
    else:
        user_list = []
    return user_list

# Helper functions
def save_user_list(user_list):
    with open(USER_LIST_FILE, "wb") as file:
        pickle.dump(user_list, file)

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

CHAT_LIST_FILE = "Chat.pkl"

def save_chat_list(pc_list):
    with open(CHAT_LIST_FILE, "wb") as file:
        pickle.dump(pc_list, file)

def load_chat_list():
    if os.path.exists(CHAT_LIST_FILE):
        with open(CHAT_LIST_FILE, "rb") as file:
            pc_list = pickle.load(file)
    else:
        pc_list = []

    return pc_list

LOCA_LIST_FILE = "Location.pkl"

def save_Location_list(pc_list):
    with open(LOCA_LIST_FILE, "wb") as file:
        pickle.dump(pc_list, file)

def load_Location_list():
    if os.path.exists(LOCA_LIST_FILE):
        with open(LOCA_LIST_FILE, "rb") as file:
            pc_list = pickle.load(file)
    else:
        pc_list = []

    return pc_list