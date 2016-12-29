#!/usr/bin/env python
from random import SystemRandom
import sys, os
import subprocess

# get a secure source of random numbers
cryptogen = SystemRandom()


if  len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help"):
    print ("Usage:")
    print ("./dice.py 7 15")
    print (" length --^  ^-- number of passwords (defaults to 1)")
    exit()

# check if we have a length argument...
if len(sys.argv) >= 2:
    try:
        passwdLength = int(sys.argv[1])
    except(ValueError):
        print ("Can't convet '" + sys.argv[1] + "' to integer")
        exit()
else:
    passwdLength = 8

# check if we have password number argument
if (len(sys.argv) >= 3):
    try:
        numPasswd = int(sys.argv[2])
    except(ValueError):
        print ("Can't convert '" + sys.argv[2] + "' to integer")
else:
    numPasswd = 1

# use GPG to verify the file
if not os.path.isfile("../diceware-v6.txt") and os.path.isfile("../diceware-v6.txt.asc"):
    print ("Verifying the diceware file using GPG")
    print ()
    print (subprocess.call(["gpg", "-v", "../diceware-v6.txt.asc"]))
    print ()

# generate the password
def genPasswd(length):
    password = []
    positions = [ cryptogen.randint(0,46655) for i in range(length)] # get random positions in file 0-46655
    for pos in positions: # look up the positions in the diceware file
        with open("../diceware-v6.txt") as fp:
            for i, line in enumerate(fp):
                if i== pos:
                    password.append(line[8:-1])

    return " ".join(password) # print the final password joined by spaces


for i in range(numPasswd):
    print (genPasswd(passwdLength))
