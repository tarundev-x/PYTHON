def change(i):
    if str.islower(i):
        return  str.upper(i)
    else:
        return str.lower(i)
    
def swap_case(s):
    return ''.join(map(change,s))

    

if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result
