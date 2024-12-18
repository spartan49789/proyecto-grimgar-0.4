class Chat:
    def __init__(self, CK,Name, Location = None):
        self.CK = CK
        self.Name = Name
        self.Location = Location
        self.Topic = "" #Info, Group, Roleplay, DirectMessage
        self.Users = []
        self.MinPCTier = 1 #Only for Roleplay and Info
        self.Messages = []