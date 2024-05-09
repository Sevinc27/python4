class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Ağlar(Piece):
    def move(self):
        print(f"{self.color} {self.name} daşı hərəkət edir...")
        steps = self.choose_steps()
        print(f"{steps} addım atıldı.")

    def choose_steps(self):
        if self.name == "Şah":
            return 1
        elif self.name == "Piyada":
            return 2
        elif self.name == "At":
            return 3

class Qaralar(Piece):
    def move(self):
        print(f"{self.color} {self.name} daşı hərəkət edir...")
        if self.name == "Vəzir":
            print("Normal hərəkət: Hər hansı bir istiqamətdə bir addım atıldı.")
        elif self.name == "Fil":
            print("Qərb istiqamətində iki addım atıldı.")
        elif self.name == "Top":
            print("Şimal istiqamətində üç addım atıldı.")

ağ = Ağlar("Şah", "Ağ")
ağ= Ağlar("Piyada", "Ağ")
ağ = Ağlar("At", "Ağ")
qara = Qaralar("Vəzir", "Qara")
qara = Qaralar("Fil", "Qara")
qara = Qaralar("Top", "Qara")

ağ.move()
qara.move()