class STParty:
    x = 0
    name = ''
    def __init__(self, nam):
        self.name = nam
        print('Welcome', self.name)
    def party(self):
        self.x += 1
        print(self.name, 'count', self.x)

s = STParty('Spock')
u = STParty('Uhura')
u.party()
s.party()
s.party()
u.party()
