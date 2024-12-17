from Classes.Status import Status

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
        self.Time = 0
        
        self.Tier = 1
        self.RM = 1
        self.Status.Refresh(RM=self.RM)

    def RefreshRM(self):
        RM = {
            "Human": 2, "Elf": 2, "Lizardman": 2, "Dwarf": 2,
            "Orc": 3, "Centaur": 3,
            "Young Dragon": 4, "Wyvern": 4,
            "Dragon": 5
        }

        self.RM = RM.get(self.Race, 1)
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
    def HealDMG(self, DMG):
        self.Status.HP += DMG
        if self.Status.HP > self.Status.maxHP:
            self.Status.HP = self.Status.maxHP

    def LoseSP(self, Lost):
        self.Status.SP += Lost
    def RegenSP(self, Regen):
        self.Status.SP += Regen
        if self.Status.SP > self.Status.maxSP:
            self.Status.SP = self.Status.maxSP

    def LoseMp(self, Lost):
        self.Status.MP += Lost
    def RegenMP(self, Regen):
        self.Status.MP += Regen
        if self.Status.MP > self.Status.maxMP:
            self.Status.MP = self.Status.maxMP

    def Training(self, GainedStat, Gain):
        if GainedStat =="STR":
            self.Status.STR += Gain*self.Status.Training
        elif GainedStat =="CON":
            self.Status.CON += Gain*self.Status.Training
        elif GainedStat =="DEX":
            self.Status.DEX += Gain*self.Status.Training
        elif GainedStat =="INT":
            self.Status.INT += Gain*self.Status.Training
        elif GainedStat =="WIS":
            self.Status.WIS += Gain*self.Status.Training
        elif GainedStat =="CHA":
            self.Status.CHA += Gain*self.Status.Training

        self.Status.TrainingRefresh(self.RM)

    def SafeTimePass(self, Time):
        self.Time += Time
        self.HealDMG(Time*(self.Status.maxHP*0.10 + self.Status.maxHP*self.Status.RegenBonus))
        self.RegenMP(Time*self.Status.maxMP*0.167)
        self.RegenSP(Time*self.Status.maxSP*0.167)

    def UnSafeTimePass(self, Time):
        self.Time += Time
        self.HealDMG(Time*(self.Status.maxHP*self.Status.RegenBonus))
        alt = 0
        for condition in self.Conditions:
            if condition == "Meditating":
                alt = 1
        if alt == 0:
            self.RegenMP(Time*self.Status.maxMP*0.025)
            self.RegenSP(Time*self.Status.maxSP*0.025)
        elif alt ==1:
            self.RegenMP(2*(Time*self.Status.maxMP*0.025))