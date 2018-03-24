char=input()
if ord(char)>=65 and ord(char)<=90:
    print("You entered an upper case alphabet.")
    if char in ['A','E','I','O','U']:
        print("you entered a vowel")
    else:
        print("You entered a constant")
elif ord(char)>=97 and ord(char)<=122:
    print("You entered an lower case alphabet.")
    if char in ['a','e','i','o','u']:
        print("you entered a vowel")
    else:
        print("You entered a constant")
else:
    print("You did not enter an alphabet")
