import discord
from discord.ext import commands
import os

# =======================
# Twój token bota
# =======================
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")  # dodamy go w Replit jako Secret

# ID Twojego serwera
GUILD_ID = 123456789012345678  # <- wklej ID swojego serwera

# Struktura kategorii i kanałów
CHANNELS = {
    "✅・verification": [],
    "◢◤━━━  INFORMATION ━━━◥◣": [
        "🛬・welcome",
        "📯・announcements",
        "🌐・teamˑsocials",
        "📛・rules",
        "🤖・selfrole",
        "🔮・boosts",
        "📰・socialˑnews",
        "✍・dolaczˑdoˑadministracji",
        "🎫・modmail"
    ],
    "◢◤━━━━━━ PUBLIC ━━━━━━◥◣": [
        "📄・chat",
        "🎮・l4p",
        "📸・media",
        "🎧・setup",
        "🔧・commands",
        "🏅・tops",
        "🤔・suggestions"
    ],
    "◢◤━━━━━━━ TEAM  ━━━━━━━◥◣": ["👥・players"],
    "◢◤━━━━━ COMMUNITY ━━━━━◥◣": ["💪🏻・zone-wars"],
    "◢◤━━━━━ ECONOMY ━━━━━◥◣": [
        "💸・market",
        "🧩・economyˑcommands",
        "📗・roles",
        "🛒・shop"
    ]
}

# =======================
intents = discord.Intents.default()
intents.guilds = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user}')
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        print("Nie znaleziono serwera!")
        return

    for category_name, channels in CHANNELS.items():
        # sprawdzamy czy kategoria już istnieje
        category = discord.utils.get(guild.categories, name=category_name)
        if not category:
            category = await guild.create_category(category_name)
            print(f"Utworzono kategorię: {category_name}")

        for ch_name in channels:
            # sprawdzamy, czy kanał już istnieje
            existing = discord.utils.get(category.channels, name=ch_name)
            if not existing:
                await guild.create_text_channel(ch_name, category=category)
                print(f"  Utworzono kanał: {ch_name}")

    print("Wszystkie kanały utworzone!")
    await bot.close()  # zamykamy bota po utworzeniu wszystkich kanałów

bot.run(TOKEN)
