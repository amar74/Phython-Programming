var=100
def sample(var):
	print("Local value:", var)
	return
print("Global Value:", var)
sample(var)