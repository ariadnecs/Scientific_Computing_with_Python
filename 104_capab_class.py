print('Star Trek Voyager')


class Voyager:
    s = 0

    def season(self):
        self.s += 1
        print('Season', self.s)
        # method
        # print('Type:', type(self.season))
        # print('Sir:', dir(self.season))

se = Voyager()

for sea in range(0, 7):
    se.season()
# class
print('Type:', type(se))
print('Sir:', dir(se))

