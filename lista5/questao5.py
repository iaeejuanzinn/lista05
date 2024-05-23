def main():
    numeros = []
    for i in range(5):
        numero = int(input(f"Digite o {i+1}º número inteiro: "))
        numeros.append(numero)
    print("Os números digitados são:")
    for numero in numeros:
        print(numero)
if __name__ == "  main  ":
    main()