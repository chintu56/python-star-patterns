rows=int(input("enter the no of rows:"))
for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()