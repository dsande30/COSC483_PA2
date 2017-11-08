#Hello everyone! Let's get this party started
import sys
import argparse

def getFlags():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest = 'keyFile', help="Enter Key file", required = True)
    parser.add_argument("-i", dest = 'inputFile', help="Enter input file", required = True)
    parser.add_argument("-o", dest = 'outputFile', help= "Enter output file", required=True)
    args = parser.parse_args()

    return args

def readKey(keyFile):
    print "Opening", keyFile


def main():
    args = getFlags()
    readKey(args.keyFile)

if __name__ == "__main__":
	main()
