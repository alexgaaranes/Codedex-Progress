# Inspired by the tiktok slideshows that plays like a decision-based RPG which results to different endings

# Status variable
health = 10

print("---Lost in the Forest---\n")
print("\tYou are lost in an unknown forest. Try to escape alive!\n")

# START
print("- You just woke up. There are 2 paths in front of you.")
print("\t1) A dark grassy path\n\t2) A path that leads to an orange light")
while True:
	ans = int(input(f"HP: {health}\nChoice: "))

	if ans!=1 and ans!= 2:
		print("invalid input")
	else:
		 break

if ans == 1:
	# Dark grassy path
	print("\n- You can't see a single thing but you can hear someone walking towards you.")
	print("\t1) Wait for that someone to get close\n\t2) Slowly walk back")

	while True:
		ans = int(input(f"HP: {health}\nChoice: "))

		if ans!=1 and ans!= 2:
			print("invalid input")
		else:
			 break

	if ans == 1:
		# Wait
		print("\n- A creepy masked guy came and swung an axe to you. Your arm got hit")
		print("You received a major damage.")
		health -= 5
		print("\t1) Run back from where you woke up\n\t2) Fight off the man")

		while True:
			ans = int(input(f"HP: {health}\nChoice: "))

			if ans!=1 and ans!= 2:
				print("invalid input")
			else:
				 break
		
		if ans == 1:
			# Run back
			print("\n- You only have on path left to go to")
			print("\t1) A path that leads to an orange light")

			while True:
				ans = int(input(f"HP: {health}\nChoice: "))

				if ans!=1:
					print("invalid input")
				else:
					 break

			# Orange light path
			print("\n- You saw an old cabin where the light comes from.")
			print("\t1) Sneak in the cabin\n\t2) Continue following the path")

			while True:
				ans = int(input(f"HP: {health}\nChoice: "))

				if ans!=1 and ans!= 2:
					print("invalid input")
				else:
					 break

			if ans == 1:
				# Sneak
				print("\n- A man with a cleave is in the kitchen chopping some meat.")
				print("\t1) Talk to the man\n\t2) Go back out")

				while True:
					ans = int(input(f"HP: {health}\nChoice: "))

					if ans!=1 and ans!= 2:
						print("invalid input")
					else:
						 break

				if ans == 1:
					# Talk
					print("\n- The man was shocked at first but understood your situation. He offered for you to stay the night.")
					print("\t1) Stay the night in the cabin\n\t2) Reject the offer")

					while True:
						ans = int(input(f"HP: {health}\nChoice: "))

						if ans!=1 and ans!= 2:
							print("invalid input")
						else:
							 break

					if ans == 1:
						# Stay
						print("\n- The man who helped you died from another man with an axe and went up to your bed to kil you too.")
						
						if health == 10:
							health -= 10
						else:
							health -= 5

						print(f"HP: {health}\nYou died")

					elif ans == 2:
						# Reject
						print("\n- The man insisted on helping you to go back to the city. You two went in the car and he dropped you off the city.")
						print("You made it out alive!")
						print("You win!")


				elif ans == 2:
					# Back out
					print("\n- A man with an axe was waiting for you")
					print("You received a major damage.")
					health -= 5

					if health == 0:
						print("You Died")
					else:
						print("You survived and ran back deep into the woods.")
						health -= 5
						print(f"HP {health}")
						print("You have no food and died of starvation.")


			elif ans == 2:
				# Path
				print("\n- After hours of walking, you met with an asphalt road.")
				print("\t1) Follow the road\n\t2) Wait for a vehicle")

				while True:
					ans = int(input(f"HP: {health}\nChoice: "))

					if ans!=1 and ans!= 2:
						print("invalid input")
					else:
						 break

				if ans == 1:
					# Follow
					print("\n- After a long walk, you made it into a city.")
					print("You escaped the forest.")
					print("You win!")

				elif ans == 2:
					# wait
					print("\n- The man with an axe caught up and killed you")

					if health == 10:
						health -= 10
					else:
						health -= 5

					print(f"HP: {health}\nYou died")
		elif ans == 2:
			# Fight
			print("\n- You got another hit from the axe completely severing your arm")
			health -= 5
			print(f"HP: {health}\nYou died")

	elif ans == 2:
		# Slowly walk back
		print("\n- You didn't find the way back and the man following you caught up.")
		print("You got stabbed from behind.")
		health -= 10
		print(f"HP: {health}\nYou died")

elif ans == 2:
	# Orange light path
	print("\n- You saw an old cabin where the light comes from.")
	print("\t1) Sneak in the cabin\n\t2) Continue following the path")

	while True:
		ans = int(input(f"HP: {health}\nChoice: "))

		if ans!=1 and ans!= 2:
			print("invalid input")
		else:
			 break

	if ans == 1:
		# Sneak
		print("\n- A man with a cleave is in the kitchen chopping some meat.")
		print("\t1) Talk to the man\n\t2) Go back out")

		while True:
			ans = int(input(f"HP: {health}\nChoice: "))

			if ans!=1 and ans!= 2:
				print("invalid input")
			else:
				 break

		if ans == 1:
			# Talk
			print("\n- The man was shocked at first but understood your situation. He offered for you to stay the night.")
			print("\t1) Stay the night in the cabin\n\t2) Reject the offer")

			while True:
				ans = int(input(f"HP: {health}\nChoice: "))

				if ans!=1 and ans!= 2:
					print("invalid input")
				else:
					 break

			if ans == 1:
				# Stay
				print("\n- The man who helped you died from another man with an axe and went up to your bed to kil you too.")
				
				if health == 10:
					health -= 10
				else:
					health -= 5

				print(f"HP: {health}\nYou died")

			elif ans == 2:
				# Reject
				print("\n- The man insisted on helping you to go back to the city. You two went in the car and he dropped you off the city.")
				print("You made it out alive!")
				print("You win!")


		elif ans == 2:
			# Back out
			print("\n- A man with an axe was waiting for you")
			print("You received a major damage.")
			health -= 5

			if health == 0:
				print(f"HP: {health}")
				print("You Died")
			else:
				print("You survived and ran back deep into the woods.")
				health -= 5
				print(f"HP {health}")
				print("You have no food and died of starvation.")

	elif ans == 2:
		# Path
		print("\n- After hours of walking, you met with an asphalt road.")
		print("\t1) Follow the road\n\t2) Wait for a vehicle")

		while True:
			ans = int(input(f"HP: {health}\nChoice: "))

			if ans!=1 and ans!= 2:
				print("invalid input")
			else:
				 break

		if ans == 1:
			# Follow
			print("\n- After a long walk, you made it into a city.")
			print("You escaped the forest.")
			print("You win!")

		elif ans == 2:
			# wait
			print("\n- The man with an axe caught up and killed you")

			if health == 10:
				health -= 10
			else:
				health -= 5

			print(f"HP: {health}\nYou died")