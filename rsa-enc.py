#Hello everyone! Let's get this party started
import sys
import argparse

def getflags():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", dest = 'keyfile', help="Enter Key file", required = True)
    parser.add_argument("-i", dest = 'inputfile', help="Enter input file", required = True)
    parser.add_argument("-o", dest = 'outputfile', help= "Enter output file", required=True)
    args = parser.parse_args()

    print "Input file: ", args.inputfile
    print "Key file: ", args.keyfile
    print "Output file: ", args.outputfile

def main():
    getflags()

if __name__ == "__main__":
	main()
