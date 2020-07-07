#! /usr/bin/env python3 
"""
import pyAesCrypt
from os import stat, remove
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"

# encrypt
with open("data.txt", "rb") as fIn:
    with open("data.txt.aes", "wb") as fOut:
        pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)

# get encrypted file size
encFileSize = stat("data.txt.aes").st_size

# decrypt
with open("data.txt.aes", "rb") as fIn:
    try:
        with open("dataout.txt", "wb") as fOut:
            # decrypt file stream
            pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
    except ValueError:
        remove("dataout.txt") 
        """

import pyAesCrypt
# encryption/decryption buffer size - 64K
bufferSize = 64 * 1024
password = "foopassword"
path = input("enter a path: ") 
# encrypt
#pyAesCrypt.encryptFile(str(path), "data.txt.aes", password, bufferSize)
# decrypt
pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)



