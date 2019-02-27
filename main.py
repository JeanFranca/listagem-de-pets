import person
import animal
import os
from person import person
from animal import animal

option = '4'
owners = []

def clearSys(): # essa função serve para limpar o console de maneira mais simples
    os.system('cls' if os.name == 'nt' else 'clear')

def listClients(): # essa função serve para listar todos os clientes que possuimos no cadastro
    for i in range(len(owners)):
            print(str(i) + " - " + owners[i].name + ", Idade: " + owners[i].age + ", Genero: " + owners[i].genre)

while option != '0':
    clearSys()
    print("Olá digite a opção desejada:")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar pet")
    print("3 - Brincar com pet")
    print("0 - Sair")

    option = input("Digite aqui a opção: ")
    clearSys()

    if option == '1': # cadastro de cliente
        name = input("Digite o nome do cliente: ")
        age = input("Digite a idade do cliente: ")
        genre = input("Digite o genero do cliente: ")
        owners.append(person(name, age, genre))
    
    elif option == '2': # cadastro de pet
        listClients()
        owner = int(input('Digite o id do cliente: '))
        clearSys()
        petname = input("Digite o nome do pet: ")
        petage = input("Digite a idade do pet: ")
        petgenre = input("Digite o genero do pet: ")
        petspecies = input("Digite a especie do pet: ")
        owners[owner].pet.append(animal(petname,petage,petgenre,petspecies))
        print("Animal cadastrado com sucesso! ")
        input("pressione enter para continuar...")
    
    elif option == '3': # brincar com o pet
        listClients()
        owner = int(input('Digite o id do cliente: '))  
        clearSys()
        print("Selecione um pet para brincar: ")
        for j in range(len(owners[owner].pet)):
            print(str(j) + " - " + owners[owner].pet[j].name + " - " + owners[owner].pet[j].species)
        selectedpet = input("Digite a opcao desejada: ")
        clearSys()
        selectactivity = 4
        while selectactivity != '0':
            print("Digite a atividade que deseja que o pet faça: ")
            print("1 - falar ")
            print("2 - brincar ")
            print("0 - sair")
            selectactivity = input("digite aqui: ")
            clearSys()
            if selectactivity == '1':
                owners[owner].pet[int(selectedpet)].speak()
            elif selectactivity == '2':
                owners[owner].pet[int(selectedpet)].play()
            input("pressione enter para continuar...")
            clearSys()