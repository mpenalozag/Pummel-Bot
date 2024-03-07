import os
import discord
from dotenv import load_dotenv
from commander import Commander

load_dotenv()

token = os.getenv('BOT_TOKEN')

class MyClient(discord.Client):
  def __init__(self, intents):
    super().__init__(intents=intents)
    self.commander = Commander() 

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    if message.author == client.user:
      return
    if message.content == "hola":
      await self.commander.send_message(message)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

print(discord.Client)