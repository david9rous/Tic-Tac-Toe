class Player:
    def __init__(self, name):
        if name == 0:
            self.name = "Kolecko"
        elif name == 1:
            self.name = "Krizek"
        elif name == 2:
            self.name = "Pocitac"

    def getinput(self):
        print(self.name, "voli pole:\n")
        selected_by_player = input()
        return selected_by_player
