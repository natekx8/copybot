import os
import discord
from discord.ext import commands

# Włącz wymagane intenty
intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Definicja ról: nazwa, emoji, kolor
ROLES = [
    {"name": "Bots", "emoji": "🤖", "color": discord.Color.light_grey()},  # nowa rola na górze
    {"name": "Owner", "emoji": "👑", "color": discord.Color.dark_red()},
    {"name": "CEO", "emoji": "🏛️", "color": discord.Color.red()},
    {"name": "Admin", "emoji": "🛡️", "color": discord.Color.orange()},
    {"name": "Mod", "emoji": "🔧", "color": discord.Color.gold()},
    {"name": "Investor", "emoji": "💵", "color": discord.Color.green()},
    {"name": "Vip", "emoji": "🌟", "color": discord.Color.purple()},
    {"name": "Server Booster", "emoji": "🚀", "color": discord.Color.blue()},
    {"name": "Only Main Rooster", "emoji": "🥇", "color": discord.Color.teal()},
    {"name": "Only Academy", "emoji": "🎓", "color": discord.Color.cyan()},
    {"name": "Only Future", "emoji": "🔮", "color": discord.Color.green()},
    {"name": "Coach", "emoji": "🏅", "color": discord.Color.dark_gold()},
    {"name": "Only Community", "emoji": "👥", "color": discord.Color.light_grey()},
    {"name": "Verified", "emoji": "✅", "color": discord.Color.lighter_grey()},
    {"name": "Unverified", "emoji": "❌", "color": discord.Color.default()},
    {"name": "Bots", "emoji": "🤖", "color": discord.Color.light_grey()}  # duplikat na samym dole
]

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

    # Pobierz ID serwera z sekretnych zmiennych
    guild_id = int(os.getenv("DISCORD_GUILD_ID"))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("❌ Bot nie jest na tym serwerze!")
        return

    # Tworzenie ról
    for role_info in ROLES:
        role_display_name = f"{role_info['emoji']}・{role_info['name']}"
        existing_role = discord.utils.get(guild.roles, name=role_display_name)
        if not existing_role:
            await guild.create_role(name=role_display_name, color=role_info['color'])
            print(f"✅ Utworzono rolę: {role_display_name}")
        else:
            print(f"⚠️ Rola już istnieje: {role_display_name}")

    print("✅ Wszystkie role zostały utworzone lub już istnieją.")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    bot.run(TOKEN)
