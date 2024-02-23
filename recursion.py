#Program using recursion
l=int(input("enter lower range"))
u=int(input("enter upper range"))
def displayrange(lower,upper):
    if lower<=upper:
        print(lower)
        displayrange(lower+1,upper)

displayrange(l,u)
