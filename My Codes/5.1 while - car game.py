print('''Type start - to start the car \nType stop - to stop the car \nType quit - to exit''')
i=j=0
while 1:
    x=input("Enter your command = ").lower()
    if x=="start":
        if j!=0:
            print("Car has already started")
            continue
        print(" car started ")
        j+=1 # to check if car is already started
        i=0
    elif x=="stop":
        if i!=0:
            print("Car has already stopped")
            continue
        print("Car stopped")
        i+=1
        j=0 # to ere enable start after the stop
    elif x=="quit":
        print("We are exiting the game")
        break
    else:
        print(" Invalid command")
