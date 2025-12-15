from telegram.ext import Application, CommandHandler, CallbackQueryHandler
import os
import asyncio
from dotenv import load_dotenv
from methods import To_Do_List 
from db import db
import signal
import sys

# Store application, and the event loop
application = None
loop = None

# --- Signal Handler Function ---
def stop_bot(signum, frame):
    """Gracefully stops the bot application using threadsafe coroutine execution."""
    global application, loop
    print("\n[INFO] Ctrl+C detected. Initiating clean shutdown...")
    
    if application and loop:
        try:
            # Schedule the application.stop() coroutine to run on the main event loop.
            future = asyncio.run_coroutine_threadsafe(application.stop(), loop)
            future.result(5) # Wait up to 5 seconds for the shutdown to complete
            
        except asyncio.TimeoutError:
            print("[WARN] Application stop timed out, forcing exit.")
        except Exception as e:
            print(f"[ERROR] Error during stop: {e}")
            
    print("[INFO] Bot application stopped.")
    # Exit the program cleanly
    sys.exit(0)
# -------------------------------

def main():
    global application, loop
    try:
        load_dotenv()
        BOT_TOKEN = os.getenv("BOT_TOKEN")
        
        # 1. Initialize database setup
        asyncio.run(db.init_db())
        
        # 2. Build the application and store it globally
        application = Application.builder().token(BOT_TOKEN).build()
        
        # 3. Register command handlers (Your existing handlers)
        application.add_handler(CommandHandler("start", To_Do_List.start))
        application.add_handler(CommandHandler("add", To_Do_List.add))
        application.add_handler(CommandHandler("help", To_Do_List.help))
        application.add_handler(CommandHandler("list", To_Do_List.list))
        application.add_handler(CommandHandler("done", To_Do_List.done))
        application.add_handler(CommandHandler("clear", To_Do_List.clear))
        application.add_handler(CallbackQueryHandler(To_Do_List.clear_callback, pattern="clear_"))
        application.add_handler(CallbackQueryHandler(To_Do_List.done_callback, pattern="^done:"))
        
        # 4. Get the event loop BEFORE polling starts. In Linux, this usually works reliably.
        loop = asyncio.get_event_loop()
        
        # 5. Set up the signal handler
        signal.signal(signal.SIGINT, stop_bot)
        
        # 6. Start polling
        print("[INFO] Bot is running. Press Ctrl+C to stop.")
        application.run_polling()
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # No Windows-specific policy needed here.
    main()