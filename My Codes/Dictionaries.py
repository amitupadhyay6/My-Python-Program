# dicttionary is all about the "Keys" and "Valuses"

dict={"Amit": 30, "member":{1:"Vibha",2:"Eva"}}
print(dict)
print("1st member's age is ", dict["Amit"], "2nd member", dict["member"][1], "3rd member ", dict["member"][2])

#Add member
dict["book"]="color book"
print(dict)

# Print keys
key=dict.keys()
print(key)
value=dict.values()
print(value)

#Remove item
del dict["member"]
print(dict)

#len function
print(len(dict))

