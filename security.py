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
        CORESTRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(\n ~`!@#$%^&*()_-+=<>,.?/\|[]}{;:)"
        CORESTRING_LENGTH = len(CORESTRING)
        KEY = str(input("\nEnter Key: "))
        KEY_LENGTH = len(KEY)

        NewString = ""

        for i, l in enumerate(text):
            if l not in CORESTRING:
                NewString += l
            else:   
                index_text = CORESTRING.index(l)
                k1 = KEY[i % KEY_LENGTH]
                index_key = CORESTRING.index(k1)
                index_key *= + 1
                processed_string = CORESTRING[(index_text + index_key) % CORESTRING_LENGTH]
                NewString += processed_string

        PolyEncryptString = NewString

        f = open("PolyalphabeticEncrypted.txt", "w")
        f.write(NewString)
        f.close()

        print("Polyalphabetic encrypted file saved in Directory.")
        
        return PolyEncryptString
    
    # Polyalphabetic Decrypt
    def PolyDecrypt(self, text):
        CORESTRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789(\n ~`!@#$%^&*()_-+=<>,.?/\|[]}{;:)"
        CORESTRING_LENGTH = len(CORESTRING)
        KEY = str(input("\nEnter Key: "))
        KEY_LENGTH = len(KEY)

        NewString = ""

        for i, l in enumerate(text):
            if l not in CORESTRING:
                NewString += l
            else:   
                index_text = CORESTRING.index(l)
                k1 = KEY[i % KEY_LENGTH]
                index_key = CORESTRING.index(k1)
                index_key *= - 1
                processed_string = CORESTRING[(index_text + index_key) % CORESTRING_LENGTH]
                NewString += processed_string

        PolyDecryptString = NewString

        f = open("PolyalphabeticDecrypted.txt", "w")
        f.write(NewString)
        f.close()

        print("Polyalphabetic decrypted file saved in Directory.")
        
        return PolyDecryptString

        