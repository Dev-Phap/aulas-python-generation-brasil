#FUNCIONARIOS
#
#
#


#Nome
#Idade
#Cidade
#Profissão


#DICIONARIO (semelhante a um objeto)
pessoa = {
    "nome" : "",
    "idade" : 0,
    "cidade" : "",
    "profissão" : ""
}

pessoa["nome"] = input("Digite o seu nome:  ")
pessoa["idade"] = int(input("Digite sua idade:  "))
pessoa["cidade"] = input("Digite sua cidade:  ")
pessoa["profissão"] = input("Digite sua profissão:   ")

print(pessoa)

