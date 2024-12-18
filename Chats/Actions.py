class Actions:
    def __init__(self, CasterTurn, TargetTurn, Type1, Type2, Number):
        self.Caster = CasterTurn
        self.Target = TargetTurn
        self.Type1 = Type1 #from 1-3
        #1 1- Damage 2- Heal ---  Number
        #2 + Buff - Debuff --- Strength
        #3 ConApplied - Bleeding, Snare, Stunned, Frightened, Rage, Sleep, Prone, Tired, Taunted, Restricted
        self.Type2 = Type2
        self.Num = Number

class Turn:
    def __init__(self,TurnOrder, CN):
        self.TurnOrder = TurnOrder
        self.CN = CN
        self.ReceivingActions = []

