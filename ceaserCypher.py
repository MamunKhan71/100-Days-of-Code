def encrypt(message, shiftLetter):
    for num in message:
        num += shiftLetter

    return message


# def decrypt(message, shiftLetter):


choice = input("Type \"encrypt\" to Encrypt the message \"decrypt\" to Decrypt the message \n: ").lower()
if choice == "encrypt":
    message = input("Enter Your Message \n:")
    enc_msg = encrypt(message=message, shiftLetter=(input("Enter The Shift Number \n:")))
    print(enc_msg)
# elif choice == "decrypt":
#     decrypt(message, int(input("Enter The Shift Number \n:")))
