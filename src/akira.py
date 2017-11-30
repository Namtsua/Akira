import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix='?', description="asdf")

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' ' + bot.user.id)

"""Deletes every message in a given channel"""
@bot.command(pass_context = True)
async def flushChannel(ctxt):
   messages = []
   async for message in bot.logs_from(ctxt.message.channel_mentions[0], limit = 1000000):
     messages.append(message)
   while len(messages) > 0:
     await bot.delete_messages(messages[0:99])

#@bot.command(pass_context=True)
#async def sendInvite(ctxt):
   # await bot.accept_invite("https://discord.gg/SFV2y5")
 #   invite = await bot.create_invite(ctxt.message.server)
  #  await bot.send_message(ctxt.message.author, invite)


bot.run('token')