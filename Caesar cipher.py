alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter a message to encrpt: \n")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Please enter a whole number from 1-25 to be your key.\n"))
encryptedString = ""
for currentCharachter in stringToEncrypt:
  position = alphabet.find(currentCharachter)
  newPosition = position + shiftAmount
  if currentCharachter in alphabet:
    encryptedString = encryptedString + alphabet[newPosition]
  else:
    encryptedString = encryptedString + currentCharachter
print("Your encrypted message is", encryptedString)
#для расшифровки необходимо использовать ключ с "-": "-6"
