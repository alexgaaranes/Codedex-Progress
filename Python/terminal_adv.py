# Inspired by the tiktok slideshows that plays like a decision-based RPG which results to different endings

# Status variable
health = 20

# Ending variable (There are endings that don't rely on these)
good = 0
mid = 0
bad = 0

print("---Lost in the Forest---\n")
print("\tYou are lost in an unknown forest.\n\tTry to escape alive!")

# START
print(f"HP: {health}n")
print("You just woke up.\n There are 2 paths in front of you.\n")
print("")
while True:
	

	d1 = int(input("Choice: "))