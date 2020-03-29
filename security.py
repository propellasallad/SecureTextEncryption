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
        return
    
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

        