import json


#função para ler o arquivo json 
def readJsonFile(fileName):
    data = {}    # se der erro volta vazio como iniciou                      
    try:
        with open(fileName, "r") as file:
            data = json.load(file)  
            #o load carrega o json como dicionario    
    except IOError:
        print("Could not read file")
    return data