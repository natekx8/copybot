import os
import discord
from discord.ext import commands

# Włącz wymagane intenty
intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Struktura kanałów
CHANNEL_STRUCTURE = {
    "Przeglądaj kanały": ["✅・verification"],

    "◢◤━━━  information ━━━◥◣": [
        "🛬・welcome", "📯・announcements", "🌐・teamˑsocials",
        "📛・rules", "🤖・selfrole", "🔮・boosts", "📰・socialˑnews",
        "✍・dolaczˑdoˑadministracji", "🎫・modmail"
    ],

    "◢◤━━━━━━ public ━━━━━━◥◣": [
        "📄・chat", "🎮・l4p", "📸・media", "🎧・setup",
        "🔧・commands", "🏅・tops", "🤔・suggestions"
    ],

    "◢◤━━━━━━━ TEAM  ━━━━━━━◥◣": [
        "👥・players"
    ],

    "◢◤━━━━━ Community ━━━━━◥◣": [
        "💪🏻・zone-wars"
    ],

    "◢◤━━━━━ economy ━━━━━◥◣": [
        "💸・market", "🧩・economyˑcommands", "📗・roles", "🛒・shop"
    ]
}

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

    # Pobierz ID serwera z sekretnych zmiennych
    guild_id = int(os.getenv("DISCORD_GUILD_ID"))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("❌ Bot nie jest na tym serwerze!")
        return

    # Tworzenie kategorii i kanałów
    for category_name, channels in CHANNEL_STRUCTURE.items():
        category = discord.utils.get(guild.categories, name=category_name)
        if not category:
            category = await guild.create_category(category_name)

        for channel_name in channels:
            if not discord.utils.get(category.channels, name=channel_name):
                await guild.create_text_channel(channel_name, category=category)

    print("✅ Wszystkie kategorie i kanały zostały utworzone.")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    bot.run(TOKEN)
