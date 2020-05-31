
def solve(s):
     for i in range(len(s)):
        if i ==0 and s[0].isalpha():
            s = s.replace(s[0],s[0].upper(), 1)
        elif i < len(s) and s[i] == " ":
            if s[i+1].isalpha():
                s = s[:i] + s[i:].replace(s[i+1], s[i+1].upper(), 1)
     print(s)

s = input()
solve(s)
