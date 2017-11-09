#Hello everyone! Let's get this party started
import sys
import argparse
from Crypto.Util import number
import fractions

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
    numBits = keyFile.readline()
    N = keyFile.readline()
    e = keyFile.readline()
    key.close()
    contents += numBits + N + e
    return contents

def readMessage(inputFile):
    f = open(inputFile, 'r')
    m = f.readline()
    print "m: %s\n" % m
    f.close()


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
    print("Length of r: ", len(r))
    if len(message) < (r-24):
        message += 0 * ((r-24)-len(message))
    print("Message: ", message)
    print("Message Length: ", len(message))
    test = 0
    while test == 0:
        test = 1
        randBits = str(random.getrandbits(r))
        bitBlocks = []
        check = randBits[:]
        while len(check) > 0:
            slicelen = min(len(randbits), 8)
            bitBlocks.append(check[0:slicelen])
            check = check[slicelen:]
        print("randBits: ", randBits)
        print("Length of randBits: ", len(randBits))
        print("bitBlocks: ", bitBlocks)
        print("bitBlocks Length: ", len(bitBlocks))
        for n in bitBlocks:
            if n == b'x\00':
                test = 0
    paddedM += randBits + b'\x00' + message

def main():
    args = getFlags()
    readKey(args.keyFile)
    readMessage(args.inputFile)
    variableGenerator()

if __name__ == "__main__":
	main()
