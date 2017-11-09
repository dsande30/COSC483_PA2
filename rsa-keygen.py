import sys
import argparse
from Crypto.Util import number
import fractions


def getFlags():
    #parse command line args
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest = 'publicFile', help="Enter public key file", required = True)
    parser.add_argument("-s", dest = 'secretFile', help="Enter private key file", required = True)
    parser.add_argument("-n", dest = 'numBits', type=int, help= "Enter num of bits file", required=True)
    args = parser.parse_args()

    return args

def variableGenerator(numBits):

    #to make p and q
    numBits = numBits
    print "N: %d\n" % numBits
    p = 0
    q = 0
    l = (numBits / 2)
    print "L: %d\n" % l
    while(p ==0 and q == 0):
        p = number.getPrime(l)
        q = number.getPrime(l)
        print "p",sys.getsizeof(p)
        print "q",sys.getsizeof(q)
        if len(str(p)) != len(str(q)):
            p = int(p)
            q = int(q)
            p = 0
            q = 0
    print "Len P: %d" % len(str(p))
    print "Len Q: %d" % len(str(q))
    print "Len N: %d" % len(str(int(p) * int(q)))
    print "P: %d\n" % int(p)
    print "Q: %d\n" % int(q)

    p = int(p)
    q = int(q)

    N = p * q
    order = (p-1)*(q-1)

    print "N: %d\n" % N
    print "Order: %d\n" % order

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
    variableGenerator(args.numBits)

if __name__ == "__main__":
	main()
