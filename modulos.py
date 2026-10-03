
#Modulos sao conjunto de recurso que da para utilizar. 
#o DATETIME é um modulo que tem o recurso datetime que tem uma função now() que traz a data e hora.

from datetime import datetime as dt  # usando um apleido/alias para a datetime simplificar. 



data_hora_atual = dt.now()

print("Data e Hora Atual :  " + str(data_hora_atual))


#calcular a idade do usuario


ano = int(input("Inserir o ano do seu nascimento: "))


idade = dt.now().year - ano


print(idade)
