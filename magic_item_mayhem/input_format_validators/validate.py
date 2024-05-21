#!/usr/bin/env python3
import sys
import re

line = sys.stdin.readline()

# Check if the input is in the correct format
if not re.match(r"^[1-9][0-9]* [1-9][0-9]*(\n|\r|\r\n)$", line):
    sys.exit(43)

n, m = map(int, line.split())

# Check if the input is within the constraints
if not (1 <= n <= 50 and 1 <= m <= 300):
    sys.exit(43)

names = set()

for i in range(n):
    line = sys.stdin.readline()
    if not re.match(r"^[a-zA-Z]+(\n|\r|\r\n)$", line):
        sys.exit(43)
    name = line.strip()
    if name in names:
        sys.exit(43)
    names.add(name)

for i in range(m):
    line = sys.stdin.readline()
    if not re.match(r"^[12345] ([a-zA-Z]+ )*[a-zA-Z]+(\n|\r|\r\n)$", line):
        sys.exit(43)
    line = line.split()
    for name in line[1:]:
        if name not in names:
            sys.exit(43)

if sys.stdin.readline() != "":
    sys.exit(43)

sys.exit(42)