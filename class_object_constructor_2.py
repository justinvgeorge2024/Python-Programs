# Program 2 creating constructors
class computers:
 
    # default constructor
    def __init__(self):
        self.clg = "Amal Jyothi"
 
    # a method for printing data members
    def print_clg(self):
        print(self.clg)
 
 
# creating object of the class
obj = computers()
 
# calling the instance method using the object obj
obj.print_clg()
