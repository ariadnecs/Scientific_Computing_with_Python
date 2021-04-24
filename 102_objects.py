print('Star Trek: The Original Series')
# template = StarTrekTOS
class StarTrekTOS:
    # objects in StarTrekTOS
    s = 0

    def season(self):
        self.s += 1
        print("Season", self.s)
# construct a StarTrekTOS object and store in se
se = StarTrekTOS()

# tell the se object to run the season() code within it
#StarTrekTOS.season(se)
se.season()
se.season()
se.season()
