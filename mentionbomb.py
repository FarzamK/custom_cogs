import discord
from discord.ext import commands


class MentionBomb:

	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def mbomb(self, ctx):
		await ctx.message.delete()

		messages = []
		msg = ""

		for member in ctx.message.channel.members:
			if len(msg) >= 1900:
				messages.append(msg)
				msg = ""

			msg += member.mention + "\n"

		if len(msg) >= 1:
			messages.append(msg)

		for message in messages:
			sent = await ctx.send(message)
			await sent.delete()
			

def setup(bot):
	bot.add_cog(MentionBomb(bot))
