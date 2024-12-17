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