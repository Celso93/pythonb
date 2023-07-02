# Python classes allow programmers to group data and information like variables and functions into a single organized unit.
# https://testautomationu.applitools.com/python-tutorial/chapter8.html

# What is an instance variable? A variable that is only available to a specific method
# 2. What is a class variable? A variable that is available to every class method
import random


class Person:

    def __init__(self, firstname, lastname, health, status):

        """ initialize attributes to be used in/available for all \
        class methods in this class, and for class Objects created \
        by this class. """

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hi, I'm {} {}".format(self.lastname, self.firstname))

    def emote(self):
        emotion = random.randrange(1,3)

        if emotion == 1:
            print("{} is happy today".format(self.firstname))

        elif emotion == 3:
            print("{} is sad right now".format(self.firstname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))

        elif self.health >= 76:
            print("{} is a little tired today.".format(self.firstname))

        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))

        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))

        else:
            print("{} is unconscious.".format(self.firstname))


# Luffy = Person("Luffy", "Monkey D.", 95, status=True)
# Nami = Person("Nami", "", 50, status=False)
# Zoro = Person("Zoro", "Roronoa", 88, status=True)

# print("{} is my friend? {}".format(Luffy.firstname, Luffy.status))

# Luffy.introduce()
# Nami.introduce()
# Zoro.introduce()

# Luffy.emote()
# Nami.emote()
# Zoro.emote()

# Luffy.status_change()
# Nami.status_change()
# Zoro.status_change()