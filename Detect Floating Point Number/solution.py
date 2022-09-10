# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true

import sys
import re

count = int(input().strip())
reg = "^[-|+]?\d*[.]\d+$"

for i in range(count):
    fl = input().strip()
    print(bool(re.match(reg ,fl)))

