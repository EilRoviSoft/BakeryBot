import discord

def getChannel(guild, elName):
	cs = guild.channels
	for eve in cs:
		if eve.name == elName:
			return eve

def getMember(guild, elName):
	cs = guild.members
	for eve in cs:
		if eve.name == elName:
			return eve

def getRole(guild, elRole):
	cs = guild.roles
	for eve in cs:
		if eve.name == elRole:
			return eve