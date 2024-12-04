from math import pi

# task 1

class Circle:
    
    def __init__(self, radius : float) -> None:
        self.radius = radius
    
    def get_circumferace(self) -> float:
        return 2 * pi * self.radius
    
    def get_circle_area(self) -> float:
        return pi * self.radius ** 2 
    
class Square:

    def __init__(self, side : float) -> None:
        self.side = side
    
    def get_square_perimeter(self) -> float:
        return self.side * 4
    
    def get_square_area(self) -> float:
        return self.side ** 2

class SquaredCircle(Circle, Square):

    def __init__(self, radius: float) -> None:
        Circle.__init__(self, radius)
        self.side = radius * 2

squared_circle = SquaredCircle(5)

print('task 1')
print(squared_circle.get_circle_area())
print(squared_circle.get_square_perimeter())
print(squared_circle.get_circumferace())
print(squared_circle.get_square_area())
print()

# task 2

class Wheels:

    def __init__(self, type_of_wheels, quality) -> None:
        self.__type = type_of_wheels
        self.__quality = quality

    def set_type(self, type_of_wheels):
        self.__type = type_of_wheels
    
    def get_type(self):
        return self.__type

    def get_quality(self):
        return self.__quality

class Engine:

    def __init__(self, type_of_engin, quality) -> None:
        self.__type = type_of_engin
        self.__quality = quality

    def set_type(self, type_of_engin):
        self.__type = type_of_engin
    
    def get_type(self):
        return self.__type

    def get_quality(self):
        return self.__quality

class Doors:

    def __init__(self, type_of_doors, quality) -> None:
        self.__type = type_of_doors
        self.__quality = quality

    def set_type(self, type_of_doors):
        self.__type = type_of_doors
    
    def get_type(self):
        return self.__type

    def get_quality(self):
        return self.__quality

class Car:

    def __init__(self, wheels_type, wheels_quality, doors_type, doors_quality, engine_type, engine_quality) -> None:

        self.wheels = Wheels(wheels_type, wheels_quality)
        self.engine = Engine(engine_type, engine_quality)
        self.doors = Doors(doors_type, doors_quality)

car = Car('steel', 'good', 'sliding', 'subpar', 'electric', 'good')

print('task 2')
car.wheels.set_type('scissor')
print(car.engine.get_type())
print(car.doors.get_quality())
print(car.wheels.get_type())
print()

# task 3

class Pet:

    def __init__(self, name : str, pet_type = 'unstated type', sound = '...') -> None:
        self.__name = name
        self.__sound = sound 
        self.__type = pet_type
    
    def get_name(self) -> None:
        print(f'This is {self.__name}.')

    def get_sound(self) -> None:
        print(f'The {self.__type} named {self.__name} says "{self.__sound}".')
    
    def get_type(self) -> None:
        print(f'{self.__name} is a {self.__type}.')

class Dog(Pet):

    def __init__(self, name: str) -> None:
        super().__init__(name, 'dog', 'Whoof!')

class Cat(Pet):

    def __init__(self, name: str) -> None:
        super().__init__(name, 'cat', 'Meow!')

class Parrot(Pet):

    def __init__(self, name: str) -> None:
        super().__init__(name, 'parrot', 'Hello!')
    
class Hamster(Pet):

    def __init__(self, name: str) -> None:
        super().__init__(name, 'hamster', 'Squeak!')

dog = Dog('Tuffy')
cat = Cat('Lou')
parrot = Parrot('Roger')

print('task 3')
dog.get_sound()
cat.get_sound()
parrot.get_sound()
print()

# task 4, 5

class Employee:
    
    def __init__(self, name : str, surname : str, age : int):
        self.name = name
        self.surname = surname
        self.age = age

    def print(self):
        print('This is Employee class.')
    
    def __int__(self):
        return self.age

    def __str__(self) -> str:
        return f"""
Name: {self.name}
Surname: {self.surname}
Age: {self.age}
"""
    

class Manager(Employee):

    def print(self):
        print(f'The manager\'s name is {self.name} {self.surname}, they are {self.age} years old.')

class Worker(Employee):

    def print(self):
        print(f'The worker\'s name is {self.name} {self.surname}, they are {self.age} years old.')

class President(Employee):

    def print(self):
        print(f'The president\'s name is {self.name} {self.surname}, they are {self.age} years old.')

president = President('John', 'Werner', 34)
manager = Manager('Jane', 'Doe', 24)

print('task 4')
president.print()
manager.print()
print()
print('task 5')
print(president)
print(int(president))


