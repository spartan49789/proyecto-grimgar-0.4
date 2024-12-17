class User:
    def __init__(self, UK):
        self.UK = UK
        self.Name = ""
        self.Password = ""
        self.SecurityLevel = 3 #0. Owner, 1. Admin, 2. Narrator, 3. Player
        self.PCs = [None, None, None, None]

class AsignedPC:
    def __init__(self, CK, Name):
        self.CK = CK
        self.Name = Name