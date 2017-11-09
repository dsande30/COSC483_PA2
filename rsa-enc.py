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

def readKey(keyFile):
    contents = []
    key = open(keyFile, 'rb')
    numBits = key.readline()
    #print "NumBits after read: %s" %numBits
    N = key.readline()
    e = key.readline()
    key.close()
    numBits = numBits.strip()
    N = N.strip()
    e = e.strip()
    contents.append(int(numBits))
    contents.append(int(N))
    contents.append(int(e))
    #print contents
    return contents

def readInput(inputFile):
    i = open(inputFile, 'r')
    m = i.readline()
    i.close()
    return m

def variableGenerator():
    #to make p and q
    p = 0
    q = 0
    while(p == q):
        p = number.getStrongPrime(512)
        q = number.getStrongPrime(512)
        if len(str(p)) != len(str(q)):
            p = int(p)
            q = int(q)
            p = 0
            q = 0

    N = p * q
    order = (p-1)*(q-1)

    #calculate e: coprime to order
    #NOTE: I am not confident this works.
    ePrimes = [3,5,7,17,257, 65537]
    booly = 0
    for x in ePrimes:
        if(fractions.gcd(order, x) == 1):
            booly = 1
            print "e =", x
            e = x
            break
    if booly == 0:
        sys.exit("No coprime")
        e = -1

    #d is inverse of e mod order
    d = number.inverse(e, order)

def pad(message, r):
    paddedM = b'\x00' + b'\x02'
    print("r: ", r)
    #print("Length of r: ", len(r))
    message = message.strip()
    if len(message) < (r-24):
        message += "0" * ((r-24)-len(message))
    print("Message: %s" % message)
    #print("Message Length: ", len(message))
    test = 0
    while test == 0:
        test = 1
        randBits = str(random.getrandbits(r))
        print "randBits before encoding: %s" % randBits
        randBits = randBits.encode('utf-8')
        print "randBits after encoding: %s" % randBits
        bitBlocks = []
        check = randBits[:]
        while len(check) > 0:
            slicelen = min(len(check), 8)
            bitBlocks.append(check[0:slicelen])
            check = check[slicelen:]
        #print("randBits: %s" % randBits)
        #print("Length of randBits: ", len(randBits))
        print("bitBlocks: ", bitBlocks)
        #print("bitBlocks Length: ", len(bitBlocks))
        for n in bitBlocks:
            if n == b'\x00':
                test = 0
    #randBits = binascii.hexlify(randBits)
    print("Hex randBits: 0x%s" % randBits)
    paddedM += format(int(randBits), '02x') + b'\x00' + binascii.hexlify(message)
    return paddedM

def main():
    args = getFlags()
    contents = readKey(args.keyFile)
    variableGenerator()
    message = readInput(args.inputFile)
    #print("N: ", contents[1])
    print("numBits: ", contents[0])
    #print(contents)
    paddedM = pad(message, int(contents[0]) / 2)
    print("paddedM: ", paddedM)


if __name__ == "__main__":
	main()
