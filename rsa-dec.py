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
    d = keyFile.readline()
    key.close()
    contents += numBits + N + d
    return contents


def main():
    args = getFlags()
    readKey(args.keyFile)
    variableGenerator()

if __name__ == "__main__":
	main()
