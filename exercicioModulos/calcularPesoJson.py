import jsonFileRead as js

# Aqui estou usando a função para ler o arquivo que esta em outro modulo e passo o caminho do arquivo para ler, tambem estou usando um alias para o modulo. 
dados = js.readJsonFile("files/insulin.json")

# Do que retornar, vai ser armazenado em dados, e fazemos a verificação se dicionario vazio conta como "falso", então o if só entra se leu algo
if dados:
    # Acesso em camadas: dados -> molecules -> bInsulin
    bInsulin = dados["molecules"]["bInsulin"]
    aInsulin = dados["molecules"]["aInsulin"]
    molecularWeightInsulinActual = dados["molecularWeightInsulinActual"]

    insulin = bInsulin + aInsulin

    print("bInsulin: " + bInsulin)
    print("aInsulin: " + aInsulin)
    print("molecularWeightInsulinActual: " + str(molecularWeightInsulinActual))

    # Cálculo (mesmo calculo de exercicios anteriores porem aqui passo valor importado do json)
    aaWeights = dados["weights"]
    aaCountInsulin = {x: float(insulin.upper().count(x)) for x in aaWeights}
    molecularWeightInsulin = sum(aaCountInsulin[x] * aaWeights[x] for x in aaWeights)

    print("The rough molecular weight of insulin: " + str(round(molecularWeightInsulin, 2)))

    percentError = abs(molecularWeightInsulin - molecularWeightInsulinActual) / molecularWeightInsulinActual * 100
    print("Percent error: " + str(round(percentError, 2)) + "%")
else:
    print("Fim do Programa")