import sys

def tail(f, number_of_lines):
    lines = f.readlines()
    if len(lines) <= number_of_lines:
        for line in lines:
            print(line, end='')
    else:
        for line in lines[-number_of_lines:]:
            print(line, end='')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        for i, file in enumerate(sys.argv[1:]):
            if (i > 0):
                print()
            if len(sys.argv[1:]) > 1:
                print('==> {} <=='.format(file))
            with open(file, 'r') as f:
                tail(f, 10)
    else:
        tail(sys.stdin, 17)