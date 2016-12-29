#!/usr/bin/env python
import sys
import math

if (len(sys.argv) <= 1):
    print ("Provide the length of the password")
    exit()
#... and try to parse it

if  len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help"):
    print ("Usage:")
    print ("./analyze.py 7")
    print ("             ^-- password length to analyze")
    exit()

# check if we have a length argument...
if len(sys.argv) == 2:
    try:
        passwdLength = int(sys.argv[1])
    except(ValueError):
        print ("Can't convet '" + sys.argv[1] + "' to integer")
        exit()


print ("A diceware password with " + str(passwdLength) + " words has a total of")
print (str((6 ** 6) ** passwdLength) + " different combinations")
print ("This is equivalent to " + str((math.log((6 ** 6) ** passwdLength,2))) + "bits")
