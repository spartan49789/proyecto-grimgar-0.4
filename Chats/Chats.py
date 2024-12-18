class Chat:
    def __init__(self, CK, Location = None):
        self.CK = CK
        self.Location = Location
        self.Topic = "" #Info, Group, Roleplay, DirectMessage
        self.Users = []
        self.MinPCTier = 1 #Only for Roleplay and Info
        self.Messages = []