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
    def __init__(self, adress, owner);
        self.adress = adress
        self.owner = owner
        self.people = []
    def people()

murzik = Pet("Murzik", "Kot", "Мяу")
bob = Human("Bob", 24)

bob.play_with_pets()
bob.getpet(murzik)
bob.play_with_pets()