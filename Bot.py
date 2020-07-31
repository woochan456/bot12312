import discord
import asyncio
import datetime
import os

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print()
    print(client.user.name)
    print()
    print("준비 완료!!")


@client.event
async def on_message(message):
    if message.content.startswith("!!dm"):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[5:]
                    embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, )
                    embed.add_field(name="누군가 보낸 메시지", value=msg, inline=False)
                    await i.send(embed=embed)
                except:
                    pass



access_token = os.environ["TOKEN_TOKEN"]
client.run(access_token)
