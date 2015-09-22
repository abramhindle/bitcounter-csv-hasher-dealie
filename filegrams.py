import sys
import os
import logging
logging.basicConfig(level=logging.DEBUG)

bits = 12 # can set to 16
mask = 0xff >> (16 - bits)

def count_from_file(f):
    count = [0] * 2**bits
    lbyte = '\0'
    bytes = f.read()
    for i in xrange(0,len(bytes)):
        byte = bytes[i]
        # Do stuff with byte.
        value = ord(byte) | ((ord(lbyte) & mask) << 8)
        count[value] += 1
        lbyte = byte
    return count

print("filename,"+",".join([str(i) for i in xrange(0,2**bits)]))


dirs = ["."]

if len(sys.argv) > 1:
    dirs = sys.argv[1:]

for directory in dirs:
    for dirName, subdirList, fileList in os.walk(directory):
        logging.info('Found directory: %s' % dirName)
        for fname in fileList:
            logging.info('\t%s' % fname)
            try:
                filename = "%s/%s" % (dirName, fname)
                with open(filename, "rb") as f:
                    count = count_from_file(f)
                    cstring = ",".join([str(c) for c in count])
                    print("\"%s\",%s" % (fname,cstring))
            except IOError as e:
                logging.warn(e)


