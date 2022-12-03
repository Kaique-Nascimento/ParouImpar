import random

print("par ou impar")
placarpc = 0
placar = 0

while (True):
    esc = input(str("par ou impar? [0/1] ou maior que 2 para sair: "))
    
    if (esc == "0"):
        pc = "impar"
    elif (esc == "1"):
        pc = "par"
    else:
        print("Tchau!")
        input()
        break  
    num = int(input("Digite um número de 1 - 5: "))
    if (num >= 6):
        print("Animal, é de 1 a 5")
        break
    numpc = random.randint(1, 5)
    print("=-"*6)
    print(f"Você colocou: {num}")
    print("---------")
    print(f"PC colocou: {numpc}")
    print("=-"*6)
    conta = num + numpc;
    print(f"O resultado de {num} + {numpc} deu: {conta}")
    if (conta % 2) == 0:
        print(f"{conta} é par")
        if (pc == "par"):
            print("PC ganhou")
            placarpc+=1
        else:
            print(f"Você ganhou!")
            placar+=1
    else:
        print(f"{conta} é impar")
        if (pc == "impar"):
            print("PC ganhou")
            placarpc+=1
        else:
            print(f"Você ganhou!")
            placar+=1
    print("\nPlacar:")
    print(f"Você = {placar} || PC = {placarpc}")
    des = input(str("Deseja jogar novamente? [s/n] "))
    if (des == "n"):
        break

