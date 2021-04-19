import discord
import re
import time
import os
import asyncio
import codecs
from discord import Embed
import plus

class Bakery(discord.Client):
	global timeDelay
	global debug_guild
	global debug_channel
	global copy_channel
	global bot_owners

	timeDelay = int(0)
	bot_owners = [504972126885773312, 713194419704037439]

	async def is_owner(self, member):
		for el in bot_owners:
			if el == member:
				return True
		return False

	async def not_owner(self, message):
		embed_obj = Embed(description = "You don't have sufficient rights to use this command!", colour = message.guild.me.colour)
		return embed_obj

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	async def self_delete(self, message):
		await asyncio.sleep(self.timeDelay)
		await message.delete()

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	async def printing(self, embed_obj, message, channel):
		if self.timeDelay != 0:
			async with message.channel.typing():
				await asyncio.sleep(self.timeDelay)
		
		await channel.send(embed = embed_obj)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	async def duple(self, embed_obj, message):
		await self.debug_channel.send(embed = embed_obj)

		new_embed = Embed(colour = message.guild.me.colour)
		new_embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
		new_embed.add_field(name = "Message content", value = message.content)
		new_embed.add_field(name = "Message was created at", value = message.created_at)
		new_embed.add_field(name = "Message channel", value = message.channel)
		new_embed.add_field(name = "Message guild", value = message.guild)
		new_embed.set_thumbnail(url = message.author.avatar_url)

		await self.debug_channel.send(embed = new_embed)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	async def on_ready(self):
		print("H&P can bake Baumkuhens for you, Admin!")
		self.timeDelay = 0
		activity = discord.Game(name = "Programming myself on C++/Sleepy Discord. Type '/help' to get more information", type = 2)
		await self.change_presence(status = discord.Status.online, activity = activity)	

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	async def on_connect(self):
		print("H&P connected to the Discord-server!")

	async def on_disconnect(self):
		print("H&P dissconected! Please, send there Admin!")

	async def on_resume(self):
		print("Working of H&P resumed! Thanks, Admin!")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	async def on_message(self, message):
		if message.author.bot == True or re.search("```", message.content.lower()):
			return

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		author_color = discord.Colour.default()
		if message.author.colour == discord.Colour.default():
			author_color = message.guild.me.colour
		else:
			author_color = message.author.Colour
	
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		if re.search("/print", message.content.lower()) or re.search("/p", message.content.lower()):
			prefix = ""
			if re.search("/print", message.content.lower()):
				prefix = "/print "
			elif re.search("/p", message.content.lower()):
				prefix = "/p "

			if re.search("def", message.content.lower()):
				prefix += "def "
				author_color = message.guild.me.colour

			embed_obj = Embed(description = message.content.replace(prefix, ""), colour = author_color)
			embed_obj.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
			await self.printing(embed_obj, message, message.channel)
			await self.duple(embed_obj, message)
			await self.self_delete(message)

		elif re.search("/attack", message.content.lower()):
			param = message.content.split(" ")[1]
			channel_de_attack = message.content.split(" ")[2]
			real_de_attack = plus.getChannel(message.guild, channel_de_attack)
			text = message.content.replace("/attack " + param + " " + channel_de_attack + " ", "")
			attacker = ""
			attacker_url = ""

			if param == "bot":
				attacker = message.guild.me.display_name
				attacker_url = message.guild.me.avatar_url
				author_color = message.guild.me.colour

			elif param == "me":
				attacker = message.author.display_name
				attacker_url = message.author.avatar_url

			embed_obj = Embed(description = text, colour = author_color)
			embed_obj.set_author(name = attacker, icon_url = attacker_url)

			await self.printing(embed_obj, message, real_de_attack)
			await self.self_delete(message)
			await self.duple(embed_obj, message)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		elif re.search("/fulldebug", message.content.lower()):
			if await self.is_owner(message.author.id) == False:
				embed_obj = await self.not_owner(message)

				await self.printing(embed_obj, message, message.channel)
				await self.duple(embed_obj, message)
				await self.self_delete(message)

			else:
				self.debug_guild = message.guild
				self.debug_channel = plus.getChannel(self.debug_guild, "debug_py")
				self.copy_channel = plus.getChannel(self.debug_guild, "copy-message_py")

				embed_obj = Embed(description = "Debug channel "+str(self.debug_channel)+" is succesfully connected in server "+str(self.debug_guild)+"!", colour = message.guild.me.colour)

				if message.content == "fulldebug":
					self.timeDelay = 0
				else:
					self.timeDelay = float(message.content.replace("/fulldebug ", ""))

				await self.printing(embed_obj, message, message.channel)
				await self.duple(embed_obj, message)
				await self.self_delete(message)

		elif re.search("/setdelay", message.content.lower()):
			if await self.is_owner(message.author.id) == False:
				embed_obj = await self.not_owner(message)

				await self.printing(embed_obj, message, message.channel)
				await self.duple(embed_obj, message)
				await self.self_delete(message)

			else:
				self.timeDelay = float(message.content.replace("/setdelay ", ""))
				text = ""
				if self.timeDelay == 0:
					text = "Delay cleared by "+str(message.author)+"!"
				elif self.timeDelay <= 1:
					text = "Delay changed by "+str(message.author)+" on "+str(self.timeDelay)+" second!"
				else:
					text = "Delay changed by "+str(message.author)+" on "+str(self.timeDelay)+" seconds!"

				embed_obj = Embed(description = text, colour = message.guild.me.colour)

				await self.Printing(embed_obj, message, message.channel)
				await self.duple(embed_obj, message)
				await self.selfDelete(message)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		elif re.search("/nsfw", message.content.lower()):
			embed_obj = await nsfw(message)
			await self.printing(embed_obj)

		elif re.search("/action", message.content.lower()):
			description = await action(message)
			await message.channel.send(description)

		elif re.search("/workact", message.content.lower()):
			embed_obj = await workact(message)
			await self.printing(embed_obj, message, message.channel)
			await self.duple(embed_obj, message)
			await self.self_delete(message)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

		elif re.search("/igni", message.content.lower()):
			await self.self_delete(message)

		new_embed = Embed(colour = author_color)
		new_embed.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
		new_embed.add_field(name = "Message conetent", value = message.content)
		new_embed.add_field(name = "Message was create at", value = message.created_at)
		new_embed.add_field(name = "Message channel", value = message.channel)
		new_embed.add_field(name = "Message guild", value = message.guild)

		#await self.copy_channel.send(embed = new_embed)