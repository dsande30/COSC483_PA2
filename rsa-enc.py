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
    i = open(inputFile, 'r')
    m = i.readline()
    i.close()
    return m





def pad(message, r):
    M = b'\x00' + b'\x02'

    print "Seed:", random.seed()

    #ensure always 20 bits
    randBits = 0
    while randBits.bit_length() != 20:
        randBits = random.getrandbits(r)

    #need direct copy of bits
    #check = randBits.bit_length()

    #seperate into chunks
    bitBlocks = []

    check = hex(randBits)

    print "Check Hex stuff: %s" % check.strip('L')

    """
    while len(check) > 0:
        slicelen = min(len(check), 8)
        bitBlocks.append(check[0:slicelen])
        check = check[slicelen:]
    """

    for n in bitBlocks:
        if n == b'\x00':
            while n == b'\x00':
                n = random.getrandbits(8)

    x = random.getrandbits(8)
    print "X: %s" % str(x).encode('hex')

'''
def pad(message, r):
    paddedM = b'\x00' + b'\x02'
    print("r: ", r)
    #print("Length of r: ", len(r))
    message = message.strip()
    if len(message) < (r-24):
        message += "0" * ((r-24)-len(message))
    print("Message: %s" % message)
    #print("Message Length: ", len(message))
    #test = 0
    #while test == 0:
    test = 1
    randBits = random.getrandbits(r)
    print "randBits before encoding: %s" % randBits
    #randBits = randBits.encode('utf-8')
    #print "randBits after encoding: %s" % randBits
    bitBlocks = []
    check = str(randBits)[:]
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
            while n == b'\x00':
                n = str(random.getrandbits(8))
            #test = 0
    #randBits = binascii.hexlify(randBits)
    print("Hex randBits: 0x%s" % randBits)
    paddedM += format(int(randBits), '02x') + b'\x00' + binascii.hexlify(message)
    return paddedM
'''

def main():
    args = getFlags()
    contents = readKey(args.keyFile)
    message = readInput(args.inputFile)
    #paddedM = pad(message, int(contents[0]) / 2) #NOTE:Doesn't work

    #NOTE: Arbitrary padded message for now
    paddedM = 666999420
    c = Encrypt(paddedM, contents)
    writeOutput(args.outputFile, c)

if __name__ == "__main__":
	main()
