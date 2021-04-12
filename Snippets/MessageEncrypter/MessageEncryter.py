message = input("Enter The Message You Want To Encrypt : ")
key = int(input("Enter How Many Charecters You Want To Shift (1-26) : "))

secretMessage = ""

for char in message:
    if char.isalpha():
        charCode = ord(char)
        charCode += key

        if char.isupper():
            if charCode > ord("Z"):
                charCode -= 26

            elif charCode < ord("A"):
                charCode += 26

        else:
            if charCode > ord("z"):
                charCode -= 26

            elif charCode < ord("a"):
                charCode += 26

        secretMessage += chr(charCode)

    else:
        secretMessage += char

print("Encrypted : ", secretMessage)

key = -key
orignalMessage = ""

for char in secretMessage:
    if char.isalpha():
        charCode = ord(char)
        charCode += key

        if char.isupper():
            if charCode > ord("Z"):
                charCode -= 26

            elif charCode < ord("A"):
                charCode += 26

        else:
            if charCode > ord("z"):
                charCode -= 26

            elif charCode < ord("a"):
                charCode += 26

        orignalMessage += chr(charCode)

    else:
        orignalMessage += char

print("Decrypted : ", orignalMessage)
