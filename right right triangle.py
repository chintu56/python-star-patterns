rows=int(input("enter the rows:"))
for i in range(rows):
    for j in range(rows-i):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    print()