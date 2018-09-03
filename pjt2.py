def getbackwards(input_string):
   output = ''
   for x in range(0,len(input_string),-1):
       output += input_string[x]
   return output

def every_other(input_string):
	output = ''
	for i in range(len(input_string)):
		# print('Iteration of the for loop' + str(i))
		if(i%2) == 0: # Do nothing when i%2 != 0
			output += input_string[i] # appending characters, not addition
	print(output)
	
user_input = input("Give me a word: ") # Will still need to change this a bit
every_other(user_input) # Temporary call for testing

 
# ============================== NOTES ============================================== 
# print(user_input[0] + user_input[2])

# 'user_input' = WORD
# len(user_input) = 4 -> number of chars in input
# range(len(user_input)) = {0, 1, 2, 3}
# 'part of the range' -> variable i



# What is this program doing?
# Print every other letter of the user_input
# Eventually, we need to print
# How to determine what to print?

# a += b

# a = a + b

# ============================== END NOTES =====================================