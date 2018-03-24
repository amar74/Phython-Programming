print("Enter numerator:")
num=input()
print("Enter denominator:")
den=input()
try:
       res=int(num)/int(den)
except:
       print("You Can't divided by 0 mah dear")
else:
       print("Result:",res)
