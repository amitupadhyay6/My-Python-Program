
dic={
    "name":"Amit Up",
    "name":"Vibha", # This one replace the value of name
    "Name":"Eva",
    "age":31,
    "email":"gmail"
}
print(dic, dic.get("surname", "Upadhyay")) # this will return Upadhyay, if key is not found.
dic["name"]="Amit"
dic["Mobile"]=70426
print(dic, dic.get("Mobile","new num"))
