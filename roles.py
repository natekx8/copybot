import os
import discord
from discord.ext import commands

# Włącz wymagane intenty
intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Definicja ról: nazwa, emoji, kolor w hex
ROLES = [
    {"name": "Bots", "emoji": "🤖", "color": 0xA0A0A0},             # szary
    {"name": "Owner", "emoji": "👑", "color": 0x8B0000},            # ciemnoczerwony
    {"name": "CEO", "emoji": "🏛️", "color": 0xFF0000},             # czerwony
    {"name": "Admin", "emoji": "🛡️", "color": 0xFFA500},           # pomarańczowy
    {"name": "Mod", "emoji": "🔧", "color": 0xFFD700},             # złoty
    {"name": "Investor", "emoji": "💵", "color": 0x008000},        # zielony
    {"name": "Vip", "emoji": "🌟", "color": 0x800080},             # fioletowy
    {"name": "Server Booster", "emoji": "🚀", "color": 0x0000FF},  # niebieski
    {"name": "Only Main Rooster", "emoji": "🥇", "color": 0x008080},# ciemnoturkusowy
    {"name": "Only Academy", "emoji": "🎓", "color": 0x00FFFF},    # turkusowy
    {"name": "Only Future", "emoji": "🔮", "color": 0x00FF00},     # jasnozielony
    {"name": "Coach", "emoji": "🏅", "color": 0xB8860B},            # ciemnozłoty
    {"name": "Only Community", "emoji": "👥", "color": 0xD3D3D3},  # jasnoszary
    {"name": "Verified", "emoji": "✅", "color": 0xADD8E6},        # jasnoniebieski
    {"name": "Unverified", "emoji": "❌", "color": 0xFFFFFF},      # biały
    {"name": "Bots", "emoji": "🤖", "color": 0xA0A0A0}             # duplikat na dole
]

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

    guild_id = int(os.getenv("DISCORD_GUILD_ID"))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("❌ Bot nie jest na tym serwerze!")
        return

    for role_info in ROLES:
        role_display_name = f"{role_info['emoji']}・{role_info['name']}"
        existing_role = discord.utils.get(guild.roles, name=role_display_name)
        if not existing_role:
            await guild.create_role(name=role_display_name, color=discord.Color(role_info['color']))
            print(f"✅ Utworzono rolę: {role_display_name}")
        else:
            print(f"⚠️ Rola już istnieje: {role_display_name}")

    print("✅ Wszystkie role zostały utworzone lub już istnieją.")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    bot.run(TOKEN)
