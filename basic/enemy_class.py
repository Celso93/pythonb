# this is the parent class
# https://testautomationu.applitools.com/python-tutorial/chapter9.html

from typing_extensions import override
from person import Person

Luffy = Person("Luffy", "Monkey D.", 95, status=True)
Nami = Person("Nami", "", 50, status=False)
Zoro = Person("Zoro", "Roronoa", 75, status=True)

Luffy.emote()

# this is the child
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    #@override
    def introduce(self):
        super().introduce(self)
        print("I OVERRIDED YOUR METHOD FROM PERSON HAHA! PS: This is a polymorphism !")

    def hurt(self, pirate):
        if self.weapon == 'rock':
            pirate.health -= 10

        elif self.weapon == 'stick':
            pirate.health -= 5

        print(pirate.health)

    def insult(self, pirate):
        if pirate.health <= 80:
            print("{}, you are tired and weak".format(pirate.firstname))

    def steal(self, pirate):
        print("ha ha ha, {}, I have your stuff!".format(pirate.firstname))

        if pirate.status == True:
            pirate.status = False


Kaido = Enemy("rock", "Kaido", "Yonkou ", 100, status=True)
Kaido.hurt(Luffy)
Kaido.insult(Zoro)
Kaido.steal(Nami)
Kaido.introduce()