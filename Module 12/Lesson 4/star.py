
num=int(input("Number of row: "))

for i in range(1,num+1):
    for j in range(i):
        print("*",end=" ")
    print()