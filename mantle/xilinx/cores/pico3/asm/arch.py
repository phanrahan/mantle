import sys


class Inst:

    def __init__(self, arch, pattern, action):
        self.pattern = pattern
        self.action = action

        self.bitlength = 0
        self.mask = 0
        self.bits = 0
        self.args = []

        self.parse(arch)

    def parse(self, arch):
        arg = None
        for i in range(len(self.pattern)):
            c = self.pattern[i]
            if c != ' ' and c != '\t':
                self.bitlength += 1
                self.bits <<= 1
                self.mask <<= 1
                if c == '0' or c == '1':
                    arg = None
                    self.bits |= (c == '1')
                    self.mask |= (c == '0' or c == '1')
                else:
                    if not arg or c is not arg['sym']:
                        arg = {}
                        arg['sym'] = c
                        arg['start'] = arch.word - i
                        arg['length'] = 1
                        arg['signed'] = c in arch.signed
                        self.args += [arg]
                    else:
                        arg['length'] += 1


class Arch:

    def __init__(self, lines):
        self.instructions = []
        self.signed = {}

        for line in lines:

            if line.startswith('word'):
                word = int(line.split()[1])
                # print 'word', word
                self.word = word
            elif line.startswith('signed'):
                # print 'signed', line[7]
                self.signed[line[7]] = True
            else:
                pattern = ''
                action = ''
                for i in range(len(line)):
                    c = line[i]
                    if c == ' ' or c == '\t':
                        continue
                    elif c == '#' or c == '\n' or c == '\r':
                        break
                    elif (c >= 'a' and c <= 'z') or c == '0' or c == '1':
                        pattern = pattern + c
                    elif c == '"':
                        rest = line[i + 1:]
                        n = rest.find('"')
                        action = rest[:n]
                        self.instructions += [Inst(self, pattern, action)]
                        break

