import sys

shift = 8

def wc(f):
    lines = 0
    words = 0
    characters = 0

    for line in f:
        lines += line.endswith('\n')
        words += len(line.split())
        characters += len(line)

    prefix1 = " " * (shift - len(str(lines)))
    prefix2 = " " * (shift - len(str(words)))
    prefix3 = " " * (shift - len(str(characters)))
    print(f"{prefix1}{lines}{prefix2}{words}{prefix3}{characters}", end='')

    return lines, words, characters

if __name__ == "__main__":
    if len(sys.argv) > 1:
        total_lines = 0
        total_words = 0
        total_characters = 0

        for file in sys.argv[1:]:
            with open(file, 'r') as f:
                lines, words, characters = wc(f)
                print(f" {file}")
                total_lines += lines
                total_words += words
                total_characters += characters

        if len(sys.argv[1:]) > 1:
            prefix1 = " " * (shift - len(str(total_lines)))
            prefix2 = " " * (shift - len(str(total_words)))
            prefix3 = " " * (shift - len(str(total_characters)))
            print(f"{prefix1}{total_lines}{prefix2}{total_words}{prefix3}{total_characters} total")
    else:
       wc(sys.stdin)
