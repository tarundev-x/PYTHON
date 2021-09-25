Dictionary to store branchcode->name
dict_ds={05:"CSE",12:"IT",03:"ECE",04:"MECH"}
print dict_ds
#type of data structure
print type(dict_ds)
#accessing elements from the dictionary
res=dict_ds[12] #dictionary_name[key]
print "At key 12 the value is {}" .format(res)
#New dictionary
#Key-Unique,value:Repeated
dict_ds1={05:"CSE",05:"CSE-C","Name":"Priya","Fname":"Priya"}
print dict_ds1
#Modify the values from the dictionary
print "Old value is %s" %dict_ds1["Name"]#dictionary_name[key]
dict_ds1["Name"]="Devi"#dictionary_name[key]=NewValue
print "New value is %s" %dict_ds1["Name"]#Devi
#Add New Keys to dictionary?
#dict_ds1[key]=value
dict_ds1["Department"]="CSE"
print "New Dict After Adding Key"
print dict_ds1



'''
{4: 'MECH', 3: 'ECE', 12: 'IT', 5: 'CSE'}
<type 'dict'>
At key 12 the value is IT
{5: 'CSE-C', 'Fname': 'Priya', 'Name': 'Priya'}
Old value is Priya
New value is Devi
New Dict After Adding Key
{'Department': 'CSE', 5: 'CSE-C', 'Fname': 'Priya', 'Name': 'Devi'}
'''
dict={1:"cse",2:"it",3:"pt",4:" agri"}
r=dict.keys()
print r#[1, 2, 3, 4]
dict.pop(3)
print dict#{1: 'cse', 2: 'it', 4: ' agri'}
dict["new"]="pp"
print dict#{1: 'cse', 2: 'it', 4: ' agri', 'new': 'pp'}
res=dict.values()
print res#['cse', 'it', ' agri', 'pp']
