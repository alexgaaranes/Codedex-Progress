# Pokedex Class

class Pokedex:
	def __init__(self,entry,name,types,description,is_caught):
		self.entry = entry
		self.name = name
		self.types = types
		self.description = description
		self.is_caught = is_caught

	def speak(self):
		print(f"{self.name[0:len(self.name)//2]}! {self.name[0:len(self.name)//2]}!, {self.name}!...")

	def display_details(self):
		print(f"Entry number: {self.entry}\nName: {self.name}\nType: {self.types}\nDescription: {self.description}")
		if self.is_caught:
			print(f"{self.name} has already been caught!")
		else:
			print(f"{self.name} has never been caught...")


pikachu = Pokedex(25,"Pikachu","Electric","It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.",True)

pikachu.speak()
pikachu.display_details()