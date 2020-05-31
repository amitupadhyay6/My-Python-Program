# There are four built-in data structures in Python - list, tuple, dictionary and set.
# Items in the list are kept in square braces and "," delimeter is used to separate the itesm in the list.
slist=["Apple", "Mango", "Banana"]
print("My list has ", len(slist), " items and my list is ", slist)
for n in slist:
    print(n, end=" ")
slist.sort()
print("\nSorted list are ", slist)
print("Add your fruit in the list")
slist.append(input("Add Item in the shopping list = "))
print("Updated list", slist)
slist.sort()
print("Sorted list are ", slist)
x=slist[0]
del slist[0]
print("i bought ", x)
print("\nNow items are in my list", slist)


''' We have used the append, del and sort function on the list and well as we have taken out the items from the list'''
