
def split_and_join(line):
   i = 0
   c = ""
   while i < len(line):
       if line[i] == " ":
           c = c + "-"
           i += 1
       else:
           c = c + line[i]
           i += 1
   return c
print(split_and_join(input().strip()))




