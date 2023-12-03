"""

projekt_1.py: první projekt do Engeto Online Python Akademie

author: Ivana ROHOVÁ

email: bytypr@gmail.com

discord: Ivana #3941

"""

import os
from task_template import TEXTS

uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
oddelovac = 50 *"-"
list_of_words = []

# if __name__ == '__main__':

def text_analyser():
    count_of_words()
    count_of_words_start_capital()
    count_of_words_capitals_only()
    count_of_words_lowers_only()
    count_of_numbers()
    sum_of_numbers()
    graf()

   #  počet slov
def count_of_words():    
    for word in TEXTS[number_of_text].split():
        list_of_words.append(word.strip(",.:;"))
    while "" in list_of_words:
            list_of_words.remove("")
    print(f"There are {len(list_of_words)} words in the selected text.")

#počet slov začínající s velkým písmenem
def count_of_words_start_capital():
    list_of_capitals = []
    for word in list_of_words:
        firts_letter = word[0].isupper()
        if firts_letter is True:
            list_of_capitals.append(word)
    print(f"There are {len(list_of_capitals)} titlecase words.")

#počet slov psaných velkými písmeny
def count_of_words_capitals_only():
    list_of_uppers = []
    for word in list_of_words:
        if word.isupper() and word.isalpha():
            list_of_uppers.append(word)
    print(f"There are {len(list_of_uppers)} uppercase words.")

#počet slov psaných malými písmeny
def count_of_words_lowers_only():
    list_of_lowers = []
    for word in list_of_words:
        if word.islower() and word.isalpha():
            list_of_lowers.append(word)
    print(f"There are {len(list_of_lowers)} lowercase words.")

list_of_numbers = []
#počet čísel (ne cifer)
def count_of_numbers():
   
    for word in list_of_words:
        if word.isdigit():
            list_of_numbers.append(word)
    print(f"There are {len(list_of_numbers)} numeric strings.")

#suma všech čísel (ne cifer) v textu
def sum_of_numbers():
    total = 0
    for number in list_of_numbers:
        total += int(number)
    print(f"The sum of all the numbers {total}.")
    print (oddelovac)

# sloupcový graf četnosti různých délek slov v textu.   
def graf():
    dict_len_num = {}
    count_of_len_words = [] #Vypsání délek textu do listu
    for word in list_of_words:
        count_of_len_words.append(len(word))

    #Spočítání délek z listu a zapsáno do slovníku
    for number in count_of_len_words:
        number_count = count_of_len_words.count(number)
        dict_len_num.update({number: number_count})

    print(
        f"LEN|", "OCCURENCES".center(14), "|NR."
    )
    print(oddelovac)

    list_len_num = list(dict_len_num.keys())
    list_len_num.sort()

    for i in list_len_num:
        hodnota = dict_len_num.get(i)
        print(f"{i:>3}|{'*' * hodnota:<16}|{hodnota}")

    print(oddelovac)
    
#login + vstup uživatele + analýza
os.system("cls")
username = input("Enter username: ")
password = input("Enter password: ")

if username in uzivatele.keys() and password == uzivatele[username]:
    print(f"""
{oddelovac}
Welcome to the app, {username}
We have {(len(TEXTS))} texts to be analyzed
{oddelovac}""")
    chosen_number = input(f"Enter a number btw. 1 and {(len(TEXTS))} to select: ")
    print(oddelovac)
    if chosen_number.isdigit() and int(chosen_number) <= len(TEXTS):
        number_of_text = int(chosen_number) -1
        text_analyser()
    else:
        print("incorrect input, terminating the program..")
        quit()
    
else:
    print("unregistered user, terminating the program..")
    quit()
    

