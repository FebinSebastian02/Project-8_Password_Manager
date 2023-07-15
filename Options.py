
def addPwd():
    with open("Password.txt", "a") as file:
        userName = input("Enter a User name...")
        pwd = input("Enter a password...")
        file.write("\nUser Name:- {}".format(userName) + ", " + "Password:- {}\n".format(pwd))
# 3 types of modes for open():- a) append "a" b) write "w" c) read "r"
# append mode appends a new password to an existing file or it creates a new file if there's none existing and then appends
# write mode completely overwrites an existing file with new details
# read mode is used to just read the existing file
# Here, with keyword is used to automatically close the file once it's opened and some operations are done. If file is not
# closed, it may cause some issue later.

def viewPwd():
    file = open("Password.txt", "r")
    for i in file.readlines():  #readlines() is an inbuilt function
        print(i.rstrip())   #rstrip() is an inbuilt() used to remove the trailing characters. If no character is passed as
        #argument, then it removes the trailing white spaces. Therefore,unwanted line space in console were removed.
    file.close()    #close() manually closes the opened file.