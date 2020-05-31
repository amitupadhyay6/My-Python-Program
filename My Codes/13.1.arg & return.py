
def volume(len, wid, hig):
    print(len*wid*hig)

print(volume(5,hig=3, wid=7)) ####### by default func return None, use "retrn" to return value
#volume(len=5,4,wid=3) #####SyntaxError: positional argument follows keyword argument

def square(x,y):
    return x*y ############## It will return the value
x=square(5,8)*2
print(square(5,8), x)
