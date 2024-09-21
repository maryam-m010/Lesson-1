class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        print(f"Hello my name is {self.name} I am {self.age} years old")

person_1 = Person("Maryam", 14)
person_1.talk()

person_2 = Person("Molly", 13)
person_2.talk()
