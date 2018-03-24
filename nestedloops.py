for var1 in range(2,101):
    flag=True
    for var2 in range(2, var1-1):
        if(var1%var2==0):
            print(var1, "is not a prime number")
            flag=False
            break
    if flag:
            print(var1, "is a prime number.")
