import re

conteudo_bruto = ""
texto_sem_numeros = ""
texto_sem_barras = ""
texto_sem_espacos = ""
texto_sem_origin = ""
texto_limpo = ""


#Pedi a ia para saber como ler o arquivo que criamos com a sequencia "suja" do site informado no enunicado do exercicio. 
with open("preproinsulin-seq.txt", "r") as arquivo:
    conteudo_bruto = arquivo.read()


#Depois pedi como funcionava o regex no python pediu para importa o re, e trabalhar com o re.sub dando um exemplo. entao segui esse exemplo criando uma variavel para guardar sempre o valor de retorno.

#Removendo os numeros com expressões regulares.
texto_sem_numeros = re.sub(r"\d+", "", conteudo_bruto)

#Usei da mesma logica para limpar as barras apos limpar os numeros
#Removendo barras

texto_sem_barras = re.sub(r"//","",texto_sem_numeros)

#Usei a mesma logica para limpar os espaços em branco o comando do regex pedi para ia mandar.
#Removendo espaços em branco 
texto_sem_espacos =  re.sub(r"\s+","",texto_sem_barras)

#Segui usando a mesma logica 
#Removendo ORIGIN
texto_sem_origin = re.sub(r"ORIGIN","",texto_sem_espacos)

#Segui usando a mesma logica  ate fica totalmente limpo
#Removendo Quebra de linha
texto_sem_quebra_de_linhas = re.sub(r"[\r\n]","",texto_sem_origin)

#Sei que nao precisava dessa ultima variavel so para guardar o texto limpo porem para melhor entendimento preferi fazer. 
#Adicionando Texto Limpo
texto_limpo = texto_sem_quebra_de_linhas

#Por fim imprimi para conferir e deu certo com 110caracteres
print(texto_limpo)

