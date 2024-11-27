# task 1

class Vihicle:

    def __init__(self, name : str, mileage : int) -> None:
        self.name = name
        self.mileage = mileage
    
    def get_vihicle_type(self, number_of_wheels : int) -> str:
        match number_of_wheels:
            case 2:
                type = 'motorcycle'   
            case 4:
                type = 'automobile'
            case 3:
                type = 'tricycle'
            case _:
                return 'Vihicle type not recognized.'
        return f'This is a {self.name} {type}.'

    def get_vihiclee_advice(self) -> str:
        if self.mileage <= 50000:
            return f'This is a good {self.name}; you should buy it.'
        elif self.mileage > 50000 and self.mileage <= 100000:
            return f'You should carefully check this {self.name} before buying it.'
        elif self.mileage > 100000 and self.mileage <= 150000:
            return f'This {self.name} should be checked thoroghly, before purchase.'
        else:
            return f'You probably should not buy this {self.name}.'

vihicle_1 = Vihicle('BMW', 50000)
vihicle_2 = Vihicle('Audi', 150000)
vihicle_3 = Vihicle('Honda', 160000)
vihicle_4 = Vihicle('Mitsubishi', 60000)

print(vihicle_1.get_vihicle_type(2))
print(vihicle_1.get_vihicle_type(3))
print(vihicle_1.get_vihicle_type(4))

print(vihicle_1.get_vihiclee_advice())
print(vihicle_2.get_vihiclee_advice())
print(vihicle_3.get_vihiclee_advice())
print(vihicle_4.get_vihiclee_advice())

# task 2

class House:

    def __init__(self, area : int, *rooms) -> None:
        self.area = area
        self.rooms = list(rooms)

    def show_around(self) -> str:
        if (self.rooms):
            rooms_listed = f"It has a {', a '.join(self.rooms[0:-1])} and a {self.rooms[-1]}."
        else:
            rooms_listed = 'There are no rooms.'
        return f'''
This is a house at {id(self)}.
Its area is {self.area}.
{rooms_listed}
'''
    
    def demolish(self) -> None:
        answer = input('Are you sure? ').strip().lower()
        if answer == 'yes':
            self.area = 0
            self.rooms = []

house_1 = House(60, 'kitchen', 'bathroom', 'living room', 'bedroom')
house_2 = House(80, 'kitchen', 'bathroom', 'living room', 'bedroom', 'garage', 'study')

print(house_1.show_around())
print(house_2.show_around())

house_1.demolish()
house_2.demolish()

print(house_1.show_around())
print(house_2.show_around())

