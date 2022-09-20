letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
          'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
          's', 't', 'u', 'v',
          'w', 'x', 'y', 'z']


def caesar(message, shiftLetter, symbol):
    cypher_text = ""
    new_pos = 0
    for num in message:
        pos = letter.index(num)
        if symbol == "+":
            new_pos = pos + shiftLetter
        elif symbol == "-":
            new_pos = pos - shiftLetter
        new_letter = letter[new_pos]
        cypher_text += new_letter
    return cypher_text


userInput = input("Type encode to encrypt and decode to decrypt a message : ").lower()
encrypted_text = ""
shiftNo = 0
if userInput == "encode":
    messageType = input("Type your message here: ").lower()
    shiftNo = int(input("How many character shift you want? : "))
    encrypted_text = caesar(shiftLetter=shiftNo, message=messageType, symbol="+")
    print(f"Your Encrypted Text is : {encrypted_text}")
elif userInput == "decode":
    messageType = input("Type your message here: ").lower()
    shiftNo = int(input("How many character shift you want? : "))
    decrypted_text = caesar(shiftLetter=shiftNo, message=messageType, symbol="-")
    print(f"Your Decrypted Text is : {decrypted_text}")
