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


def radar_chart(canvas, stats, tiers, center_x, center_y, radius):
    """Draws a radar chart on the given canvas (updated to match new chart style)."""
    # Prepare data
    labels = ['STR', 'DEX', 'CON', 'WIS', 'INT', 'CHA']
    
    # Normalize stats based on maximum value (similar to new chart)
    max_stat_value = get_max_stat_value(stats)
    stats = [stat / max_stat_value * 3 for stat in stats]  # Normalize values to fit within the range 0-3
    
    # Close the loop by repeating the first stat
    stats += stats[:1]
    
    num_vars = len(labels)

    # Calculate the angles for each axis (6 axes in total)
    angles = [n / float(num_vars) * 2 * math.pi for n in range(num_vars)]
    angles += angles[:1]  # Close the loop by adding the first angle

    # Create the radar chart figure using matplotlib
    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))

    # Plot the radar chart: stats are plotted as a line and filled
    ax.plot(angles, stats, linewidth=2, linestyle='solid', color="green", marker='o')
    ax.fill(angles, stats, 'green', alpha=0.4)

    # Set chart ticks and limits
    ax.set_yticks(np.arange(0, 4, 1))  # Ticks every 1 unit, range [0, 3]
    ax.set_ylim(0, 3)

    # Add labels for each axis, with stats and tiers
    ax.set_xticks(angles[:-1])  # Skip the last angle as it overlaps with the first
    ax.set_xticklabels([f"{label}\n{value} (T{tier})" for label, value, tier in zip(labels, stats[:-1], tiers)])

    # Embed the radar chart in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=canvas.winfo_toplevel())
    canvas.draw()

    # Place the radar chart in the Tkinter grid
    canvas.get_tk_widget().pack(pady=10)
    plt.close(fig)
    
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

    # HP, SP, MP
    hp_label = tk.Label(frame, text=f"HP: ({self.Creature.Status.HP}/{self.Creature.Status.maxHP})")
    sp_label = tk.Label(frame, text=f"SP: ({self.Creature.Status.SP}/{self.Creature.Status.maxSP})")
    mp_label = tk.Label(frame, text=f"MP: ({self.Creature.Status.MP}/{self.Creature.Status.maxMP})")
    hp_label.pack()
    sp_label.pack()
    mp_label.pack()

    # Radar Chart
    canvas = tk.Canvas(frame, width=300, height=300, bg="white")
    canvas.pack(pady=10)
    stats = [
        self.Creature.Status.STR,
        self.Creature.Status.DEX,
        self.Creature.Status.CON,
        self.Creature.Status.WIS,
        self.Creature.Status.INT,
        self.Creature.Status.CHA
    ]
    tiers = [
        self.Creature.Status.strT,
        self.Creature.Status.dexT,
        self.Creature.Status.conT,
        self.Creature.Status.wisT,
        self.Creature.Status.intT,
        self.Creature.Status.chaT
    ]
    radar_chart(canvas, stats, tiers, center_x=150, center_y=150, radius=100)

    # Inventory Grid
    table_frame = tk.Frame(frame)
    table_frame.pack(fill="both", expand=True)
    headers = ["Equipment", "Backpack", "Abilities", "Empty"]
    for i, header in enumerate(headers):
        ttk.Label(table_frame, text=header, font=("Arial", 10, "bold"), borderwidth=1, relief="solid").grid(row=0, column=i, sticky="nsew")

    # Fill table with dummy rows
    for i in range(1, 11):
        for j in range(4):
            ttk.Label(table_frame, text="", borderwidth=1, relief="solid").grid(row=i, column=j, sticky="nsew")

    # Make table stretchable
    for i in range(4):
        table_frame.columnconfigure(i, weight=1)

def get_max_stat_value(stats):
    max_stat = max(stats)
    thresholds = [3, 5, 8, 11, 15, 20]
    for threshold in thresholds:
        if max_stat <= threshold:
            return threshold
    return thresholds[-1]