# parent
class STParty:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print('\nWelcome', self.name)
    def party(self):
        self.x += 1
        print(self.name, 'count', self.x)

# child
class TOS(STParty):
    points = 0

    def char(self):
        self.points += 5
        self.party()
        print(self.name, "points", self.points)

d = STParty('Data')
d.party()

s = TOS("Spock")
s.char()

u = TOS('Uhura')
u.party()
u.char()


