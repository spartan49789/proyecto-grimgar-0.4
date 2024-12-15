from Status import Status

class Creature:
    def __init__(self, CN):
        self.CN = CN
        self.Name = ""
        self.Race = ""
        self.Status = Status(CN)
        self.RM = 2

        self.Conditions = []
        self.actions = []
        self.Hunger = 0

        RM = {
            "Human": 2, "Elf": 2, "Lizardman": 2, "Dwarf": 2,
            "Orc": 3, "Centaur": 3,
            "Young Dragon": 4, "Wyvern": 4,
            "Dragon": 5
        }

        self.RM = RM[self.Race, 1]
        self.Status.Refresh(RM=self.RM)

    def STRDMG(self):
        return self.Status.STR + self.Status.PhyDMGBonus
    
    def CONDMG(self):
        return self.Status.CON + self.Status.PhyDMGBonus
    
    def DEXDMG(self):
        return self.Status.DEX + self.Status.PhyDMGBonus
    
    def STRDEF(self):
        return self.Status.STR + self.Status.PhyDEFBonus
    
    def CONDEF(self):
        return self.Status.CON + self.Status.PhyDEFBonus

    def DEXDEF(self):
        return self.Status.DEX + self.Status.PhyDEFBonus
    
    def TakeDMG(self, DMG):
        self.Status.HP -= DMG