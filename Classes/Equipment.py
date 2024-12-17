class Equipment:
    def __init__(self, CN):
        self.CN = CN

        self.Head = None
        self.Shoulder = None
        self.Chest = None
        self.Legs = None
        self.Feet = None

        self.Extra = None
        self.Hand1 = None
        self.Hand2 = None

        self.DamageTypes = []
        self.DMGBonus = 0
        self.DEFBonus = 0
        self.RangeStats = []
        self.manaBack = 0
        self.MagDMGBonus = 0
        self.SpellSlots =0
        self.StoredSpells = []