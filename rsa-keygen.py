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
    print "N: %d" % numBits
    p = 0
    q = 0
    l = (numBits / 2)
    print "L: %d" % l
    while(p ==0 and q == 0):
        p = number.getPrime(l)
        q = number.getPrime(l)
        print "p bitlength %d" % p.bit_length()
        print "q bitlength %d" % q.bit_length()
        #confirm lengths are the same, not the values
        if p.bit_length() != q.bit_length() or p == q:
            p = 0
            q = 0
    print "P: %d" % int(p)
    print "Q: %d" % int(q)

    p = int(p)
    q = int(q)

    N = p * q
    order = (p-1)*(q-1)

    print "N: %d" % N
    print "Order: %d" % order

    #calculate e: coprime to order
    #NOTE: I am not confident this works.
    ePrimes = [3,5,7,17,257, 65537]
    booly = 0
    for x in ePrimes:
        if(fractions.gcd(order, x) == 1):
            booly = 1
            print "e: %d" % x
            e = x
            break
    if booly == 0:
        sys.exit("No coprime")

    #d is inverse of e mod order
    d = number.inverse(e, order)
    print "d: %d" % d


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
