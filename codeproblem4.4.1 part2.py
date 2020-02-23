#Problem 4.4.1 part 2:

read_file = "test_data.csv"

def saveUserInfo(username, value, password):
    usernameFile = open("Username.txt", "w")
    accountValueFile = open("AccountValue.txt", "w")
    passwordFile = open("Password.txt", "w")
    usernameFile.write(username)
    print(value, file=accountValueFile)
    passwordFile.write(password)
    usernameFile.close()
    accountValueFile.close()
    passwordFile.close()

saveUserInfo("RamblinWreck20", 222, "burd311")

#So the following answers do work: 
# - accountValueFile.write(str(value))
# - saveUserInfo("RamblinWreck20", str(222), "burd311")
# - print(value, file=accountValueFile)
