var=100
def test():
	global var
	var=var+10
	print(var)
	return
test()
print(var)