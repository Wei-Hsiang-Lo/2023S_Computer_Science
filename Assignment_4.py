#I write this program by myself. Sign here:羅瑋翔
#Email adress: xianglo9121.mg10@nycu.edu.tw
#Anything specail? I write this program which satisfied all target.
#Iprovide additional functions: None
def remove(aString,i):
    return aString[:i]+aString[i+1:]

def beforeLastGen(aString, i):
    return aString[:i]

def afterLastGen(aString, i):
    return aString[i+1:]
    
def keyGen(password):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    for i in range(len(password)-1):
        for j in range(i+1, len(password)):
            if password[i] == password[j]:
                remove(password, j)
    lastLetterOfPassword = password[len(password)-1]
    ind = alphabet.find(lastLetterOfPassword)
    beforeLast = beforeLastGen(alphabet, ind)
    afterLast = afterLastGen(alphabet, ind)
    for ch in password:
        i = beforeLast.find(ch)
        j = afterLast.find(ch)
        if i != -1:
            beforeLast = remove(beforeLast, i)
        if j != -1:
            afterLast = remove(afterLast, j)
    return password + afterLast + beforeLast

def encrypt(plainText,key):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '
    cipherText = ""
    for ch in plainText:
        i = alphabet.find(ch)
        cipherText = cipherText + key[i]
    return cipherText

def decrypt(cipherText, key):
    from string import ascii_lowercase
    decryptionMess = ""
    alphabet = ascii_lowercase + ' '
    for ch in cipherText:
        i = key.find(ch)
        decryptionMess = decryptionMess + alphabet[i]
    return decryptionMess

condition = True
while condition == True:
    password = input("Enter password : ")
    key = keyGen(password)
    plainText = input("Please enter a message that you want to encrypt : ")
    cipherText = encrypt(plainText,key)
    print("The cipherText is :", cipherText)
    decryptionMess = decrypt(cipherText, key)
    print("The message after decrypt is :",decryptionMess)
    answer = input("Do you want to do it again(y for yes, n for no) : ")
    if answer != 'y' and answer != 'Y':
        condition = False
