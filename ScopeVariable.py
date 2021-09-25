#Local variable-Global variable
s=int(raw_input("Enter number"))#global variable
def factorial(number):
      fact=1#Local varaible and scope is limited to factorial
      for i in range(1,number+1):
            fact=fact*i
      print "Fact of %d is %d " %(s,fact)#s is global used in fact function


#call function
factorial(s)
print "Fact is %d " %fact #access outside of the function
'''
'''
#NameError: name 'fact' is not defined


#Fact of 7 is 5040 
