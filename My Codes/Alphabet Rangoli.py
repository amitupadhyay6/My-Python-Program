from string import ascii_lowercase

charlist = []
for c in ascii_lowercase:
    charlist.append(c)
#numrangoli = int(input())
numrangoli = 5
d = "-"
mid = charlist[numrangoli-1]
## Top Line
for i in range(1, numrangoli):
    print(d*((numrangoli-i)*2)+mid+d*((numrangoli-i)*2))
    mid = charlist[numrangoli-(i+1)]+ "-" + mid + "-" + charlist[numrangoli-(i+1)]

## Middle Line
print(mid)

## Bottom Line

