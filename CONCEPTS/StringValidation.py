''''
The validation rules are as follows:

The string is valid only if it starts with lowercase characters, followed by special characters !@#$% followed by numbers.
In any other case the string is not valid.
Example:

Input: 
str = asdsab@!@234
Output: 
True
Explanation: 
The string is valid as characters are
followed by special case characters 
which are then followed by numbers.
'''
def validate(str):
    pat= re.compile('[a-z]+[!@#$%]+[0-9]+')##your pattern here
    match = re.search(pat, str)
    if(match):
        return True
    else:
        return False

