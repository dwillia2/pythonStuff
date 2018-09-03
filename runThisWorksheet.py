import random

#Random enemy stats generator for physical traits, mental traits are static
class Enemy():

	def calc_bonus(self, param):
		return int((param - 10) / 2 if param >= 10 else 5 - (param / 2))

	def calc_stats(self, st, dex, con):
		self.attack = self.calc_bonus(st) + self.proficiency_bonus
		self.armor_class = 10 + self.calc_bonus(dex)
		self.hit_points = 0
		for i in range(self.level):
			self.hit_points += random.randint(1, 6) + self.calc_bonus(con)

	def __init__(self):
		self.level = random.randint(1, 2)
		self.strength = 10 + random.randint(1, 4) if self.level == 1 else 10 + random.randint(2, 6)
		self.dexterity = 10 + random.randint(1, 2) if self.level == 1 else 10 + random.randint(2, 4)
		self.constitution = 10 + random.randint(1, 2) if self.level == 1 else 10 + random.randint(2, 4)
		self.intelligence = 8
		self.wisdom = 7
		self.charisma = 6
		self.proficiency_bonus = 2
		self.calc_stats(self.strength, self.dexterity, self.constitution)

	def report(self):
		print("Enemy report:\nlevel: " + str(self.level) +"\nstrength: " + str(self.strength) + "\ndexterity: " + str(self.dexterity) + "\nconstitution: " + str(self.constitution) + "\nintelligence: " + str(self.intelligence) + "\nwisdom: " + str(self.wisdom) + "\ncharisma: " + str(self.charisma) + "\nhp: " + str(self.hit_points) + "\nAC: " + str(self.armor_class) + "\nattack: " + str(self.attack))

my_Enemy = Enemy()
my_Enemy.report()