import discord
from dispatcher import dispatcher
import random
import sys

d = dispatcher()
d.register_builtin('!ping', lambda msg: msg.channel.send('pong'))
d.register_builtin('!source', lambda msg: msg.channel.send('https://github.com/mr1337357/discordbot'))
d.register_builtin('!log',lambda msg: print(msg))
d.register_builtin('!reload',lambda msg: sys.exit(0))

d.register_cmd('!roll', lambda msg: msg.channel.send(random.randint(1,20)))
d.register_cmd('!socks', lambda msg: msg.channel.send(random.choice(['UwU','OwO','onii-chan'])),channels = ['programming-socks-gone-wild'])

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'logged on as {self.user}!')

    async def on_message(self,message):
        await d.dispatch_cmd(message)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
with open('.secret','r') as sec:
    secret = sec.readline()[:-1]
    client.run(secret)
