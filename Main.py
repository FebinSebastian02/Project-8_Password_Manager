#imports are done
from cryptography.fernet import Fernet  #pip install cryptography -> To install cryptography package

# def generateKey():
#     key = Fernet.generate_key()
#     with open("Key.key", "wb") as keyFile:
#         keyFile.write(key)
def loadKey():
    keyFile = open("Key.key", "rb")
    #Another operations that can performed while opening a file are:-
    #rb -> To read in bytes
    #wb -> To write in bytes
    key = keyFile.read()
    keyFile.close() #Manually closing the opened file
    return key

key1 = loadKey()
fer = Fernet(key1)  #To initialize the encryption module
def viewPwd():
    file = open("Passwords.txt", "r")
    for i in file.readlines():
        line = i.rstrip()
    #rstrip() removes unwanted trailing characters. If there are no characters passed as arguments, it removes white spaces.
        userName, pswd = line.split("|")
        print("User Name:- " + userName + ", Password:- " + fer.decrypt(pswd.encode()).decode())
def addPwd():
     with open("Passwords.txt", "a") as file:
        #Here, with keyword is used to automatically close a file once the operations are performed.
        #Mainly 3 operations can be performed while opening a file,
        #a -> append (Create a new file if existing file is not present and add a new line/ Add a new line to existing file)
        #w -> overwrite (Overwrites the existing file with new changes)
        #r -> read (Read an existing file)
         userName = input("Enter a User name...")
         pwd = input("Enter a password...")
         file.write(userName + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
         #encode () -> To convert string to bytes
         #decode() -> To convert byte string to regular string

print("\n!!!Welcome to the Password Manager!!!")
while True:
    mas_pwd =input("\nEnter your Master Password...").lower()
    #Master password is p123
    if mas_pwd == "p123":
        #generateKey()
        while True:
            choice = int(input("\nSelect an option 1) add password 2) view password 3) quit..."))
            if choice == 1:
                addPwd()
            elif choice == 2:
                viewPwd()
            elif choice == 3:
                print("!!!Bye, see you soon!!! ")
                quit()
            else:
                print("Invalid option entered. Please enter a valid one...")
    else:
        print("Invalid Master Password entered. Please enter a valid one...")