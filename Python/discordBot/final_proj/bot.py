import discord, requests, json



class MyClient(discord.client):
	async def on_ready(self):
		print("Logged on as {0}".format(self.user));

	async def on_message(self, message):
		if message.author == self.user:	# Don't detect itself
			return

		if message.content.startswith("$hello"):
			await message.channel.send("Hi!")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("")	# token