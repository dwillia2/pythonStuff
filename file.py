import shutil # shutil not used yet
import os

# Let's play with the file system
# Delete the file if it exists
if not os.path.isfile(r'C:\Users\Rj\Codingstuff\pythonStuff\tempFile'):
	file = open('tempFile', 'w')
	file.write('Stuff')
	file.close()
if os.path.isfile(r'C:\Users\Rj\Codingstuff\pythonStuff\tempFile'):
	print('Success')
else:
	print('Failure')