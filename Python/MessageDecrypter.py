alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = -3
OriginalMessage = ''

message = input ('Please enter a message: ')


for character in message:
  if character in alphabet :
   position = alphabet.find(character)
   OriginalPosition = (position + answer)%26
   OriginalCharacter = alphabet[OriginalPosition]
   OriginalMessage += OriginalCharacter
  else :
    OriginalMessage += character
  
print ('Your decrypted message is ' , OriginalMessage)
  
