#def list_sum method 
def list_sum(list1):
    sum=0
    for s in list1:
        sum+=s
    return s
def list_sort(list1):
    list1.sort()
    return list1
def string_list_convertion(s):
    l1=list(s)
    return l1
    
    
#for accesing

from list_sum import*
list1=[10,30,20,50]
print(list_sum(list1))
print(list_sort(list1))
print(string_list_convertion("hello world"))
