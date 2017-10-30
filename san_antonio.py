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
    # todo: get a random number
    item = my_list[0] # get a quote from a list
    print(item) # show the quote in the interpreter
    return "program is over" # returned value

user_answer = 'A'

while user_answer != 'B':
    print(get_random_item_in(quotes))
    user_answer = input('Appuyez sur enter pour une nouvelle citation ou \'B\' pour quitter')
