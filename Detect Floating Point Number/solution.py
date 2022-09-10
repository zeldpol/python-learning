# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

count = int(input().strip())
reg = "^[-|+]?\d*[.]\d+$"

for i in range(count):
    fl = input().strip()
    print(bool(re.match(reg ,fl)))

