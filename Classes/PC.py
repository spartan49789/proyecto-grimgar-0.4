from Classes.Backpack import Backpack
from Classes.Creature import Creature
from Classes.Equipment import Equipment
from Classes.CharClass import CharClass
from Chats.User import AsignedPC

class PC:
    def __init__(self, Chk):
        self.Creature = Creature(Chk)
        self.Creature.Race = "Human"
        self.Creature.RefreshRM()
        self.Creature.Tier = 0

        self.Age = 0
        self.Gender = ""
        self.Backpack = Backpack(self.Creature)
        self.Equipment = Equipment(self.Creature.CN)
        self.Class = []
        self.Abilities = []

    def PHY_Attack(self,Stat="STR"):
        DamageBonus = self.Equipment.DMGBonus
        
        if Stat == "STR":
            DamageStat = self.Creature.STRDMG()
        elif Stat == "CON":
            DamageStat = self.Creature.CONDMG()
        elif Stat == "DEX":
            DamageStat = self.Creature.DEXDMG()

        AttackDamgage = DamageStat + DamageBonus
        return AttackDamgage

    def PHY_Deffense(self,Stat="STR"):
        DefenseBonus = self.Equipment.DEFBonus
        
        if Stat == "STR":
            DefenseStat = self.Creature.STRDEF()
        elif Stat == "CON":
            DefenseStat = self.Creature.CONDEF()
        elif Stat == "DEX":
            DefenseStat = self.Creature.DEXDEF()

        AttackDamgage = DefenseStat + DefenseBonus
        return AttackDamgage
    
    def SafeTime(self, Time):
        self.Creature.SafeTimePass(Time)

    def UnSafeTime(self, Time):
        self.Creature.UnSafeTimePass(Time)

    def AsignPC(self):
        new = AsignedPC(self.Creature.CN, self.Creature.Name)
        return new 
    
import tkinter as tk
from tkinter import ttk
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def ShowSheet(self, frame):
    # Clear previous content
    for widget in frame.winfo_children():
        widget.destroy()

    # Title
    title_label = tk.Label(frame, text=f"{self.Creature.Name}", font=("Arial", 16, "bold"))
    title_label.pack()

    # Race, Gender, Age
    info_frame = tk.Frame(frame)
    info_frame.pack(fill="x", pady=5)
    tk.Label(info_frame, text=f"{self.Creature.Race}", font=("Arial", 10)).grid(row=0, column=0)
    tk.Label(info_frame, text=f"{self.Gender}", font=("Arial", 10)).grid(row=0, column=1)
    tk.Label(info_frame, text=f"({self.Age})", font=("Arial", 10)).grid(row=0, column=2)

    stats_frame = tk.Frame(frame)
    stats_frame.pack(fill="x", pady=10)

    # Stat names row ("STR | DEX | CON | WIS | INT | CHA")
    stat_names = ["STR", "DEX", "CON", "WIS", "INT", "CHA"]
    for col, stat_name in enumerate(stat_names):
        tk.Label(stats_frame, text=stat_name, font=("Arial", 12, "bold")).grid(row=0, column=col, padx=5)

    # Stat values row (e.g., "strT | dexT | conT | wisT | intT | chaT")
    stat_values = [
        round(self.Creature.Status.STR, 2),
        round(self.Creature.Status.DEX, 2),
        round(self.Creature.Status.CON, 2),
        round(self.Creature.Status.WIS, 2),
        round(self.Creature.Status.INT, 2),
        round(self.Creature.Status.CHA, 2)
    ]
    for col, stat_value in enumerate(stat_values):
        tk.Label(stats_frame, text=stat_value, font=("Arial", 12)).grid(row=1, column=col, padx=5)

    # Stat tiers row (e.g., "strT | dexT | conT | wisT | intT | chaT")
    stat_tiers = [
        self.Creature.Status.strT,
        self.Creature.Status.dexT,
        self.Creature.Status.conT,
        self.Creature.Status.wisT,
        self.Creature.Status.intT,
        self.Creature.Status.chaT
    ]
    for col, stat_tier in enumerate(stat_tiers):
        tk.Label(stats_frame, text=stat_tier, font=("Arial", 12)).grid(row=2, column=col, padx=5)

    # Set column weights for even distribution
    for col in range(6):  # 6 columns for the 6 stats
        stats_frame.columnconfigure(col, weight=1)

    # HP Label and Progress Bar
    hp_label = tk.Label(frame, text=f"HP: ({self.Creature.Status.HP}/{self.Creature.Status.maxHP})")
    hp_label.pack(fill="x", pady=5)
    hp_bar = ttk.Progressbar(frame, length=300, maximum=self.Creature.Status.maxHP, value=self.Creature.Status.HP, mode="determinate")
    hp_bar.pack(fill="x", pady=5)
    hp_bar.config(style="green.Horizontal.TProgressbar")

    # SP Label and Progress Bar
    sp_label = tk.Label(frame, text=f"SP: ({self.Creature.Status.SP}/{self.Creature.Status.maxSP})")
    sp_label.pack(fill="x", pady=5)
    sp_bar = ttk.Progressbar(frame, length=300, maximum=self.Creature.Status.maxSP, value=self.Creature.Status.SP, mode="determinate")
    sp_bar.pack(fill="x", pady=5)
    sp_bar.config(style="yellow.Horizontal.TProgressbar")

    # MP Label and Progress Bar
    mp_label = tk.Label(frame, text=f"MP: ({self.Creature.Status.MP}/{self.Creature.Status.maxMP})")
    mp_label.pack(fill="x", pady=5)
    mp_bar = ttk.Progressbar(frame, length=300, maximum=self.Creature.Status.maxMP, value=self.Creature.Status.MP, mode="determinate")
    mp_bar.pack(fill="x", pady=5)
    mp_bar.config(style="blue.Horizontal.TProgressbar")

    # Inventory Buttons - Equipment, Backpack, Abilities, Actions
    button_frame = tk.Frame(frame)
    button_frame.pack(fill="x", pady=10)
    
    # Buttons for Equipment, Backpack, Abilities, and Actions
    equipment_button = tk.Button(button_frame, text="Equipment", command= lambda: on_Equipment_select(empty_frame))
    equipment_button.pack(side="left", fill="x", expand=True)

    def on_Equipment_select(empty_frame):
        equipment_button.config(bg="Gray17", fg="White")
        backpack_button.config(bg="White", fg="Black")
        abilities_button.config(bg="White", fg="Black")
        actions_button.config(bg="White", fg="Black")
        self.Backpack.ShowInfo(empty_frame)
    
    backpack_button = tk.Button(button_frame, text="Backpack", command= lambda: on_backpack_select(empty_frame))
    backpack_button.pack(side="left", fill="x", expand=True)
    
    def on_backpack_select(empty_frame):
        equipment_button.config(bg="White", fg="Black")
        backpack_button.config(bg="Gray17", fg="White")
        abilities_button.config(bg="White", fg="Black")
        actions_button.config(bg="White", fg="Black")
        self.Backpack.ShowInfo(empty_frame)
    
    abilities_button = tk.Button(button_frame, text="Abilities", command= lambda: on_abilities_select(empty_frame))
    abilities_button.pack(side="left", fill="x", expand=True)

    def on_abilities_select(empty_frame):
        equipment_button.config(bg="White", fg="Black")
        backpack_button.config(bg="White", fg="Black")
        abilities_button.config(bg="Gray17", fg="White")
        actions_button.config(bg="White", fg="Black")
        self.Backpack.ShowInfo(empty_frame)
    
    actions_button = tk.Button(button_frame, text="Actions", command= lambda: on_actions_select(empty_frame))
    actions_button.pack(side="left", fill="x", expand=True)

    def on_actions_select(empty_frame):
        equipment_button.config(bg="White", fg="Black")
        backpack_button.config(bg="White", fg="Black")
        abilities_button.config(bg="White", fg="Black")
        actions_button.config(bg="Gray17", fg="White")
        self.Backpack.ShowInfo(empty_frame)

    # Empty frame for spacing below buttons
    empty_frame = tk.Frame(frame)
    empty_frame.pack(fill="both", expand=True)
