import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']

def capitalize_suffix(name):
    return name.capitalize()

cap_suffix = list(map(capitalize_suffix, suffixes))

def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

random_names = [create_fantasy_name(prefixes, cap_suffix) for i in range(10)]

def fire_in_name(name):
    return 'Fire' in name

def concatenate_names(name1, name2):
    return name1 + name2

filtered = list(filter(fire_in_name, random_names))
reduced = reduce(concatenate_names, filtered)

def display_name_info():
    print("Fantasy Names:")
    for name in random_names:
        print(name)
    print("Filtered:", filtered)
    print("Reduced:", reduced)

display_name_info()
