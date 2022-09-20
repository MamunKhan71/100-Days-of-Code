letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']


def encrypt(message, shiftLetter):
    cypher_text = ""
    for num in message:
        pos = letter.index(num)
        new_pos = pos + shiftLetter
        new_letter = letter[new_pos]
        cypher_text += new_letter
    return cypher_text


def decrypt(message, shiftLetter):
    decypher_text = ""
    for num in message:
        pos = letter.index(num)
        new_pos = pos - shiftLetter
        new_letter = letter[new_pos]
        decypher_text += new_letter
    return decypher_text

userInput = input("Type encode to encrypt and decode to decrypt a message \n:").lower()
encrypted_text = ""
shiftNo = 0
if userInput == "encode":
    messageType = input("Type your message here: ").lower()
    shiftNo = int(input("How many character shift you want? : "))
    encrypted_text = encrypt(shiftLetter=shiftNo, message=messageType)
    print(f"Your Encrypted Text is : {encrypted_text}")
elif userInput == "decode":
    messageType = input("Type your message here: ").lower()
    shiftNo = int(input("How many character shift you want? : "))
    decrypted_text = decrypt(message=messageType, shiftLetter=shiftNo)
    print(f"Your Decrypted Text is : {decrypted_text}")