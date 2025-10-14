import discord
from discord import app_commands
from discord.ext import commands
import aiohttp
import random
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
INTENTS = discord.Intents.default()


bot = commands.Bot(command_prefix="/", intents=INTENTS)
tree = bot.tree


events = [
    {"name": "Code Cafe", "date": "Oct 15, 2025"},
    {"name": "Code Cafe, again", "date": "Oct 22, 2025"},
    {"name": "Cant think of anything other than Code Cafe", "date": "Oct 29, 2025"},
]

weekly_challenge = {
    "title": "Make something new!",
    "desc": "Come up with a software to bring in new members."
}

quotes = [
    "If you want another coffee you can make it yourself.",
    "Programmers turn caffeine into code. Not me though, I just make it.",
    "Stay grounded and keep coding. Ha",
    "Life begins after coffee. I'll just keep making it i suppose.",
    "You got this — just one more bug to fix! When will you fix mine though.",
    "Drink coffee. Because rewriting the same function for the third time at 2am builds character.",
    "Behind every successful commit is a developer powered by equal parts caffeine and regret.",
    "Coffee: because your code won’t compile without emotional support.",
    "One cup of coffee away from replacing your app with a handwritten letter and a carrier pigeon.",
    "Coffee doesn't solve problems, but it makes you care slightly less that your API call just lit itself on fire.",
    "Without coffee, there is chaos. With coffee… still chaos, but at least you're alert while it burns.",
]




@tree.command(name="help", description="Displays the list of available commands and usage.")
async def help_command(interaction: discord.Interaction):
    embed = discord.Embed(
        title="☕ Code Café Bot Commands",
        description="Here's what I can do:",
    )
    embed.add_field(name="/help", value="List all commands.", inline=False)
    embed.add_field(name="/events", value="View upcoming Code Café events.", inline=False)
    embed.add_field(name="/challenge", value="See the current coding challenge.", inline=False)
    embed.add_field(name="/profile", value="View your Code Café profile stats.", inline=False)
    embed.add_field(name="/github", value="Get GitHub repo info.", inline=False)
    embed.add_field(name="/quote", value="Get a random motivational or coffee quote.", inline=False)
    await interaction.response.send_message(embed=embed)


@tree.command(name="events", description="Lists upcoming Code Café events.")
async def events_command(interaction: discord.Interaction):
    embed = discord.Embed(title="☕ Upcoming Code Café Events", color=discord.Color.orange())
    for event in events:
        embed.add_field(name=event["name"], value=event["date"], inline=False)
    await interaction.response.send_message(embed=embed)


@tree.command(name="challenge", description="Shows the current weekly coding challenge.")
async def challenge_command(interaction: discord.Interaction):
    embed = discord.Embed(title=f"🏆 {weekly_challenge['title']}", description=weekly_challenge['desc'], color=discord.Color.gold())
    await interaction.response.send_message(embed=embed)


@tree.command(name="profile", description="View your Code Café stats and activity.")
async def profile_command(interaction: discord.Interaction):
    user = interaction.user
    embed = discord.Embed(title=f"👤 {user.name}'s Profile", color=discord.Color.blue())
    embed.add_field(name="XP", value=str(random.randint(100, 5000)), inline=True)
    embed.add_field(name="Challenges Completed", value=str(random.randint(1, 50)), inline=True)
    embed.add_field(name="Favorite Drink", value=random.choice(["Latte", "Espresso", "Cappuccino", "Cold Brew"]), inline=True)
    embed.set_thumbnail(url=user.avatar.url if user.avatar else None)
    await interaction.response.send_message(embed=embed)


@tree.command(name="github", description="Fetch GitHub repo details.")
async def github_command(interaction: discord.Interaction):
        await interaction.response.send_message(f"https://github.com/Staffs-Code-Cafe/Code-Cafe-Coffee-Machine")


@tree.command(name="quote", description="Get a random coffee quote or motivational message.")
async def quote_command(interaction: discord.Interaction):
    quote = random.choice(quotes)
    await interaction.response.send_message(f"☕ {quote}")



@bot.event
async def on_ready():
    await tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Slash commands synced!")

bot.run(TOKEN)
