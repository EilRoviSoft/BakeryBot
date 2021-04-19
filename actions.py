import discord
import re
import time
import os
import asyncio
import codecs
from discord import Embed



class StarMember:
	actions = []

	def __init__(self, _id, _name, _actions):
		self.id = _id
		self.name = _name
		for i in range(len(_actions)):
			if _actions[i] != "None":
				self.actions.append(_actions[i])
			else:
				self.actions.append(anti_selector[i])


def checkID(FEl):
	id_list = open("id_list.txt", "r")
	lines = id_list.readlines()

	for i in range(len(lines)):
		if re.search(FEl, lines[i]):
			_id = lines[i].split(":")[0]
			_name = lines[i].split(":")[1]
			actions = []

			for j in range(len(selector)):
				actions.append(lines[i].split(":")[j+1])

			user = StarMember(_id, _name, actions)
	
			id_list.close()

			return user

	return None

def checkLine(FEl):
	id_list = open("id_list.txt", "r")
	lines = id_list.readlines()

	for i in range(len(lines)):

		if re.search(FEl, lines[i]):

			return i

	return None

async def nsfw(message):
	description = " "

	if message.channel.is_nsfw() == 1:
		user = message.content.split(" ")[2]
		command = message.content.split(" ")[1]

		if command == "fuck":
			description = "You facked "+user+"!"

		elif command == "fap":
			description = "You fapped on "+user+"!"

		elif command == "cum":
			description = "You cummed on "+user+"!"

	else:

		description = "This channel isn't nsfw! Please, change channel."

	embed_obj = Embed(description = description, colour = message.author.colour)
	embed_obj.set_author(name = message.author.display_name, icon_url = message.author.avatar_url)
	return embed_obj

async def action(message):
	command = selector[message.content.split(" ")[1]]
	user = checkID(str(message.author.id))

	description = user.name + ", " + message.author.mention + ", " + user.actions[command]

	return description

async def workact(message):
	tyre = message.content.split(" ")[1]
	current_id = str(message.author.id)

	if tyre == "add":
		if checkID(current_id) == None:
			id_list = open("id_list.txt", "a")
			id_list.write("\n" + str(message.author.id) + ":" + message.content.replace("/workact add ", ""))
			embed_obj = Embed(description = "New unical actions added " + message.author.display_name + "!", colour = message.author.colour)
			embed_obj.set_thumbnail(url = message.author.avatar_url)
			id_list.close()
			return embed_obj
		else:
			embed_obj = Embed(description = "You have already had your own actions! Please, use command /workact edit!", colour = message.guild.me.colour)
			return embed_obj

	elif tyre == "edit":

		current_line = checkLine(current_id)

		if current_line != None:
			id_list = open("id_list.txt", "r")
			lines = id_list.readlines()
			id_list.close()
			
			id_list = open("id_list.txt", "w")
			lines[current_line] = str(message.author.id) + ":" + message.content.replace("/workact edit ", "")

			for i in range(len(lines)):
				id_list.write(lines[i])

			id_list.close()

			embed_obj = Embed(description = "Unical actions was edited for user " + message.author.display_name + "!", colour = message.author.colour)
			embed_obj.set_thumbnail(url = message.author.avatar_url)
			return embed_obj

		else:
			embed_obj = Embed(description = "You havn't own unical actions! Please, use command /workact add!", colour = message.guild.me.colour)
			return embed_obj

	elif tyre == "delete":

		current_line = checkLine(current_id)

		if current_line != None:
			id_list = open("id_list.txt", "r")
			lines = id_list.readlines()
			id_list.close()
			
			id_list = open("id_list.txt", "w")
			del lines[current_line]

			for i in range(len(lines)):
				id_list.write(lines[i])

			id_list.close()

			embed_obj = Embed(description = "Unical actions was deleted for user " + message.author.display_name + "!", colour = message.author.colour)
			embed_obj.set_thumbnail(url = message.author.avatar_url)
			return embed_obj

		else:
			embed_obj = Embed(description = "Not found your unical actions!", colour = message.guild.me.colour)
			return embed_obj