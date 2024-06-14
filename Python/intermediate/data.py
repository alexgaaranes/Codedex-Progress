# Kansas City Chiefs

player_list = [
	{
	'name': 'John',
	'position': 'quarterback',
	'jersey_number': 29,
	'touchdowns': 4
	},
	{
	'name': 'Mavy',
	'position': 'center',
	'jersey_number': 14,
	'touchdowns': 3
	},
	{
	'name': 'John',
	'position': 'offensive_guard',
	'jersey_number': 45,
	'touchdowns': 10
	}
]

# Print all positions
print("Positions:")
for player in player_list:
	for k,v in player.items():
		if k == "position":
			print(v)
print()


# Update Mavy
for player in player_list:
	if player['name'] == "Mavy":
		player['touchdowns'] += 1;

# Average touchdowns
total = 0
average = 0
for player in player_list:
	total += player['touchdowns']
average = total/len(player_list)
print("Average touchdowns:", average)
