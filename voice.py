import os
import discord
from discord.ext import commands

# Intenty — wystarczą do zarządzania kanałami
intents = discord.Intents.default()
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Konfiguracja VOICE
VOICE_CATEGORY_NAME = "◢◤━━━━━━ VOICE ━━━━━━◥◣"
VOICE_EMOJI = "🔊"
VOICE_SPECS = [
    {"label": "MAX 2", "limit": 2, "count": 3},
    {"label": "MAX 3", "limit": 3, "count": 3},
    {"label": "MAX 4", "limit": 4, "count": 3},
]

@bot.event
async def on_ready():
    print(f"✅ Zalogowano jako {bot.user}")

    guild_id = int(os.getenv("DISCORD_GUILD_ID"))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("❌ Bot nie jest na tym serwerze!")
        return

    # Tworzenie kategorii VOICE, jeśli nie istnieje
    voice_category = discord.utils.get(guild.categories, name=VOICE_CATEGORY_NAME)
    if not voice_category:
        voice_category = await guild.create_category(
            VOICE_CATEGORY_NAME,
            reason="Automatyczne tworzenie kategorii VOICE"
        )

    # Tworzenie kanałów głosowych według specyfikacji
    for spec in VOICE_SPECS:
        desired_name = f"{VOICE_EMOJI} {spec['label']}"
        user_limit = spec["limit"]
        desired_count = spec["count"]

        existing = [ch for ch in voice_category.voice_channels if ch.name == desired_name]

        # Ustaw poprawny limit jeśli trzeba
        for ch in existing:
            if ch.user_limit != user_limit:
                await ch.edit(user_limit=user_limit, reason="Korekta limitu użytkowników")

        # Dodaj brakujące kanały aż do desired_count
        while len(existing) < desired_count:
            new_channel = await guild.create_voice_channel(
                desired_name,
                category=voice_category,
                user_limit=user_limit,
                reason="Automatyczne tworzenie kanału głosowego"
            )
            existing.append(new_channel)

    print("✅ Kategorie i kanały głosowe zostały utworzone/zaktualizowane.")

if __name__ == "__main__":
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    bot.run(TOKEN)
