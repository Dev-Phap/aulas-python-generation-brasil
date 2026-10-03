
compras = []

item = ""

primeiro_item = 0

#----------------------------

compras = ["arroz", "feijão", "banana", "Leite"]

item = input("Insira o item :  ")

compras.append(item)
compras.append("Tang")
compras.append("Chocolate") 



compras.pop() #remove ultimo item adicionado a lista. 

#-------------------------------------------
primeiro_item = compras[0]



#-------------------------------------------

print(compras)

print(primeiro_item)