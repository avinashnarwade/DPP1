#Program for Demonstrating the Functionality of GC
#DestEx3.py
import time,sys
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parameterized Constructor:")
		self.eno=eno
		self.ename=ename
		print("\tEmployee Number=",self.eno)
		print("\tEmployee Name=",self.ename)
		print("-"*50)
	def __del__(self): # Destructor Def. called by GC
		print("\tGC Calls __del__()-For Dellocatin gthe Memory Space:")

#Main Program
print("Program Execution Started")
print("-----------------------------------------------")
eo1=Employee(10,"RS")
print("No Longer Interested to Use eo1 Object")
time.sleep(3)
eo1=None # Forcefull GC
time.sleep(3)
eo2=Employee(20,"DR")
print("No Longer Interested to Use eo2 Object")
time.sleep(3)
eo2=None # Forcefull GC
time.sleep(3)
eo3=Employee(30,"JH")
print("No Longer Interested to Use eo3 Object")
time.sleep(3)
eo3=None # Forcefull GC
print("Program Execution Ended")
print("-----------------------------------------------")