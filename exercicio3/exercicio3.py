# versão do python = 3.14.6

#a variavel a baixo armazena a sequência da pré-proinsulina humana 

#valor gerado no exercicio 1
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


#variaveis abaixo irão armazenar partes restante da sequencia da insulina. 

#primeira parte
lsInsulin = "malwmrllpllallalwgpdpaaa"

#segunda parte
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"

#terceira parte
aInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"

#quarta parte
cInsulin = "giveqcctsicslyqlenycn"


insulin = lsInsulin + bInsulin + aInsulin + cInsulin


#imprimindo valores com print 


print("Sera apresentado abaixo a sequencia da pré-proinsulina humana")


print(preproInsulin)


print("Primeira parte: " + lsInsulin)

print("Segunda parte: " + bInsulin)

print("Terceira parte: " + aInsulin)

print("Quarta parte:  " + cInsulin)


# Exercicio 4 - Calcular o peso molecularaproximado da insulina



# Dicionário: cada chave (letra do aminoácido) está associada
# a um valor (peso daquele aminoácido).

aaWeigths = {
    'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
    'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17,
    'M': 149.21, 'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20,
    'S': 105.09, 'T': 119.12, 'V': 117.15, 'W': 204.23, 'Y': 181.19
}



# a variavel aaCountInsulin vai receber um novo dicionario, onde vai ter um loop que passa por todo dicionario aaWeigths e pega o valor "x" da chave e usa de funções integradas como .count para contar quantas veses ele aparece na sequencia "insulin"  e tambem esta sendo tratado para fica em maiusculo. 
# a contagem quem fez foi a ia, eu so compreendi o que as funções e loops estao fazendo. 
aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeigths}


# Aqui  a variavel molecularWeigthInsulin recebe o retorno da função integrada soma/ sum onde calcula o a quantidade contada do valor da chave 'C' por exemplo, teve 4x aparecendo C na sequencia insulin entao pega esse valor e multiplica pelo valor cadastrado no dicionario aaWeigths em 'C' ai o for faz o loop para fazer essa multiplicação com todas as letras do dicionario aaCountInsulin e o sum vai somar tudo o que retornar dessas multiplicações. 
molecularWeigthInsulin = sum(aaCountInsulin[x] * aaWeigths[x] for x in aaWeigths)


# imprime o peso molecular e ja convertendo para fazer a contatenação no mesmo tipo str.
print("Peso molecular aproximado: " + str(molecularWeigthInsulin))


realWiegth = 5807.63


# aqui o errorPercent vai receber o resultado do calculo do valor absoluto da molecularWieghtInsuiln - realWeigth, dividio pela multiplicação de realWeigth * 100 para descobrri o percentual de erro. 
errorPercent = abs(molecularWeigthInsulin - realWiegth) / realWiegth * 100



#imprimindo o percentual de erro. 
print("Percentual de erro: " + str(errorPercent))

