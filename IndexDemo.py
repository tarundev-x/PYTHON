'''Difference between index() and find()
#index(Substring)
#2.index(Substring,startindex)
#3.index(substring,startindex,endindex)

Returns the integer value that indicates index of first
occurence if string is existed.

Raises an error if the string is not existed in the main
string

'''
s="Python"
res_index=s.index("o")#searching O from the python
print "index()"
print res_index#4

res_index=s.index("Z")#Searching Z from the python

#print "index() with error generation"
print res_index #value error:substring not found
print "Hello"#is this statement is executed or not -No



'''
find() return -1 if the string is not existed
find() can be used with Control statements
...if,if-else,elif,....
find() is only for strings

'''















