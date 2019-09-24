import sys
def execOp(op, *args):
    if len(args) < 2:
        raise TypeError(op + " operation needs at least 2 arguments! " + len(args) + " given.")

    ans = args[0]

    if op == '+':
        ans = sum(args)
    elif op == '-':
        ans -= sum(args[1:])
    elif op == 'x':
        for x in args[1:]:
            ans *= x
    elif op == '/':
        for x in args[1:]:
            ans /= x
    elif op == '//':
        for x in args[1:]:
            ans //= x
    elif not isOp(op):
        raise TypeError("Invalid operator: " + op)

    return ans

def parseLine(tokens):
    op = tokens[-1]
    args = (map(float, tokens[:-1]))
    return op, args

def isOp(c):
    return (c == '+' or c == '-' or c == 'x' or c == '/' or c == '//')

if __name__ == "__main__":
    stack = []
    if len(sys.argv) < 2:
        print("Enter RPN command:")
        line = input()
        stack = line.split()
    else:
        stack = (sys.argv[1:])
    while(len(stack) > 1):
        for i, c in enumerate(stack):
            if isOp(c):
                op, args = parseLine(stack[:i+1])
                ans = execOp(op, *args)
                del stack[:i]
                stack[0] = ans
                break
            elif not c.isdigit():
                raise TypeError("Invalid operator: " + c)

    print(stack[0])
