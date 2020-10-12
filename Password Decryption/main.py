from decryption import  decryptPassword
if __name__ == "__main__":
    # Test case 1
    encryptedPassword = "pTo*Ta*O"
    decryptedPassword = decryptPassword(encryptedPassword)
    print(decryptedPassword)
    # Test case 2
    encryptedPassword = "51Pa*0Lp*0e"
    decryptedPassword = decryptPassword(encryptedPassword)
    print(decryptedPassword)
