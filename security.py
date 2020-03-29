class Security():

    # Initialize
    def __init__(self):
        pass

    # Caesar Cipher Encryption
    def CaesarEncrypt(self, text):
        CORESTRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(\n ~`!@#$%^&*()_-+=<>,.?/\|[]}{;:)"
        SHIFT = int(input("\nEnter Shift: "))
        SHIFT = int(SHIFT)

        NewString = ""
        for character in text:
            char = CORESTRING.find(character)
            new_char = char + SHIFT
            
            if character in CORESTRING:
                NewString = NewString + CORESTRING[new_char]
            else:
                NewString = NewString + character

        CaesarEncryptString = NewString

        f = open("CaesarCipherEncrypted.txt", "w")
        f.write(NewString)
        f.close()

        print("Caesar encrypted file saved in Directory.")
        
        return CaesarEncryptString

    # Caesar Cipher Decryption
    def CaesarDecrypt(self, text):
        return

    # Polyalphabetic Encrypt
    def PolyEncrypt(self, text):
        return
    
    # Polyalphabetic Decrypt
    def PolyDecrypt(self, text):
        return

        