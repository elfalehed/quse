#! /usr/bin/env python3 

# modules 
import os, sys
import subprocess
import random
from cryptography.fernet import Fernet 
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
 

def dAES(): 
    obj = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV256')


# root check 
def prompt_sudo():
    ret = 0
    if os.geteuid() != 0:
        msg = "[sudo] password for %u:"
        ret = subprocess.check_call("sudo -v -p '%s'" % msg, shell=True)
    return ret

def main(): 
    print(banner)
    prompt_sudo() 
    if prompt_sudo() != 0: 
        print("You need SUDO for this!")
        exit() 
    st_dsp() 
if __name__=='__main__':main()
