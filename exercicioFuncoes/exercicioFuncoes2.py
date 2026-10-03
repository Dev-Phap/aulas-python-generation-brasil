#Função que é para duplicar o alphabeto
def getDoubleAlphabet(alphabet):
    return alphabet + alphabet                     

#Função so para pegar mensagem e.e
def getMessage():
    return  input("Digite a mensagem a ser criptografada: ")
    

# Função para pegar a chave de cifra 
def getCipherKey():
    return input("Digite a chave de cifra (1 a 25): ")
    

# função para criptografar (com auxilio de ia para guiar)
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""          
    message = message.upper()
    key = int(cipherKey)            

    for currentCharacter in message:
        position = alphabet.find(currentCharacter)   

        if position == -1:
            encryptedMessage = encryptedMessage + currentCharacter
        else:
            newPosition = position + key
            encryptedMessage = encryptedMessage + alphabet[newPosition]

    return encryptedMessage

# agora uma função que vai descriptografar chamando a outra função que criptografa onde  vai fazer o processo inverso da criptografia por conta da chave negativa. 
def decryptMessage(message, cipherKey, alphabet):
    negativeKey = -int(cipherKey)            
    return encryptMessage(message,negativeKey, alphabet)                     

# por fim uma função que vai correr o programa e chamando as outras criada anteriormente. 
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("Alfabeto: " + myAlphabet)

    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print("Alfabeto duplicado: " + myAlphabet2)

    myMessage = getMessage()
    print("Mensagem: " + myMessage)

    myCipherKey = getCipherKey()
    print("Chave: " + str(myCipherKey))

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)       
    print("Mensagem criptografada: " + myEncryptedMessage)

    myDecryptedMessage = decryptMessage(myEncryptedMessage,myCipherKey,myAlphabet2)       
    print("Mensagem descriptografada: " + myDecryptedMessage)


# Sem esta linha, nada acontece: definir não é executar
runCaesarCipherProgram()