import sys

def copy(in_file, out_file):
    CHUNK_SIZE = 1024
    with open(in_file, 'rb') as fi:
        with open(out_file, 'wb') as fo:
            while True:
                data = fi.read(CHUNK_SIZE)
                if not data:
                    break
                fo.write(data)
try:
    print("input file: " + sys.argv[1])
    print("output file: " + sys.argv[2])
    copy(sys.argv[1], sys.argv[2])
except:
    print("exception occurred")
