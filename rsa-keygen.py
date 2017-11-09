import sys
import argparse

def getFlags():
    #parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest = 'publicFile', help="Enter public key file", required = True)
    parser.add_argument("-s", dest = 'secretFile', help="Enter private key file", required = True)
    parser.add_argument("-n", dest = 'numBitsFile', help= "Enter num of bits file", required=True)
    args = parser.parse_args()

    return args

def main():
    args = getFlags()

if __name__ == "__main__":
	main()
