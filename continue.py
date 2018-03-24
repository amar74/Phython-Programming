for var in range(1,16):
    if(var in range(9,14)):
        continue
    else:
        print(var)
        
    
print("Enter a string:")
var=input()
for letter in var:
    if(letter==' '):
        continue
    else:
        print(letter)
