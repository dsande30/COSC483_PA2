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
    #print "N: %d" % numBits
    p = 0
    q = 0
    l = (numBits / 2)
    #print "L: %d" % l
    while(p ==0 and q == 0):
        p = number.getPrime(l)
        q = number.getPrime(l)
        #print "p bitlength %d" % p.bit_length()
        #print "q bitlength %d" % q.bit_length()
        #confirm lengths are the same, not the values
        if p.bit_length() != q.bit_length() or p == q:
            p = 0
            q = 0
    #print "P: %d" % int(p)
    #print "Q: %d" % int(q)

    p = int(p)
    q = int(q)

    N = p * q
    order = (p-1)*(q-1)

    #print "N: %d" % N
    #print "Order: %d" % order

    #calculate e: coprime to order
    #NOTE: I am not confident this works.
    ePrimes = [3,5,7,17,257, 65537]
    booly = 0
    for x in ePrimes:
        if(fractions.gcd(order, x) == 1):
            booly = 1
            #print "e: %d" % x
            e = x
            break
    if booly == 0:
        sys.exit("No coprime")

    #d is inverse of e mod order
    d = number.inverse(e, order)
    #print "d: %d" % d

    '''
    #prelim testing
    c = (107 ** e) % N
    print "%d" % c
    newm = (c ** d) % N
    print "%d" % newm
    '''

    return N, d, e

def writeFiles(args, keys):
    pub = open(args.publicFile, 'w')
    priv = open(args.secretFile, 'w')

    #Write public key
    pub.write("%d\n" % args.numBits)
    pub.write("%d\n" % keys[0])
    pub.write("%d\n" % keys[2])

    #Write private key
    priv.write("%d\n" % args.numBits)
    priv.write("%d\n" % keys[0])
    priv.write("%d\n" % keys[1])

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
    keys = variableGenerator(args.numBits)
    print "N: %d" %keys[0]
    print "d: %d" %keys[1]
    print "e: %d" %keys[2]
    writeFiles(args, keys)

if __name__ == "__main__":
	main()
