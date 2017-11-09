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
    key = open(keyFile, 'rb')
    N = key.readline()
    key.close()

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

def main():
    args = getFlags()
    readKey(args.keyFile)
    readMessage(args.inputFile)
    variableGenerator()

if __name__ == "__main__":
	main()
