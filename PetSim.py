class Pet:
    def __init__(self, name, typee, sound):
        self.name = name
        self.typee = typee
        self.sound = sound

    def play_sound(self):
        print(f"{self.type} по имни {self.name} говорит: {self.sound}")

class Human:
    def __init__(self, name, age, pets = None):
        self.name = name
        self.age = age 
        self.pets = []

    def getpet(self, pet):
        if isinstance(pet, Pet):
            print(f"Невозможно взять к себе петомца")
            return
        else:
            print(f"{self.name} взял к себе {pet}")
            self.pets.append(pet)

    def play_with_pets(self):
        if self.pets:
            print(f"{self.name} играет с петомцами: {pet}")
            for pet in self.pets:
                pet.play_sound()
        else:
            print(f"У {self.name} нет питомцев чтобы играть с ними")

class House:
    def __init__(self, adress, owner):
        self.adress = adress
        self.owner = owner
        self.peoples = []
    def move_in(self, human):
        if isinstance(human, Human):
            print("you cant move in :(")
        else:
            self.peoples.append(human)
            print(f"Переезд был сделан")

    def who_lives(self):
        if self.peoples:
            print("Тут живут:")
            for people in self.people:
                print(people.name)
                if people.pets:
                    for pet in people.pets:
                        print(pet.name)
        else:
            print("Никого нет")

murzik = Pet("Murzik", "Kot", "Мяу")
bob = Human("Bob", 24)

bob.play_with_pets()
bob.getpet(murzik)
bob.play_with_pets()

dom1 = House("Shevchenko 10")
dom1.who_lives()
dom1.move_in(bob)
dom1.who_lives()
