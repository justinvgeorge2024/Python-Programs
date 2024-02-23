# Program 1 creating a class,object
class Employee:
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1  #emp count gets updated for every instance created.
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)
   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print (Employee.empCount)  # this command
emp1.displayCount()         # and this command
print(emp2.empCount)        # and this command will print same value [i.e, current value of empCount]
