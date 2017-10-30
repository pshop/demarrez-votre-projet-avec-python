import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "Kirikou"
]

def get_random_item_in(my_list):
    # get a random number
    rand_num = random.randint(0, len(my_list) - 1)
    item = my_list[rand_num] # get a quote from a list
    # returned value
    return item

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    return "{} à dit: \'{}\'".format(character, quote)

user_answer = input('Appuyez sur enter pour une nouvelle citation ou \'B\' pour quitter')

while user_answer != 'B':
    print(message(get_random_item_in(characters),get_random_item_in(quotes)))
    user_answer = input('Appuyez sur enter pour une nouvelle citation ou \'B\' pour quitter')
