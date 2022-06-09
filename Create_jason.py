def create_json():
    print(f"Give me your name  and surname")
    name = input("Name: \n")
    surname = input("Surename: \n")

    json = open("dane.json", "w+")
    json.write(name + " " + surname)
    json.close()

create_json()
