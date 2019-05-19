alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("Please enter a message to encrpt: ")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("Please enter a whole number from 1-25 to be your key.\n"))
encryptedString = ""
for currentCharachter in stringToEncrypt:
  position = alphabet.find(currentCharachter)
  newPosition = position + shiftAmount
  encryptedString = encryptedString + alphabet[newPosition]
print("Your encrypted message is", encryptedString)
