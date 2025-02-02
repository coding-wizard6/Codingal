num=57
gnum=int(input("Guess the number:"))

if gnum==num:
    print("Correct Guess!!!")

elif gnum<60 and gnum>50:
    print("You are very close")

else:
    print("Try again")