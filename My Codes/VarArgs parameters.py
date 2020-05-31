# Sometimes you might want to define a function that can take any number of parameters, i.e.
# variable number of arguments, this can be achieved by using the stars

# Two star is required for the next variable argument
def fun(a,*num,**Phone,):
    print("a ", a)

    for single_part in num:
        print("Single Item", single_part)
    for first_part, second_part in Phone.items():
        print( first_part, second_part)

fun(5,7,9,6,jack=12,mack=14, sack=13, crack=10)
