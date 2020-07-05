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
pyAesCrypt.encryptFile("data.txt", "data.txt.aes", password, bufferSize) 
pyAesCrypt.decryptFile("data.txt", "data.txt.aes", password, bufferSize) 

# hash related
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

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
                                                                     BY: @KMx404"""
def st_dsp():
    print("Choose the type of Encryption You want to Use!:") 
    print("1- AES") 
    print("2- RSA")
    print("3- TripleDES")
 
def aes_q() :
    an = input("You want to decrypt, encrypt with AES?\n") 
   
# AES decrypting 
class AES: 
    def __init__(self): 
        pass 
    
    # AES encrypt 
    def eAES(): 
        obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV256')
        path = input("type the file path: ") 
        dfile = obj.encrypt(path) 
        with open(str(path), "rb") as fIn: 
            with open(str(path)+".aes", "wb") as fOut: 
                pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize) 
    # AES decrypt
    def dAES(): 
        with open(str(path)+".aes", "rb") as fIn: 
            try: 
                with open ("dataout.txt", "wb")  as fOut: 
                    pyAesCrypt.decryptStream(fIn, fOut, password, buffersize, encFileSize) 
            except ValueError: 
                remove("dataout.txt") 

# root check 
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "[sudo] password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

if __name__=='__main__':
    print(banner)
    prompt_sudo() 
    if prompt_sudo() != 0: 
        print("You need SUDO for this!")
        exit() 
    st_dsp() 
    answer = input("$  ") 
    if int(answer) == 1: 
        aes_q()
        if int(aes_a) == 1: 
            AES.eAES() 
        else: 
            AES.dAES() 
    elif int(answer) == 2: 
        # This one to be edited.  
        pass
