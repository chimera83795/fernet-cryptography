#!/usr/bin/python3
import os
from cryptography.fernet import Fernet
files = []
en_files = []
de_files = []
curennt_path = os.getcwd()
key = None
def showbanner():
    print("""
#####################################################################
                                                    ____________     
    ____                                           |            |    
   |                                  |            |  O         |    
 __|____                            __|__       ___|_____       |___ 
   |      ____    __  |____    ____   |        |                |   |
   |     |____|  /    |    |  |____|  |        |    ____________|   |
   |     |____   |    |    |  |____   \        |   |                |
   |                                   \__     |___|        ________|
   |                                               |            |    
                            en-/decryptor          |        O   |    
                                                   |____________|    
                                       by chimera83795
#####################################################################
                                                                    
!!!Warning! This is for educational porpuse only!!!                  
Doesn't use this programm against files without permission!            
The author don't take any resonsability fot things,                  
that are done with this programm!                                    
Also be aware, that files, that are encrypted with this programm,    
could be encrypted, locked or not accessable forever!                
It's recommanded to only encrypt copies!                             
""")
def open_key():
    global key
    key_name = input("[*]Please enter the name of the .key file: ")
    key_path = input("[*]Please enter the folder of the key: ")
    try:
        os.chdir(key_path)
        with open(key_name, 'rb') as thekey:
            key = thekey.read()
            return key
    except:
        print("[-]Can't access the key")
        open_key()

def encrypt(path, target_files):
    global files, key
    try:
        os.chdir(path)
    except:
        print("[-]Please enter a valid path")
        encrypt_setup()
    number = 0
    for file in os.listdir():
        for target_file in target_files:
            if file == target_file and os.path.isfile(file):
                files.append(file)
                number += 1
    key_choice = input("[*]Use a already created key.key file?[y/n] ")
    if key_choice == 'y':
        open_key()
    elif key_choice == 'n':
        os.chdir(curennt_path)
        key = Fernet.generate_key()
        with open("thekey.key" , "wb") as thekey:
            thekey.write(key)
            print("[+]Successfully saved the key as thekey.key in current workingdirectory ")
        
    os.chdir(path)
    for file in files:
            try:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_encrypted)
                    print("[+]Successfully encrypted " + file)
            except:
                print("[-]" + file + " wasn't encrypted")
    print("[*]Encryption finished")
    files = []
    input()

def decrypt(path, target_files):
    global files, key
    try:
        os.chdir(path)
    except:
        print("[-]Please enter a valid path")
        decrypt_setup()
    open_key()
    number = 0
    os.chdir(path)
    for file in os.listdir():
        for target_file in target_files:
            if file == target_file and os.path.isfile(file):
                files.append(file)
                number += 1
    os.chdir(path)
    for file in files:
            try:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(key).decrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)
                    print("[+]Successfully decrypted " + file)
            except:
                print("[-]" + file + " wasn't decrypted")
    print("[*]Decryption finished")
    files = []
    input()
    
def encrypt_all(path):
    global files, curennt_path, key
    try:
        os.chdir(path)
    except:
        print("[-]Please enter a valid path")
        encrypt_setup()
    number = 0
    for file in os.listdir():
        files.append(file)
        number += 1
    key_choice = input("[*]Use a already created key.key file?[y/n] ")
    if key_choice == 'y':
        open_key()
    elif key_choice == 'n':
        os.chdir(curennt_path)
        key = Fernet.generate_key()
        with open("thekey.key" , "wb") as thekey:
            thekey.write(key)
            print("[+]Successfully saved the key as thekey.key in current workingdirectory ")    
    os.chdir(path)
    for file in files:
            try:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_encrypted = Fernet(key).encrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_encrypted)
                    print("[+]Successfully encrypted " + file)
            except:
                print("[-]" + file + " wasn't encrypted")
    print("[*]Encryption finished")
    files = []
    input()


def decrypt_all(path):
    global files, curennt_path, key
    number = 0
    try:
        os.chdir(path)
    except:
        print("[-]Please enter a valid path")
        decrypt_setup()
    for file in os.listdir():
        if file == "fernet_encryption.exe" or file == "thekey.key":
            continue
        if os.path.isfile(file):
            files.append(file)
            number += 1
    open_key()
    os.chdir(path)
    for file in files:
            try:
                with open(file, "rb") as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(key).decrypt(contents)
                with open(file, "wb") as thefile:
                    thefile.write(contents_decrypted)
                    print("[+]Successfully decrypted " + file)
            except:
                print("[-]" + file + " wasn't decrypted")
    print("[*]Decryption finished")
    files = []
    input()

def encrypt_setup():
    global en_files
    en_path = input("encrypter>[*]Enter target path of the folder: ")
    if en_path == 'options' or en_path == 'showoptions':
        print("""
number = decrypts/encrypts x target files
all    = decrypts/encrypts all files in the folder

""")
        encrypt_setup()
    en_number = input("encrypter>[*]How many files do you want to encrypt? ")
    if en_number == 'all':
        encrypt_all(en_path)
    elif en_number == 'options' or en_number == 'show options':
        print("""
number = decrypts/encrypts x target files
all    = decrypts/encrypts all files in the folder

""")
        encrypt_setup()
    else:
        try:
            en_number = int(en_number)
        except:
            print("[-]Please enter a number")
            encrypt_setup()
        for i in range(en_number):
            en_file = input("[*]Enter a file: ")
            en_files.append(en_file)
        encrypt(en_path, en_files)

def decrypt_setup():
    global de_files
    de_path = input("decrypter>[*]Enter target path of the folder: ")
    if de_path == 'options' or de_path == 'show options':
        print("""
number = decrypts/encrypts x target files
all    = decrypts/encrypts all files in the folder

""")
        decrypt_setup()
    de_number = input("decrypter>[*]How many files do you want to decrypt? ")
    if de_number == 'all':
        decrypt_all(de_path)
    elif de_number == 'options' or de_number == 'show options':
        print("""
number = decrypts/encrypts x target files
all    = decrypts/encrypts all files in the folder

""")
        decrypt_setup()
    else:
        try:
            de_number = int(de_number)
        except:
            print("[-]Please enter a number")
            decrypt_setup()
        for i in range(de_number):
            de_file = input("[*]Enter a file: ")
            de_files.append(de_file)
        decrypt(de_path, de_files)

def main():
    menu = input("#fernet_cryptography$>")
    if menu == 'help' or menu == '--help' or menu == '-help' or menu == '-h':
        print("""
Opening help page...
help    = shows this help-page
encrypt = opens the encrypter
decrypt = opens the decrypter   
exit    = exits the programm
options = shows the options for en-/decryption

""")
        main()
    elif menu == 'encrypt' or menu == '-encrypt':
        encrypt_setup()
    elif menu == 'decrypt' or menu == '-decrypt':
        decrypt_setup()
    elif menu == 'exit' or menu == '-exit':
        print("[*]Exiting programm...")
        exit()
    else:
        print("\n[-]Command not found\n")
        main()

showbanner()
main()