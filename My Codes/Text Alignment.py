#thickness = int(input()) #This must be an odd number
c = 'H'
thickness = 5
k = " "
s = thickness // 2
#Top Cone
for i in range(thickness):
    print(((c*i).rjust(thickness-1, " ")+c+(c*i).ljust(thickness-1," ")))

#Top Pillars
for i in range(thickness+1):
    print(k*s+(c*thickness).ljust(thickness*2, " ")+k*thickness*2+(c*thickness).ljust(thickness*6, " "))

#Middle Belt
for i in range((thickness+1)//2):
    print(k*s+(c*thickness)+(c*thickness*3)+(c*thickness))

#Bottom Pillars
for i in range(thickness+1):
    print(k*s+(c*thickness).ljust(thickness*2)+k*thickness*2+(c*thickness).ljust(thickness*6))

#Bottom Cone
i = thickness-1
while i >= 0:
    print((c*i).rjust((thickness*5)-1, " ")+c+(c*i).ljust(thickness-1," "))
    i -= 1
