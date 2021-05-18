print("---- CRYPTO CONVERTER ----")
print("Opção 1 - Converter Bitcoin em Reais")
print("Opção 2 - Converter Reais em Bitcoins")
print("Opção 3 - Sair")

inputOption=input("Digite a opção desejada: ")
option = int (inputOption)

if option == 1:
    inputValue=input("Digite o valor que deseja converter: ")
    value = float (inputValue)
    print(f"{value} Bitcoin equivale a R${value*237.782}")        
elif option == 2:
    inputValue=input("Digite o valor que deseja converter: ")
    value = float (inputValue)
    print(f"R${value} equivale a {value/237.782} em Bitcoin")
else:
    print("Fim do programa")
