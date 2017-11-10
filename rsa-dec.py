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
    numBits = key.readline()
    numBits = numBits.strip()
    N = key.readline()
    N = N.strip()
    d = key.readline()
    d = d.strip()
    key.close()
    return numBits, N, d

def readInput(inputFile):
    inp = open(inputFile, 'rb')
    c = inp.readline()
    c = c.strip()
    return c

def Dec(key, c):
    c = int(c)
    d = int(key[2])
    N = int(key[1])
    print "C: %d" % c
    print "N: %d" % N
    print "d: %d" % d
    m = pow(c, d, N)
    return m

def writeOutput(outputFile, m):
    out = open(outputFile, 'wb')
    out.write("%d" %m)
    out.close()

def unpad(m):
    pad, r, M = m.split("0")
    M = M.strip()
    return M

def main():
    args = getFlags()
    key = readKey(args.keyFile)
    c = readInput(args.inputFile)
    m = Dec(key, c)
    m = unpad(str(m))
    print m
    m = int(m)
    writeOutput(args.outputFile, m)

if __name__ == "__main__":
	main()
