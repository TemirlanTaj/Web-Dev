# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

txt = input()
pat = input()
res = []
for i in range(len(txt) - len(pat) + 1):
    if re.search(pat, txt[i:i+len(pat)]):
        res.append((i, i+len(pat)-1))

if not res:
    res.append((-1, -1))

for i in res:
    print(i)