import os
import discord
from discord.ext import commands

# Włącz wymagane intenty
intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Lista ról w kolejności od najwyższych uprawnień do najniższych
ROLES = [
    "Owner",
    "CEO",
    "Admin",
    "Mod",
    "Investor",
    "Vip",
    "Server Booster",
    "Only Main Rooster",
    "Only Academy",
    "Only Future",
    "Coach",
    "Only Community",
    "Verified",
    "Unverified"
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
    for role_name in ROLES:
        role_display_name = f"・{role_name}"  # dodaj znak ・ na początku
        existing_role = discord.utils.get(guild.roles, name=role_display_name)
        if not existing_role:
            await guild.create_role(name=role_display_name)
            print(f"✅ Utworzono rolę: {role_display_name}")
        else:
            print(f"⚠️ Rola już istnieje: {role_display_name}")

    print("✅ Wszystkie role zostały utworzone lub już istnieją.")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    bot.run(TOKEN)
