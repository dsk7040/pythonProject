#overriding
class parent:
    def find_area(self):
        print("Parent class method")
class Child(parent):
    def find_area(self):
        super().find_area()
        print("child class method")
object = Child()
object.find_area()

#Overloading

class area:
   def find_area(self, x = None, y = None):
       if x != None and y != None:
           print(x*y)
       elif x != None:
           print(x*x)
       else:
           print("Nothing")


object = area()
object.find_area()
object.find_area(5)
object.find_area(5, 2)