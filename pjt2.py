def getbackwards(input_string):
	#==============FUNCTION SCOPE==================
	output = ''   # user_input = fungus -> len(user_input) = 6
	              # f->user_input[0] ... s -> user_input[5] ... {0,1,2,3,4,5} ... user_input[len(user_input)]
	for x in range(len(input_string) - 1, -1, -1): # (0, len(input_string), -1) -> start->inclusive, stop->exclusive, step : range(0, len(user_input)) [0,1,2,3,4,5,6]
		output += input_string[x]
	print(output)

def every_other(input_string):
	#==============FUNCTION SCOPE==================
	output = ''
	for i in range(len(input_string)):
		# print('Iteration of the for loop' + str(i))
		if(i%2) == 0: # Do nothing when i%2 != 0
			output += input_string[i] # appending characters, not addition
	print(output)
	
#palimdrome -> string reads backwards the same as it does reading forwards. If not palimdrome, print they are a little, insignificant bitch
# return true or false
def palimdrome(input_string): # down -> len(input_string) = 4
	#==============FUNCTION SCOPE==================
	for i in range(len(input_string)): # [0,1,2,3]
		if user_input[i] != user_input[len(user_input) -1 - i]:
			return False # As in, not a palindrome
	return True
	# code here
	# fungus
	# datatypes: strings (words or sentences), integers (whole numbers), characters (singular letters or symbols or 'numbers'), others
	# 0 != user_input[0], user_input[0] == 'f'
	# Step 1: Get string -> get string into the scope of the function
	# 
	# if ('f' == user_input[0]):
	#     code for if statement would run
	#
	# step 2: Computer needs to know values of each character, needs to know if those values are the same
	# Step 3: 
	# Step 4: 
	# Big, significant betch (if it is a palimdrome)
	# funfuck <-
	# user_input[0] == f ? yes
	# user_input[3] == f ? yes
	# f == f ? yes
	# user_input[0] == f
	# user_input[0] == user_input[3] <-
	# len(user_input) = number of characters in the string <- will likely be useful
	# range() <- will likely be useful
	# len(user_input) -> evaluates to a number 7
	# user_input : [0,1,2,3,4,5,6] -> 6 
	# user_input[len(user_input)-1] == user_input[6] == k
	# if(some condition is true, run IF statement code)
	# user_input[0] == user_input[len(user_input) -1]             leftSide | rightside-1
	# user_input[1] == user_input[len(user_input) -2]           leftSide+1 | rightside-2
	# user_input[2] == user_input[len(user_input) -3]           leftSide+2 | rightside-3
	
	
# ========================GLOBAL SCOPE========================================
user_input = input("Give me a word: ") # Will still need to change this a bit
getbackwards(user_input) # Temporary call for testing
every_other(user_input) # temporary call for testing
print(palimdrome(user_input)) # dummy call for palimdrome

 
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