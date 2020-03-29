import security
s = security.Security()
openfile = str(input("\nEnter file (Example.txt): "))

with open(openfile, "r") as f:
    text = f.read()

selected_file = int(input("\nWould you like to Encrypt or Decrypt a file?\n-------------------------\n1. Encrypt\n2. Decrypt\n"))

if selected_file == 1:
    encryption_method = int(input("\nPlease select your encryption method\n-------------------------\n1. Caesar\n2. Polyalphabetic\n"))
    if encryption_method == 1:
        s.CaesarEncrypt(text)
    elif encryption_method == 2:
        s.PolyEncrypt(text)
    else:
        print("Invalid option.")
elif selected_file == 2:
    decryption_method = int(input("\nPlease select your decryption method\n-------------------------\n1. Caesar\n2. Polyalphabetic\n"))
    if decryption_method == 1:
        s.CaesarDecrypt(text)
    elif decryption_method == 2:
        s.PolyDecrypt(text)
    else:
        print("Invalid option.")
else:
    print("Invalid option.")
