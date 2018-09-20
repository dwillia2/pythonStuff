
# Step 1 - know what our class needs to do

class Character:

	def __init__(self):
		self.hp = 0
		self.str = 0
		self.defense = 0
		self.mp = 0
		self.mag_defense = 0
		self.luck = 0
		self.speed = 0
		self.magic = 0
		
	def attack_enemy(self):
		# enemy_hp -= self.str
		print('Enemy hit')
		

my_character = Character()
my_character2 = Character()
print('The constructed character object has ' + str(my_character.hp) + ' hit points')
my_character.attack_enemy()