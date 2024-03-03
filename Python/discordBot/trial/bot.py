#Token: MTIxMzgzMDAwMDgzOTYzMDg5OA.GVItAC.wqXCGzQ8PdWf6dFXarScYfjqTewyyfRaqKlhWo

import discord, requests, json, random

def slot():
	symbols = ["7️⃣","🍒","🍉","🍒","🍒","🍉","🍉","🍇","🍇","🍇"]

	rolled = random.choices(symbols, k=3)
	result = ""
	if rolled == ["7️⃣","7️⃣","7️⃣"]:
		result = "Jackpot! 💰"
	elif rolled == ["🍒","🍒","🍒"]:
		result = "Nice Try!"
	elif rolled == ["🍉","🍉","🍉"]:
		result = "Not Bad!"
	elif rolled == ["🍇","🍇","🍇"]:
		result = "Wow Grape!"
	else:
		result = "Try Again..."
	return rolled, result



def get_meme():
	response = requests.get('https://meme-api.com/gimme')
	json_data = json.loads(response.text)
	return json_data['url']

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged on as {0}!'.format(self.user))

	async def on_message(self, message): # Prints a message
		if message.author == self.user:
			return

		if message.content.startswith('$sorry'):
			await message.channel.send("I'm choni...")

		if message.content.startswith("$meme"):
			await message.channel.send(get_meme())

		if message.content.startswith("$slot"):
			rolled, result = slot()

			outcome = ""
			# format rolled
			for i in range(len(rolled)):
				if i!=len(rolled)-1:
					outcome += rolled[i] + " | "
				else:
					outcome += rolled[i]

			outcome += "\n"+result
			await message.channel.send(outcome)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTIxMzgzMDAwMDgzOTYzMDg5OA.GVItAC.wqXCGzQ8PdWf6dFXarScYfjqTewyyfRaqKlhWo') # Replace with your own token.
