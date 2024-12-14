# write a program to print the pascals triangle.
#ncr=n!/(n-r)!.r!
""" 
              0c0           
           1c0    1c1
        2c0   2c1   2c2
    3c0     3c1    3c2   3c2
4c0    4c1     4c2    4c3   4c4 
                                              
                                              
                                              """


from math import factorial
rows=int(input("enter the number of rows:"))
for n in range(rows):

    for space in range(1,rows-n):
        print(end=" ")
    for r in range(n+1):
        ncr=factorial(n)//(factorial(r)*factorial(n-r))
        print(ncr,end=" ")
    print()