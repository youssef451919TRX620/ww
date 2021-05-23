from discord.ext import commands
import discord
import os
import keep_alive
keep_alive.keep_alive()

intents = discord.Intents.default()
mention = discord.AllowedMentions(everyone=False, users=True, roles=False)
bot = commands.Bot(command_prefix="/", intents = intents, allowed_mentions=mention)


bot.load_extension("cogs.nqn")


if __name__ == "__main__":
	bot.run(os.environ["token"])
