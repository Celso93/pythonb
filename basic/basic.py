# Lists : A Python list is a collection of items.

from typing import Dict

print("-----------------List------------------------")

list = ["Luffy", "Zoro", "Nami", "Nami", 3, True]

# Check if this item exist on this list
print("Luffy" in list)

# Return the item on this position
print(list.index(3))

# This method will check how many item with this value exist on list
print(list.count("Nami"))

numbers = [5, 1928, 4, 17, 68, 73.76, 20.458]

# This going to organize the correct order. But all theses item need to be integer/float
numbers.sort()
print(numbers)

# This will add a list in another list
numbers.extend(list)
print(numbers)


print("-----------------Dictionary------------------------")
# Dictionaries are a type of Python data collection that stores the data in key/value pairs.
# https://testautomationu.applitools.com/python-tutorial/chapter7.html
# The keys are generally made of Strings, integers, or tuples, and need to be both unique and immutable.
# "key": value

strawhat_crew = {
    "capitan": "Luffy",
    "sword-master": "Zoro",
    "navigation": "Nami",
    "crew-number": 10
}

# get the item from this dictionary
print(strawhat_crew.get("capitan"))

# Show all items
print(strawhat_crew.items())

# Show all keys
print(strawhat_crew.keys())
print(strawhat_crew.values())

# Remove the last item from the dictonary
print(strawhat_crew.popitem())

strawhat_crew2 = {
    "capitan": "Luffy",
    "sword-master": "Zoro",
    "navigation": "Nami",
    "crew-number": 10
}


# setdefault you can see the value and..
# allows us to set a default value when a key is not in the dictionary and to add that value to the dictionary.
print(strawhat_crew2.setdefault("capitan"))
print(strawhat_crew2)
print(strawhat_crew2.setdefault("musician", "Brook"))
print(strawhat_crew2.setdefault("sword-master", "You cannot change the value using this method"))
print(strawhat_crew2)

# .update - We can update:

strawhat_wano = {
    "capitan": "Luffy",
    "swordsman": "Zoro",
    "navigation": "Nami",
    "crew-number": 10
}

new_menbers = {
    "fishman": "Jimbe",
    "figther": "Yamato",
    "Power": 4000
}

# list1 with another list2
strawhat_wano.update(new_menbers)
print(strawhat_wano)

# values from the list1 with another list2
new_menbers = {
    "fishman": "Jinbe",
    "Power": 8000
}
strawhat_wano.update(new_menbers)
print(strawhat_wano)

# values from the list2 with another list2
update_name = {
    "capitan": "Monkey D. Luffy"
}
strawhat_wano.update(update_name)
print(strawhat_wano)

# values from a list
strawhat_wano.update( swordsman = "Roronoa Zoro")
print(strawhat_wano)

print("-----------------Functions------------------------")

# function with args and kwargs
def user_info(name, age, city):
    """This function prints name, age, and city from an argument provided to the function."""
    print("{} is {} years old, from {}".format(name, age, city))

user_info("Janet", 58, "Oklahoma City")

# args & kwargs
# more information about kwargs: https://testautomationu.applitools.com/python-tutorial/chapter3.html
def user_info2(name, age=0, city="Tucson"):
    '''This functoin prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info2("Micah")
user_info2(age=56, name="roger")

# *args and **kwargs
def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her email is {}.".format(fname, lname, company, email))


application("Jess", "Ingrass", "mail@mail.com", "Teach Code", 75000, hire_date="September 2010")