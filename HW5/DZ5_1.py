myString = input("Введите предложение: ")

def delWords(yourStr):

    yourStr=tuple(filter( lambda x: "абв" not in x , myString.split() ))
    return " " .join(yourStr)

print (delWords(myString))