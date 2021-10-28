class MyClass:
  #class variable exists without instances
  # every instance has its own class vars
  class_var = "Stuff"
  "!!!!!"
  "! ! ! ! !"

# instance variable exists only with instances
# every instance has its own
  def __init__(self, name = "default iName", birthmonth = 1 ):
    self.instance_name = name
    self.i_birthMonth = birthmonth

print(MyClass.class_var)
#print(MyClass.instance_name) #doesn't work
print("")

someClass = MyClass(birthmonth = 3)
print( someClass.instance_name)
print( someClass.i_birthMonth )
print("")

thirdClass = MyClass()
print(thirdClass)
print("")

newClass = MyClass("Barney")
secondClass = MyClass("Fife")
print(newClass.instance_name)
print(newClass.class_var)
print("")
print(secondClass.instance_name)
print(secondClass.class_var)
print("")

newClass.class_var = "ffutS"
print(MyClass.class_var)
print(newClass.class_var)
print(secondClass.class_var)
print("")

class MyChild(MyClass):
  # def __init__(self):
  #   #super("Horatio") #doesn't work
  #   super().__init__("Horatio")

  def __init__(self, age = 3 ): #trying cotr overload
  # python does not have method overloading, 
  # there is a way ... tricky ...
  #   self.age = age
    super().__init__("Nelson",5)
    self.i_age = age
    pass

fourthClass = MyChild()
print(fourthClass)
print(fourthClass.instance_name)
print(fourthClass.i_birthMonth)
print(fourthClass.i_age)