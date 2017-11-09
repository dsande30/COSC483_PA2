import sys
import argparse

def getFlags():
    #parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest = 'publicFile', help="Enter public key file", required = True)
    parser.add_argument("-s", dest = 'secretFile', help="Enter private key file", required = True)
    parser.add_argument("-n", dest = 'numBits', type=int, help= "Enter num of bits file", required=True)
    args = parser.parse_args()

    return args

def writeFiles(args):
    pub = open(args.publicFile, 'w')
    priv = open(args.secretFile, 'w')

    #We don't have N yet so this will be weird
    pub.write("%d\n" % args.numBits)
    #pub.write("%d" % N)
    pub.write("We don't have N yet\n")
    #pub.write("%d" % d)
    pub.write("We don't have d yet\n")

    #We don't have N yet so this will be weird
    priv.write("%d\n" % args.numBits)
    #pub.write("%d" % N)
    priv.write("We don't have N yet\n")
    #pub.write("%d" % d)
    priv.write("We don't have e yet\n")

    '''
    print "Bits: %d" % int(Nbits)
    print "N: %d" % int(N)
    print "e: %d" % int(e)
    print "d: %d" % int(d)
    '''

    #close files
    pub.close()
    priv.close()

def main():
    args = getFlags()
    writeFiles(args)

    print "Public key file:", args.publicFile
    print "Private key file:", args.secretFile
    print "Number of bits file:", args.numBits

if __name__ == "__main__":
	main()
