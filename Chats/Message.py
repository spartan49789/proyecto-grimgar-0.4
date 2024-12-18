from datetime import datetime

class Message:
    def __init__(self, MK, Sender, Chat, Body):
        self.MK = MK
        now = datetime.now()
        self.Time = now.strftime("%H:%M:%S")
        self.Date = now.strftime("%Y-%m-%d")
        self.Sender = Sender
        self.Body = Body
        self.PC = None
        self.Actions = []

