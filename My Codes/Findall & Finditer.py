
import re
#str = input().strip()
str = "rabcdeefgyYhFjkIoomnpOeorteeeeet"
str = "daadoooop"
mat = re.findall(r"[^aiueoAIUEO]([aiueoAIUEO]{2,})(?=[^aiueoAIUEO])", str)

if mat:
    for i in mat:
        print(i)
else:
    print(-1)




