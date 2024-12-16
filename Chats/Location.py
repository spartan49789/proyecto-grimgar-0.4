class Location:
    def __init__(self, LK, Greater=None):
        self.LK = LK
        self.Name = ""
        self.Greater = Greater
        #You can go to a chat within the same greater location in the instant unless a fight is going on
        self.Lesser = []
        #You can go to a chat withing a lesser greater location like "Back Yard"
        if self.Greater != None:
            self.BaseSafety = Greater.BaseSafety #0. Safe, 1. Unsafe
        else:
            self.BaseSafety = 0

        self.Creatures = [] # Creatures inside the Location