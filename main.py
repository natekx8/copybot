import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

categories_channels = {
    "INFORMATION": ["🛬・welcome", "📯・announcements", "🌐・teamˑsocials", "📛・rules", "🤖・selfrole", "🔮・boosts", "📰・socialˑnews", "✍・dolaczˑdoˑadministracji", "🎫・modmail"],
    "PUBLIC": ["📄・chat", "🎮・l4p", "📸・media", "🎧・setup", "🔧・commands", "🏅・tops", "🤔・suggestions"],
    "TEAM": ["👥・players"],
    "COMMUNITY": ["💪🏻・zone-wars"],
    "ECONOMY": ["💸・market", "🧩・economyˑcommands", "📗・roles", "🛒・shop"]
}

@bot.event
async def on_ready():
    print(f'Bot online: {bot.user}')
    guild = bot.guilds[0]  # Pierwszy serwer, gdzie jest bot
    for category_name, channels in categories_channels.items():
        category = await guild.create_category(category_name)
        for channel_name in channels:
            await guild.create_text_channel(channel_name, category=category)
    print("Kategorie i kanały utworzone!")

bot.run("MTQwMTU3MDgyNzY5ODE3NjA4MQ.G7yUHP.4UTAD8_ysj2mR1_o1SQQBbXvKrmriEYxGMtiQw")
