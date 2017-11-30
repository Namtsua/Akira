import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' ' + bot.user.id)

#  @bot.event
#  async def on_message(message):
#      await bot.send_message(message.channel, 'Hello World!')



#@bot.command(pass_context=True)
#async def sendInvite(ctxt):
   # await bot.accept_invite("https://discord.gg/SFV2y5")
 #   invite = await bot.create_invite(ctxt.message.server)
  #  await bot.send_message(ctxt.message.author, invite)


bot.run('token')