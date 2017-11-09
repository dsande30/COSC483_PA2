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

def variableGenerator(N):
    #to make p and q

    print "N: %d\n" % N
    p = 0
    q = 0
    while(p == q):
        p = number.getPrime(N/2)
        q = number.getPrime(N/2)
        if len(str(p)) != len(str(q)):
            p = int(p)
            q = int(q)
            p = 0
            q = 0
    print "P: %d\n" % p
    print "Q: %d\n" % q

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

def pad(message, r):
    paddedM = b'\x00' + b'\x02'
    print("r: ", r)
    print("Length of r: ", len(r))
    test = 0
    while test == 0:
        test = 1
        randBits = str(random.getrandbits(r))
        print("randBits: ", randBits)
        print("Length of randBits: ", len(randBits))
        for n in randBits:
            if n == b'x\00':
                test = 0
    paddedM += randBits + b'\x00' + message


def main():
    args = getFlags()
    writeFiles(args)
    variableGenerator(args.numBits)


    print "Public key file:", args.publicFile
    print "Private key file:", args.secretFile
    print "Number of bits file:", args.numBits

if __name__ == "__main__":
	main()
