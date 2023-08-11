import sys
from unicodedata import name

print(sys.version)
print()
print('sys.stdout.isatty():', sys.stdout.isatty())
print('sys.stdour.encoding:', sys.stdout.encoding)
print()

test_chars = [
    '\N{HORIZONTAL ELLIPSIS}',
    '\N{INFINITY}',
    '\N{CIRCLED NUMBER FORTY TWO}'
]

for char in test_chars:
    print(f'Trying to output {name(char)}:')
    print(char)
