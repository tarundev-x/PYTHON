
'''
Enumerate: Enumerate is built-in python function that takes input as iterator, list etc and 
  returns a tuple containing index and data at that index in the iterator sequence. For example, enumerate(cars), 
  
  returns a iterator that will return (0, cars[0]), (1, cars[1]), (2, cars[2]), and so on.
  '''

cars = ["Aston" , "Audi", "McLaren "]
for i, x in enumerate(cars):
    print (i,x)
    
    '''
 (0, 'Aston')
(1, 'Audi')
(2, 'McLaren ')
''
# Printing return value of enumerate() 
'''

cars = ["Aston" , "Audi", "McLaren "]
print enumerate(cars)
