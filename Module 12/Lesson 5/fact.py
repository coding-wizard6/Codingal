def r(n):
    if n==1:
        return n
    else:
        return n*r(n-1)

num=int(input("Enter number: "))

if num<0:
    print("No factorial")

elif num==1:
    print("Factorial is 1")

else:
    print("Factorial is",r(num))