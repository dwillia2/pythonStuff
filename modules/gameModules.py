class Player(object):
	"""Simple player class"""
	def __init__(self):
		self.health = 10
		print("In the Player constructor, player created!")

class Enemy(object):
	"""Enemy class that holds the details of the enemies as well as their capabilities"""
	def __init__(self, id, health):
		self.id = id
		self.health = health

class GameEngine(object):
	"""Engine that controls the game"""
	def __init__(self):
		#placeholder
		print("Engine created")

	def runCombat(self, enemyArr):
		for enemy in enemyArr:
			print("Enemy " + str(enemy.id) + " joined the battle!")