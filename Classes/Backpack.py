from Money import Money

class Backpack:
    def __init__(self, Creature):
        self.CN = Creature.CN
        self.Money = Money(self.CN)
        self.maxW = Creature.Status.STR*3
        self.W = 0
        self.Items = []
        