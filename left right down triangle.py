rows=int(input("enter the number:"))
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print('*',end=" ")
    print()