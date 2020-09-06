def prime(n):
	import math
	count = 0
	i = 1
	while count!=n:
		i = i+1
		for j in range(2 , int(math.sqrt(i))+1):
			if i%j == 0:
				break
			else:
				pass
		else:
			count = count + 1
	return(i)	
