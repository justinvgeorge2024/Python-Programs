#Program finding highest of two numbers using function 
x= int(input("enter x"))
y= int(input("enter y"))           
def high2(p,q):
 if p>q:
       m=x
 else:
       m=y
 return m
print ("highest is :",high2(x,y))
