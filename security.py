class Security():

    # Initialize
    def __init__(self):
        pass

    # Caesar Cipher Encryption
    def CaesarEncrypt(self, text):
        return
    
    # Caesar Cipher Decryption
    def CaesarDecrypt(self, text):
        CORESTRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(\n ~`!@#$%^&*()_-+=<>,.?/\|[]}{;:)"
        SHIFT = int(input("\nEnter Shift: "))
        SHIFT = int(SHIFT)

        NewString = ""
        for character in text:
            char = CORESTRING.find(character)
            new_char = char - SHIFT
            
            if character in CORESTRING:
                NewString = NewString + CORESTRING[new_char]
            else:
                NewString = NewString + character
        
        CaesarDecryptString = NewString

        f = open("CaesarCipherDecrypted.txt", "w")
        f.write(NewString)
        f.close()

        print("Caesar decrypted file saved in Directory.")
        
        return CaesarDecryptString
    
    # Polyalphabetic Encrypt
    def PolyEncrypt(self, text):
        return
    
    # Polyalphabetic Decrypt
    def PolyDecrypt(self, text):
        return

        