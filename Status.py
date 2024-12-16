class Status:
    def __init__(self, CN, RM=2):
        self.CN = CN

        self.STR = 1
        self.strT = 0

        self.CON = 1
        self.conT = 0

        self.DEX = 1
        self.dexT = 0

        self.INT = 1
        self.intT = 0
        
        self.WIS = 1
        self.wisT = 0

        self.CHA = 1
        self.chaT = 0

        self.HP = self.CON*40*RM
        self.maxHP = self.HP

        self.MP = self.INT*100
        self.maxMP = self.MP

        self.SP = self.DEX*100
        self.maxSP = self.SP

        self.ActionP = 1
        self.AbilityP = 1
        self.Movement = self.DEX*3
        self.PhyDMGBonus = 0
        self.PhyDEFBonus = 0
        self.LootDie = 1
        self.RegenBonus = 0
        self.Training = 1
        self.CritChance = 0 
        self.RangedBonus = 0
        
    def Refresh(self, RM = 2):
        self.HP = self.CON*40*RM
        self.maxHP = self.HP

        self.MP = self.INT*100
        self.maxMP = self.MP

        self.SP = self.DEX*100
        self.maxSP = self.SP
        
        self.TierRefresh()

    def TrainingRefresh(self, RM = 2):
        self.maxHP = self.CON*40*RM

        self.maxMP = self.INT*100

        self.maxSP = self.DEX*100
        
        self.TierRefresh()

    def TierRefresh(self):
        self.strT = GetTier(self.STR)
        self.conT = GetTier(self.CON)
        self.dexT = GetTier(self.DEX)
        self.intT = GetTier(self.INT)
        self.wisT = GetTier(self.WIS)
        self.chaT = GetTier(self.CHA)

        if self.strT>=1:
            self.PhyDMGBonus = 1
            if self.strT >= 2:

                if self.strT>= 3:
                    self.PhyDMGBonus = 3
                    if self.strT >= 4:

                        if self.strT >= 5:
                            self.PhyDMGBonus = 6

        if self.conT>=1:
            self.PhyDEFBonus = 1
            if self.conT >= 2:
                self.RegenBonus = 0.5
                if self.conT>= 3:
                    self.PhyDEFBonus = 3
                    if self.conT >= 4:
                        self.RegenBonus = 2
                        if self.conT >= 5:
                            self.PhyDEFBonus = 6
        
        if self.dexT >=1:
            self.ActionP = 2
            if self.dexT >= 2:
                self.RangedBonus = 20
                if self.dexT>= 3:
                    self.ActionP = 3
                    if self.dexT >= 4:
                        self.RangedBonus = 40
                        if self.dexT >= 5:
                            self.ActionP = 4
        
        if self.intT>=1:
            self.Training = 1.5
            if self.intT >= 2:
                self.AbilityP = 2
                if self.intT>= 3:
                    self.Training = 2
                    if self.intT >= 4:
                        self.AbilityP = 3
                        if self.intT >= 5:
                            self.Training = 3

        if self.wisT>=1:
            self.LootDie = 3
            if self.wisT >= 2:
                self.CritChance = 10
                if self.wisT>= 3:
                    self.LootDie = 3
                    if self.wisT >= 4:
                        self.CritChance = 30
                        if self.wisT >= 5:
                            self.LootDie = 4

def GetTier(num):
    if num >= 3:
        return 1
    elif num >=5:
        return 2
    elif num >=8:
        return 3
    elif num >= 11:
        return 4
    elif num >= 15:
        return 5
    else:
        return 0
