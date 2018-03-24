#employee={'Amar':5000, 'mark':1800, 'abhay':8987}
#def test(employee):
 #   employee={'Buck':2000,'Stan':5000}
  #  print("Inside the function", employee)
  #  return
#test(emplyoee)
print("Outside the function:", employoee)
employee={'Amar':5000, 'mark':1800, 'abhay':8987}
def test(employee):
    new={'Buck':2000,'Stan':5000}
    employee.update(new)
    print("Inside the function", employee)
    return
test(employee)
print("Outside the function:", employee)
