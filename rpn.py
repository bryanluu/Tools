import sys
def execOp(op, *args):
    if len(args) < 2:
        raise TypeError(op + " operation needs at least 2 arguments! " + len(args) + " given.")

    ans = args[0]

    if op == '+':
        ans = sum(args)
    elif op == '-':
        ans -= sum(args[1:])
    elif op == '*' or op == 'x':
        for x in args[1:]:
            ans *= x
    elif op == '/':
        for x in args[1:]:
            ans /= x
    elif op == '//':
        for x in args[1:]:
            ans //= x

    return ans

def parseLine(tokens):
    op = tokens[-1]
    args = (map(float, tokens[:-1]))
    return op, args


if __name__ == "__main__":
    tokens = []
    if len(sys.argv) < 2:
        print("Enter RPN command:")
        line = input()
        tokens = line.split()
    else:
        tokens = sys.argv[1:]
    op, args = parseLine(tokens)
    ans = execOp(op, *args)
    print(ans)
