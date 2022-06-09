print("Give me your first and last name")
name = input()

plik = open("dane.json", 'w')
plik.write('\n' + name)
plik.close()

## Dwa sposoby bo nie wiedziaem 

## import json
## with open('nowy.json', 'w') as f:
## f.write("Klaudiusz Jaworski")
