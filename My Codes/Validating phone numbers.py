
import re

n = int(input())
for i in range(n):
    str = input().strip()
    if len (str) == 10:
        mat = re.match(r"^[7|8|9][0-9]{9}", str)
        if mat: print("YES")
        else: print("NO")
    else:
        print("NO")

        # mak = re.match(r"[789]\d{9}",str)
        # if mak: print("YES")
        # else: print("NO")

