
import discord
from discord.ext import commands
print(discord.__version__)

import settings
from utils import log, get_data, upd_data
from cmds.stuff.birthday import Birthday 

intents = discord.Intents.all()

bot = commands.Bot(
	command_prefix=commands.when_mentioned_or(settings.BOT_PREFIX),
	case_insensitive=True,
	help_command=None,
	intents=intents,
	strip_after_prefix=True
)
bot.description = "" # not synced



@bot.event
async def on_ready():
	log("INFO", f"Logged in as {bot.user}")
	for ext in settings.extensions:
		await bot.load_extension(ext)
		log("INFO", f"{ext} loaded ")

	Bd = Birthday(bot)
	Bd.birthdays_loop.start()

	print("SINF illégal family bot online\n")

@bot.command()
async def ping(ctx:commands.Context):
	await ctx.send(f"🏓 **PONG!** je t'ai renvoyé la balle en `{round(bot.latency*1000)}`_ms_ !")

bot.run(settings.DISCORD_API_TOKEN)