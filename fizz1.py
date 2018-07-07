for fizzbuzz in range(50):
	if fizzbuzz % 3 == 0:
		print(str(fizzbuzz) + "fizz",end='')
		continue
	if fizzbuzz % 5 ==0:
		print(str(fizzbuzz) + "buzz",end='')
		continue
	print(fizzbuzz,end='')