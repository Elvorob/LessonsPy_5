class Animal:
    def __init__(self,name,place,food):
        self.name = name
        self.place = place
        self.__food = food

    def get_name(self):
        print(f'Animal: {self.name}')

    def get_place(self):
        print(f'Plase: {self.place}')

    def get_food(self):
        print(f'Food: {self.food}')

an1 = Animal('Cat', 'All world', 'meet')
print(an1.__dict__)
print(an1.get_name())
print(an1.get_place())
print(an1.food())