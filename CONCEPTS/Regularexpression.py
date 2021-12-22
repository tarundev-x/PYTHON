'''
Input: 
str = asdasd123asmdasdk34234kfdsd34sdfk5
Output: 
123 34234 34 5

'''
 pat=r'\d+'##write the pattern here
    match=re.findall(pat,str) ##find all finds all the matched texts and returns a list
    if(match): 
        for i in match:
            print(i, end=" ")
    else:
        print(-1,end="")
        
        '''
        
        import re
 
s = 'GeeksforGeeks: A computer science portal for geeks'
 
match = re.search(r'portal', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())
'''
 Start Index: 34
End Index: 40
  ''''
  [\d+] = one digit (0-9) or + character.

\d+ = one or more digits.
        
