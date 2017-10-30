# -*- coding: utf8 -*-
import random
import json

def read_values_from_json(file, key):
    #crée un tableau vide
    values = []
    #ouvre le json passé en paramètre
    with open(file) as f:
        #stocke le contenu du json dans data
        data = json.load(f)
        #pour chaque element dans data
        for entry in data:
            #ajoute la valeur associée à la clé key passée en paramètre
            values.append(entry[key])
    #renvoie le tableau de valeurs
    return values

def message(character, quote):
    #met une majuscule au premeier mot
    n_character = character.capitalize()
    n_quote = quote.capitalize()
    #renvoie le message à afficher sur le prompt
    return "{} a dit : {}".format(n_character, n_quote)

def get_random_item_in(my_list):
    #renvoie un entier compris en 0 et la taille de la liste -1
    rand_numb = random.randint(0, len(my_list) - 1)
    #enregistre la valeur de la liste passée en param à l'indice rand_numb
    item = my_list[rand_numb]
    #renvoie cette valur
    return item # return the item

def get_random_quote():
    #récupère la liste de citations avec la fonction read_values_from_json
    all_values = read_values_from_json('quotes.json', 'quote')
    #renvoie une citation au hasard avec la fonction get_random_item_in
    return get_random_item_in(all_values)

#IDEM avec les noms
def get_random_character():
    all_values = read_values_from_json('characters.json', 'character')
    return get_random_item_in(all_values)

#le programme commence et demande à l'utilisateur ce qu'il veut faire
user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')

#tant qu'il ne quitte pas en tapant B
while user_answer != "B":
    #on affiche un nom et une citation au hasard formatés par message()
    print(message(get_random_character(), get_random_quote()))
    #redemande à l'utilisateur ce qu'il veut faire
    user_answer = input('Tapez entrée pour connaître une autre citation ou B pour quitter le programme.')
