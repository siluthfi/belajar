import time # to make delay

# receive input from user
inputfib = int(input('Please input number to generate fibonacci> '))

fib1 = 0
fib2 = 1
count = 0

if inputfib == 1 :
	print('That is first number of fibonacci.... try again')
else:
	print("Wait fibonacci being generate....")
	time.sleep(2)
	while count < inputfib :
		print(fib1)
		time.sleep(0.25)
		result = fib1 + fib2
		# update values
		fib1 = fib2
		fib2 = result
		count += 1
