import sys


def count_from_file(f):
    count = [0 for i in xrange(0,2**16)] # must be a better way
    lbyte = '\0'
    byte = f.read(1)
    while byte:
        # Do stuff with byte.
        value = ord(byte) + (ord(lbyte) << 8)
        count[value] += 1
        lbyte = byte
        byte = f.read(1)
    return count

print("filename,"+",".join([str(i) for i in xrange(0,2**16)]))

for filename in sys.argv[1:]:
    with open(filename, "rb") as f:
        count = count_from_file(f)
        cstring = ",".join([str(c) for c in count])
        print("\"%s\",%s" % (filename,cstring))
