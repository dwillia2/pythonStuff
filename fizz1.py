for fizzbuzz in range(50):
	if fizzbuzz % 3 ==0 and fizzbuzz % 5 == 0:
		print(str(fizzbuzz) + "fizzbuzz",end='')
		continue
	elif fizzbuzz % 3 == 0:
		print(str(fizzbuzz) + "fizz",end='')
		continue
	elif fizzbuzz % 5 ==0:
		print(str(fizzbuzz) + "buzz",end='')
		continue
	print(fizzbuzz,end='')