from keep_alive import keep_alive
keep_alive()

# Aqui entra o código do teu bot
# Exemplo com Discord:
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Mantém o bot online no Replit
keep_alive()

# Token do teu bot
bot.run("MTM1OTMwOTkxNDg3ODUwOTA3Ng.G1XnGx.jj2m6KIHHtUZ-5I-dr-0BGEtuWKwlSU7k4nhkI")
