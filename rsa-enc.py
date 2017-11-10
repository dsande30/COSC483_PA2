#Hello everyone! Let's get this party started
import sys
import argparse
from Crypto.Util import number
from Crypto.Random import random
import fractions
import binascii

def getFlags():
    #parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest = 'keyFile', help="Enter Key file", required = True)
    parser.add_argument("-i", dest = 'inputFile', help="Enter input file", required = True)
    parser.add_argument("-o", dest = 'outputFile', help= "Enter output file", required=True)
    args = parser.parse_args()
    return args

def Encrypt(m, contents):
    print "M: %d" % m
    print "N: %d" % contents[1]
    print "e: %d" % contents[2]
    return pow(m, contents[2], contents[1])
    #return ((m**contents[2]) % contents[1])

#NOTE: This will change with proper message
def writeOutput(outputFile, paddedM):
    o = open(outputFile, 'wb')
    #o.write("".join(paddedM))
    o.write(str(paddedM))
    o.close()


def readKey(keyFile):
    key = open(keyFile, 'rb')
    numBits = key.readline()
    N = key.readline()
    e = key.readline()
    key.close()
    numBits = numBits.strip()
    N = N.strip()
    e = e.strip()
    return int(numBits), int(N), int(e)

def readInput(inputFile):
    i = open(inputFile, 'rb')
    m = i.readline()
    i.close()
    m = str(m)
    return m

def pad(message, r):
    print "Bear with me Schuchard"
    M = ""
    M += ord(b'\x00') + ord(b'\x02')
    test = 0
    while test == 0:
        test = 1
        rand = random.getrandbits(r)
        rand = str(rand)
        randlength = 0
        for i in range(0, len(rand)):
            if rand[i] == '0':
                test = 0
            randlength += int(rand[i]).bit_length()
        if randlength != r:
            test = 0
    print "Rand: %s" % rand
    print randlength
    M += rand + str(ord(b'\x00'))
    message = message.strip()
    print "Message before pad: %s" % message
    messageLen = 0
    padCount = 0
    for i in range(0, len(message)):
        messageLen += int(message[i]).bit_length()
        if message[i] == "0":
            messageLen += 1
    for n in range(0, len(message)):
        message = message + "0"*((r - 24) - messageLen)
        #messageLen += (r - 24) - messageLen
    print "Message after pad: %s" % message
    print "messageLen: %d" % messageLen
    M += message
    print "What's M: %s" % M
    bitLength = 0
    for i in range(0, len(M)):
        bitLength += int(M[i]).bit_length()
        if M[i] == "0":
            bitLength += 1
    print "bitLength: %d" % bitLength
    return int(M)



def main():
    args = getFlags()
    contents = readKey(args.keyFile)
    message = readInput(args.inputFile)
    paddedM = pad(message, int(contents[0]) / 2)
    c = Encrypt(paddedM, contents)
    writeOutput(args.outputFile, c)

if __name__ == "__main__":
	main()
