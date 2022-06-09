print("Give me your first and last name")
name = input()

plik = open("dane.json", 'w')
plik.write('\n' + name)
plik.close()

