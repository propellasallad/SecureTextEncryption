class Security():

    # Initialize
    def __init__(self):
        pass

    # Caesar Cipher Encryption
    def CaesarEncrypt(self, text):
        return
    
    # Caesar Cipher Decryption
    def CaesarDecrypt(self, text):
        return
    
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
        return

        