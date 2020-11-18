TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
hesla = [("bob", "123"), ("ann", "pass123"), ("mike", "password123"), ("liz", "pass123")]
print("-"*50)
print("Welcome to the app, please log in.")
jmeno = input("USERNAME: ")
heslo = input("PASSWORD: ")
if (jmeno, heslo) not in hesla:
    print("Sorry, but entered username or password is incorrect.")
    quit()
print("-"*50)
print("We have 3 texts to be analyzed.")
vyber = int(input("Enter a number btw. 1 and 3 to select: "))
print("-"*50)
vybrany_text = TEXTS[vyber - 1]
cista_slova = vybrany_text.strip(".,:;")
seznam = cista_slova.split()
velke = []
velka = []
mala = []
cislo = []
index = 0
soucet = 0
while index < len(seznam):
    slovo = seznam[index]
    if slovo.istitle():
        velke.append(slovo)
    if slovo.isupper():
        velka.append(slovo)
    if slovo.islower():
        mala.append(slovo)
    if slovo.isdecimal():
        cislo.append(slovo)
        soucet = soucet + float(slovo)
    index += 1
print("There are", len(seznam), "words in the selected text.")
print("There are", len(velke), "titlecase words.")
print("There are", len(velka), "uppercase words.")
print("There are", len(mala), "lowercase words.")
print("There are", len(cislo), "numeric strings.")
print("-"*50)
list = []
for i in seznam:
    list.append(len(i))
    list.sort()
for i in range(1, list[-1] + 1):
    if list.count(i) != 0:
        print(i, "*" * list.count(i), list.count(i))
print("-"*50)
print("If we summed all the numbers in this text we would get: ", soucet)
print("-"*50)
