def create_txt():
    print(f"Give me your name  and surname")
    name = input("Name: \n")
    surname = input("Surename: \n")

    txt = open("dane.txt", "w+")
    txt.write(name + " " + surname)
    txt.close()

create_txt()
