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

def: variableGenerator(N):
    #to make p and q
    p = 0
    q = 0
    while(p == q):
        p = number.getStrongPrime(N/2)
        q = number.getStrongPrime(N/2)
        if len(str(p)) != len(str(q)):
            p = int(p)
            q = int(q)
            p = 0
            q = 0
    print "P: %d\n" % p
    print "Q: %d\n" % q

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
    test = 0
    while test == 0:
        test = 1
        randBits = str(random.getrandbits(r))
        for n in randBits:
            if n == b'x\00':
                test = 0
    randBits = str(random.getrandbits(r))
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
