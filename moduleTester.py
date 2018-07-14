from modules.printModule import *
from modules.gameModules import *
#The following two lines are for testing the printNoNewLine() function from modules/printModule
printNoNewLine("<STRING1>The next string should be printed on the same line</STRING1>")
print("<STRING2>This is string 2</STRING2>\n")

#The following three lines are for testing the reverseString() function from modules/printModule
myString = "This is the string to be reversed"
print(myString)
print(reverseString(myString))

#The following 3 lines are to test the Player() class and setting/accessing the Player.health member variable
print("Attempting to create player class")
player = Player()
print("Player's health is: " + str(player.health))

#The following 3 lines test the Enemy class and it's initializer
enemies = []
for i in range(5):
	enemies.append(Enemy(i+1, 10))

#The following 3 lines have the dependency of the last 3 lines succeeding.
#These lines test the initializer of the gameEngine class and the gameEngine.runCombat method as well as a list as a function argument
gameEngine = GameEngine()
print("Attempting to start combat")
gameEngine.runCombat(enemies)

#More tests to come