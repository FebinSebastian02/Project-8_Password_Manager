#imports are done
from Options import *

print("\n!!!Welcome to the Password Manager!!!")
mas_pwd = input("\nEnter your Master Password...")
while True:
    choice = int(input("\nSelect an option 1) Add password 2) View password 3) Quit..."))
    if choice == 1:
        addPwd()
    elif choice == 2:
        viewPwd()
    elif choice == 3:
        print("\n!!!Bye, see you soon!!!")
        quit()
    else:
        print("\nInvalid option entered. Enter a valid option...")