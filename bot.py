import discord
import aiohttp
import asyncio
from token import TOKEN # type: ignore
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

        if message.content.startswith('$meme'):
            async with aiohttp.ClientSession() as session:
                async with session.get('https://meme-api.com/gimme') as resp:
                    if resp.status != 200:
                        return await message.channel.send('Could not fetch meme 😢')
                    data = await resp.json()
                    await message.channel.send(data['url'])

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN) 