# contador = 1
 
# print("Valor inicial do Contador: " + str(contador))
 
# while contador <= 5:    # enquanto(while) expressão lógica = true/false
#     print(contador)     # exibir o número do contador
#     contador = contador + 1
 
# print("Valor final do Contador: " + str(contador))



# total = 0
# numero = 0
 
# numero = int(input("Insira um número positivo: "))
 
# while numero > 0:
#     total = total + numero
#     numero = int(input("Insira um número positivo: "))
 
# print(f"O total dos números digitados é: {total}")


# nomes = ["Celso", "Paulo", "Thalles"]

# for item in nomes: 
#     print("Seja bem vindo/a " + item)

# print("Final do programa")



lista = []
valor = 0
contador = 0


while contador <= 3:
    valor = int(input("insira um valo:  "))
    lista.append(valor)
    contador = contador + 1 

for item in lista:
    print(item * item)

