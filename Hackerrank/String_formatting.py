def print_formatted(number):
    w=len("{0:b}".format(number))
    for i in range(1,number+1):
        print("{0:{l}d} {0:{l}o} {0:{l}X} {0:{l}b}".format(i,l=w))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
