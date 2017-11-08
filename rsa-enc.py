#Hello everyone! Let's get this party started
import sys
import argparse
from Crypto.Util import number

def getFlags():
    #parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest = 'keyFile', help="Enter Key file", required = True)
    parser.add_argument("-i", dest = 'inputFile', help="Enter input file", required = True)
    parser.add_argument("-o", dest = 'outputFile', help= "Enter output file", required=True)
    args = parser.parse_args()

    return args

def readKey(keyFile):
    print "Opening", keyFile

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

    print "P:", int(p)
    print "Q:", int(q)


def main():
    args = getFlags()
    readKey(args.keyFile)
    variableGenerator()

if __name__ == "__main__":
	main()
