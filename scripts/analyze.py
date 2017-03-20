#!/usr/bin/env python
import sys
import math

if (len(sys.argv) <= 1):
    print("Provide the length of the password")
    exit()
# ... and try to parse it

if len(sys.argv) == 2 and \
   (sys.argv[1] == "-h" or sys.argv[1] == "--help" or sys.argv[1] == "help"):
    print("Usage:")
    print("./analyze.py 7")
    print("             ^-- password length to analyze")
    exit()

# check if we have a length argument...
if len(sys.argv) == 2:
    try:
        passwdLength = int(sys.argv[1])
    except(ValueError):
        print("Can't convet '" + sys.argv[1] + "' to integer")
        exit()


def bitsEqivalent(length):
    return math.log((6 ** 6) ** length, 2)


def combinations(length):
    return (6 ** 6) ** passwdLength


def guessTime(length, guessRate):
    comb = combinations(length)
    return comb/guessRate


def saneTime(time):
    if(time < 60):
        return str(time) + " seconds"
    elif(time < 3600):
        return str(time/60) + " minutes"
    elif(time < 86400):
        return str(time/3600) + " hours"
    elif(time < 31536000):
        return str(time/86400) + " days"
    elif(time < 3153600000):
        return str(time/31536000) + " years"
    elif(time < 31536000000):
        return str(time/3153600000) + " centuries"
    else:
        return str(time/31536000000) + " millennia"


print("A diceware password with " +
      str(passwdLength) + " words has a total of")
print(str(combinations(passwdLength)) + " different combinations")
print("This is equivalent to " +
      str(bitsEqivalent(passwdLength)) + "bits")
print("It would take an attacker the following time to crack the password brute force:")
print("Slow attacker at 100 hash/s: \t" + saneTime(guessTime(passwdLength, 100)))
print("Faster attacker at 10k hash/s: \t" + saneTime(guessTime(passwdLength, 10000)))
print("Faster attacker at 1M hash/s: \t" + saneTime(guessTime(passwdLength, 1000000)))
print("Faster attacker at 1B hash/s: \t" + saneTime(guessTime(passwdLength, 1000000000)))
print("Faster attacker at 10B hash/s: \t" + saneTime(guessTime(passwdLength, 10000000000)))
print("NSA at 1T hash/s: \t" + saneTime(guessTime(passwdLength, 1000000000000)))
print("GOD at 1 Google hash/s: \t" + saneTime(guessTime(passwdLength, 1e100)))
