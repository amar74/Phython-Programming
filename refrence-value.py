employee={'Amarnath':5000, 'srk':2000}
def test (employee):
   new={'Buck':2000,'Amar':658}
   employee.update(new)
   print("Inside the function", employee)
   return
test (employee)
print("Outside the function:", employee)