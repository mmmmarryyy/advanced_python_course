import sys

shift = 6

def nl(file):
    try:
        line_number = 1
        for line in file:
            if line != "\n":
                prefix = " " * (shift - len(str(line_number)))
                print(f"{prefix}{line_number}  {line.strip()}")
                line_number += 1
            else:
                print()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    assert len(sys.argv[1:]) <= 1, f"you provide {len(sys.argv[1:])} files, 0 or 1 expected"
    
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            nl(f)
    else:
        nl(sys.stdin)
