def read(filename):
    lines = open(filename).readlines()
    tokens = " ".join(lines).split()

    mem = 1024 * [0]
    addr = 0
    for token in tokens:
        if token[0] == '@':
            addr = int(token[1:], 16)
        else:
            data = int(token, 16)
            mem[addr] = data
            addr += 1

    return mem


def save(mem, filename):

    file = open(filename, 'w')

    MAX = len(mem)
    N = 8

    addr = True
    for i in range(0, MAX, N):
        zero = True
        for j in range(N):
            if mem[i + j]:
                zero = False

        if not zero:
            if addr:
                print >> file, "@%04X" % i
                addr = False

            for j in range(N):
                print >> file, "%06X" % mem[i + j],
            print >> file
        else:
            addr = True

    file.close()

# mem = readmem( 'test0.mem' )
# print mem[0:10]
