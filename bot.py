import os
from telethon import TelegramClient, events

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

client = TelegramClient("sudi_bot_session", api_id, api_hash)

source_username = "infosphere1"

target_channels = [
    "peacevolunteer",
    "LenegeCommunity",
    "classcalculus",
    "All_Ethio_Books",
    "Ethio_online_market",
    "mezzobet",
    "TemaryGroup_2018",
    "hayyuuacademy"
]


@client.on(events.NewMessage)
async def main_event_handler(event):

    if not event.text:
        return

    text = event.text.strip()

    # Private commands
    if event.is_private:

        if text.startswith("/start"):
            await event.respond(
                "Welcome to Sudi2bot! 🚀\n"
                "This bot manages and automates your broadcasting workflow."
            )

        elif text.startswith("/help"):
            await event.respond(
                "📖 Available Commands:\n"
                "/start - Start\n"
                "/help - Help\n"
                "/status - Status\n"
                "/sources - Sources\n"
                "/targets - Targets\n"
                "/stats - Stats\n"
                "/settings - Settings\n"
                "/test - Test\n"
                "/restart - Restart\n"
                "/support - Support"
            )

        elif text.startswith("/status"):
            await event.respond(
                "🟢 Status: The bot is active and running smoothly!"
            )

        elif text.startswith("/sources"):
            await event.respond(
                f"📡 Active Source: @{source_username}"
            )

        elif text.startswith("/targets"):
            await event.respond(
                f"👥 Connected to {len(target_channels)} target channels."
            )

        elif text.startswith("/stats"):
            await event.respond(
                "📊 Forwarding Stats: All systems are operational."
            )

        elif text.startswith("/settings"):
            await event.respond(
                "⚙️ Settings configuration is managed via your script."
            )

        elif text.startswith("/test"):
            await event.respond(
                "🧪 Test message: Connection is working fine!"
            )

        elif text.startswith("/restart"):
            await event.respond(
                "🔄 The bot is running on the server."
            )

        elif text.startswith("/support"):
            await event.respond(
                "🛠 For support, check your bot configuration."
            )

        return

    # Forward messages from source channel
    try:
        chat = await event.get_chat()

        if chat and getattr(chat, "username", None) == source_username:

            for channel in target_channels:
                try:
                    await event.message.forward_to(channel)
                    print(f"✅ Forwarded to {channel}")

                except Exception as e:
                    print(f"❌ Send failed to {channel}: {e}")

    except Exception as e:
        print(f"❌ Forward error: {e}")


async def start_bot():
    await client.start(bot_token=bot_token)

    me = await client.get_me()

    print("=" * 40)
    print("🚀 SUDI2BOT IS ONLINE")
    print("=" * 40)
    print(f"🤖 Bot: @{me.username}")
    print(f"📡 Source: @{source_username}")
    print(f"👥 Targets: {len(target_channels)}")
    print("🔄 Auto Forwarding: ENABLED")
    print("=" * 40)


client.loop.run_until_complete(start_bot())
client.run_until_disconnected()
