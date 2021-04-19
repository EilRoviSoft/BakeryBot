import discord
import re
import time
import os
import asyncio
import codecs
from discord import Embed
from plus import getMember, getRole
from permissions import power

async def AID(message, tyre, command):
	colour = message.guild.me.colour

	if tyre == "main":
		embed_obj = Embed(title = "Menu of our Bakery", description = "Print /help + 'command name' to get description", colour = colour)
		embed_obj.add_field(name = "System Commands", value = "```/fulldeubg``` ```/setdelay```")
		#embed_obj.add_field(name = "Moderation Commands", value = "```/ban``` ```/kick``` ```/mute``` ```/unmute```")
		embed_obj.add_field(name = "Info Commands", value = "```/help``` ```/avatar``` ```/userinfo``` ```/roleinfo``` ```/serverinfo``` ```/botinfo```")
		embed_obj.add_field(name = "Text Commands", value = "```/print``` ```/attack```")
		#embed_obj.add_field(name = "Emoji Commands", value = "```/emoji``` ```/allemoji``` ```/displayall```")
		#embed_obj.add_field(name = "Unique Commands", value = "```/clear```")
		#embed_obj.add_field(name = "Postfix Commands", value = "```igni``` ```pin```")
		#embed_obj.add_field(name = "Funny Commands", value = "```/pingabuse```")
		embed_obj.add_field(name = "Action Commands", value = "```/nsfw``` ```/action``` ```/workact```")

		return embed_obj

	elif tyre == "catar":
		elif command == "setdelay":
			embed_obj = Embed(title = command, description = "Change delay between your commnad and bot's message", colour = colour)
			embed_obj.add_field(name = "Example", value = "```/setdelay 'time-for-delay'``` ```/setdelay 0.15```")
			embed_obj.add_field(name = "Possible values of time-for-delay", value = "```Number (seconds)``` ```0```")
			return embed_obj

		elif command == "fulldebug":
			embed_obj = Embed(title = command, description = "Full debuging connection to server. Use only, if you have channels debug_py and copy-message_py!", colour = colour)
			embed_obj.add_field(name = "Example", value = "```/fulldebug 'None-or-num'``` ```/fulldebug 0.15```")
			embed_obj.add_field(name = "Possible values of None-or-num", value = "```Number (seconds)``` ```Nothing```")
			return embed_obj

		elif command == "print":
			embed_obj = Embed(title = command, description = "Print your message with Embed", colour = colour)
			embed_obj.add_field(name = "Example", value = "```/print 'your-text'``` ```/print this is Embed!```")
			return embed_obj

		elif command == "attack":
			embed_obj = Embed(title = command, description = "Print your message with Embed in current channel", colour = colour)
			embed_obj.add_field(name = "Example", value = "```/attack 'channel-name' 'your-text'``` ```/attack main_py this is Embed!```")
			embed_obj.set_footer(text = "Channel name must be without #")
			return embed_obj

		elif command == "nsfw":
			embed_obj = Embed(title = command, description = "NSFW-Commands for role-play and fun", colour = colour)
			embed_obj.add_field(name = "fuck", value = "```Fuck somebody``` ```/nsfw fuck @mention-player-or-role``` ```/nsfw fuck @Hikka```")
			embed_obj.add_field(name = "cum", value = "```Cum on somebody``` ```/nsfw cum @mention-player-or-role``` ```/nsfw cum @Hikka```")
			embed_obj.add_field(name = "fap", value = "```Fap on somebody``` ```/nsfw fap @mention-player-or-role``` ```/nsfw fap @Programmer```")
			return embed_obj

		elif command == "action":
			embed_obj = Embed(title = command, description = "Action-Commands for role-play and fun", colour = colour)
			embed_obj.add_field(name = "nya or first", value = "```Just say Nya or your command!```` ```/action first```")
			embed_obj.add_field(name = "meow or second", value = "```Just say Meow or your command!``` ```/action second```")
			return embed_obj

		elif command == "workact":
			embed_obj = Embed(title = command, description = "Edit or Add our own commands for fun and role-play", colour = colour)
			embed_obj.add_field(name = "Example", value = "```/workact 'command-type' 'input-form'``` ```/workact add Hikka:Hey-Hey:Yo``` ```/workact edit Hikka:Hey-Hey:Yo``` ```/workact delete```")
			embed_obj.add_field(name = "Possible values of command-type", value = "```add``` ```edit``` ```delete```")
			embed_obj.add_field(name = "Possible values of 'input-form'", value = "```nick-prefix:first-action:second-action```")
			return embed_obj

		else:
			embed_obj = Embed(description = "Help information about command '"+command+"' don't find!", colour = colour)
			return embed_obj

async def avatar(message):

	if str(message.content) == "/avatar":
		embed_obj = Embed(description = str(message.author.display_name), colour = message.author.colour)
		embed_obj.set_thumbnail(url = message.author.avatar_url)
		return embed_obj

	else:
		type = "small"
		member = None

		if message.content.split(" ")[1] == "big":
			type = "big"
			member = getMember(message.guild, message.content.replace("/avatar big ", ""))
		else:
			member = getMember(message.guild, message.content.replace("/avatar ", ""))

		if member != None:

			embed_obj = Embed(description = member.display_name, colour = member.colour)

			if type == "small":
				embed_obj.set_thumbnail(url = member.avatar_url)
			else:
				embed_obj.set_image(url = member.avatar_url)

			return embed_obj

		else:
			embed_obj = Embed(description = "Member, "+message.content.replace("/avatar ", "")+", not found!", colour = message.guild.me.colour)
			return embed_obj

async def UserDesu(message):
	member = None

	if message.content == "/userinfo":
		member = message.author
	else:
		member = getMember(message.guild, message.content.replace("/userinfo ", ""))

	strRole = None

	embed_obj = Embed(colour = member.colour)
	embed_obj.set_author(name =  "User information of " + member.display_name, icon_url = message.author.avatar_url)
	embed_obj.add_field(name = "Main Information", value = "```Nick: "+member.display_name+"``` ```User ID: "+str(member.id)+"``` ```Accaunt Created: "+str(member.created_at).split(" ")[0]+"``` ```Join Date: "+str(member.joined_at).split(" ")[0]+"``` ```Color: "+str(member.color)+"``` ```Status: "+str(member.status)+"```")

	Roles = member.roles
	i = len(Roles) - 1
	if len(Roles) != 1:
		strRole = ""
		while i >= 1:
			strRole = strRole + "```" + str(Roles[i]) + "```" #message.guild.get_role(str(Roles[i]).replace("@&", "") )
			i-=1
	else:
		strRole = "```None```"

	embed_obj.add_field(name = "**Roles**: " + str(len(Roles) - 1), value = strRole)
	embed_obj.set_thumbnail(url = member.avatar_url)
	return embed_obj

async def RoleDesu(message):
	role = getRole(message.guild, message.content.split(" ")[1])

	embed_obj = Embed(colour = role.colour)
	embed_obj.add_field(name = "Main Information", value = "```Guild: "+str(role.guild)+"``` ```Place in Hierarchy: "+str(role.position)+"``` ```Can you mention role: "+str(role.mentionable)+"``` ```Color: "+str(role.colour)+"``` ```Is Admin: "+str(role.permissions.administrator)+"``` ```Data of Create: "+str(role.created_at)+"```")

	permissions = power(role.permissions)

	strPerm = ""

	for i in range(len(permissions.pack)):
		strPerm += "```" + permissions.pack[i][0] + ": " + str(permissions.pack[i][1]) + "```"

	embed_obj.add_field(name = "Role's permissions", value = strPerm)

	return embed_obj

