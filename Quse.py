#! /usr/bin/env python3 

# modules 
import os, sys
import subprocess
import random
import pyaes, pbkdf2, binascii, secrets
import pyAesCrypt
from cryptography.fernet import Fernet
from os import stat, remove 
bufferSize = 64 * 1024 
password = "kmx404isthebest"
#pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize) 
#pyAesCrypt.decryptFile("data.txt", "data.txt.aes", password, bufferSize) 

# hash related
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

# in order to make this tool dynamic there's a commented parts made to be a place of evolving.
# banner
banner = """
     QQQQQQQQQ                                                            
   QQ:::::::::QQ                                                          
 QQ:::::::::::::QQ                                                        
Q:::::::QQQ:::::::Q                                                       
Q::::::O   Q::::::Quuuuuu    uuuuuu      ssssssssss       eeeeeeeeeeee    
Q:::::O     Q:::::Qu::::u    u::::u    ss::::::::::s    ee::::::::::::ee  
Q:::::O     Q:::::Qu::::u    u::::u  ss:::::::::::::s  e::::::eeeee:::::ee
Q:::::O     Q:::::Qu::::u    u::::u  s::::::ssss:::::se::::::e     e:::::e
Q:::::O     Q:::::Qu::::u    u::::u   s:::::s  ssssss e:::::::eeeee::::::e
Q:::::O     Q:::::Qu::::u    u::::u     s::::::s      e:::::::::::::::::e 
Q:::::O  QQQQ:::::Qu::::u    u::::u        s::::::s   e::::::eeeeeeeeeee  
Q::::::O Q::::::::Qu:::::uuuu:::::u  ssssss   s:::::s e:::::::e           
Q:::::::QQ::::::::Qu:::::::::::::::uus:::::ssss::::::se::::::::e          
 QQ::::::::::::::Q  u:::::::::::::::us::::::::::::::s  e::::::::eeeeeeee  
   QQ:::::::::::Q    uu::::::::uu:::u s:::::::::::ss    ee:::::::::::::e  
     QQQQQQQQ::::QQ    uuuuuuuu  uuuu  sssssssssss        eeeeeeeeeeeeee  
             Q:::::Q                                                      
              QQQQQQ                                                      
                                                                     BY: @KMx404
// Behold, Some of this tool's option is made to edit your files.
// So make sure you have full access and know what to do.  """

def st_dsp():
    print("Choose the type of Encryption You want to Use!:") 
    print("1- AES") 
    print("2- RSA")
    print("3- TripleDES")
 
def aes_q() :
    print("You want to encrypt, decrypt with AES?") 
    print("A- Encrypt") 
    print("B- Decrypt") 
# AES decrypting 
class AES: 
    bufferSize = 64 * 1024 
    # change the password
    password = "kmx404isthebest" 

    """
    def __init__(self): 
        pass 
    def generateKey(self): 
        key = ''.join(chr(random.randint(0,100)) for i in range(16))
        fd = open("AES_key.pem", "wb") 
        fd.write(bytes(str(key), 'utf-8'))
        fd.close()
        return bytes(str(key), 'utf-8') 
        """
    # AES encrypt 
    def eAES(): 
        # its needs an update though, ths imported modules gotta be updated
        """
        obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV256')
        path = input("type the file path: ") 
        dfile = obj.encrypt(path) 
        with open(str(path), "rb") as fIn: 
            with open(str(path)+".aes", "wb") as fOut: 
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize) 
        """
        path = input("Path of the File you want to encrypt: ") 
        pyAesCrypt.encryptFile(str(path), "dataout.txt.aes", password, bufferSize) 


    # AES decrypt
    def dAES(): 
       # These deep features are gonna be contained in the next version! Since I'm aiming for the basics right now!
        """
        with open(str(path)+".aes", "rb") as fIn: 
            try: 
                with open ("dataout.txt", "wb")  as fOut: 
                    pyAesCrypt.decryptStream(fIn, fOut, password, buffersize, encFileSize) 
            except ValueError: 
                remove("dataout.txt") 
        """
        poth = input("path of the encrypted File: ") 
        pyAesCrypt.decryptFile(str(poth), "dataout.txt", password, bufferSize) 
# root check 
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "[sudo] password for %u to continue:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

if __name__=='__main__':
    try:
        print(banner)
        if prompt_sudo() != 0: 
            print("You need SUDO for this!")
            exit() 
        st_dsp() 
        answer = input("$  ") 
        if int(answer) == 1: 
            aes_q()
            so = input("$  ") 
            if so == 'A': 
               AES.eAES() 
               print("Your file has been encrypted!") 
               p = input("Where do you want to save your file?") 
               os.system('mv dataout.txt.aes' + ' ' + str(p))  
               os.system('rm -rf' + str(path)) 
           else: 
               AES.dAES() 
               print("Your file has been decrypted!") 
        elif int(answer) == 2: 
        # This one to be edited.  
            pass
    except: 
        print("Theres an Error! Check the path && Unvalid inputs!") 
