rows=int(input("enter the no of rows:"))
for i in range(1,rows):
    for space in range(1,rows-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(rows,0,-1):
    for space in range(1,rows-i+1):
        print(end=" ")
    for star in range(1,i+1):
        print("*",end=" ")
    print()