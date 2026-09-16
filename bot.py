import os
from telethon import TelegramClient, events

# እነዚህን በ Hosting ዳሽቦርድዎ (Environment Variables) ላይ ማስገባት ይችላሉ
api_id = int(os.environ.get("API_ID", 0))  # የእርስዎን API_ID ያስገቡ
api_hash = os.environ.get("API_HASH", "")  # የእርስዎን API_HASH ያስገቡ
bot_token = os.environ.get("BOT_TOKEN", "")  # የእርስዎን BOT_TOKEN ያስገቡ

client = TelegramClient("sudi_bot_session", api_id, api_hash)

# 1. የእርስዎ ቻናል (ምንጭ) - ከሊንኩ የመጨረሻ ክፍል የተወሰደ
source_username = "infosphere1" 

# 2. የእርስዎ ቡድኖች (መድረሻዎች) - ከሊንኮቹ የመጨረሻ ክፍል የተወሰዱ
target_channels = [
    "forwardtobots",
    "Adimngp",
    "mygroupSudi",
    "sudiforwarding"
]

@client.on(events.NewMessage)
async def main_event_handler(event):
    # የግል ትዕዛዞች (Private Commands)
    if event.is_private:
        text = event.text.strip() if event.text else ""

        if text.startswith("/start"):
            await event.respond("Welcome to Sudi2bot! 🚀\nThis bot manages and automates your broadcasting workflow.")
        elif text.startswith("/help"):
            await event.respond("📖 Available Commands:\n/start\n/help\n/status\n/sources\n/targets\n/stats\n/settings\n/test\n/restart\n/support")
        elif text.startswith("/status"):
            await event.respond("🟢 Status: The bot is active and running smoothly!")
        elif text.startswith("/sources"):
            await event.respond(f"📡 Active Source: @{source_username}")
        elif text.startswith("/targets"):
            await event.respond(f"👥 Connected to {len(target_channels)} target groups.")
        elif text.startswith("/stats"):
            await event.respond("📊 Forwarding Stats: All systems are operational.")
        elif text.startswith("/settings"):
            await event.respond("⚙️ Settings configuration is managed via your script.")
        elif text.startswith("/test"):
            await event.respond("🧪 Test message: Connection is working fine!")
        elif text.startswith("/restart"):
            await event.respond("🔄 The bot is running on the server.")
        elif text.startswith("/support"):
            await event.respond("🛠 For support, check your bot configuration.")
        return

    # 3. ከቻናል ወደ ቡድኖች ማስተላለፍ (Forwarding Logic)
    try:
        chat = await event.get_chat()
        
        # መልዕክቱ ከእርስዎ ቻናል መሆኑን ማረጋገጥ
        if chat and getattr(chat, "username", None) == source_username:
            
            # ፎቶ፣ ቪዲዮ፣ ፋይል ወይም ጽሑፍ መሆኑን ሳይለይ ያስተላልፋል
            for channel in target_channels:
                try:
                    # ወደ ቡድኑ ለመላክ የሚሞክር
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
    print(f"👥 Targets: {len(target_channels)} groups")
    print("🔄 Auto Forwarding: ENABLED")
    print("=" * 40)

client.loop.run_until_complete(start_bot())
client.run_until_disconnected()
