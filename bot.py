import logging
import os
import random
import sys

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enabling logging
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# Getting mode, so we could define run function for local and Heroku setup
mode = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")
if mode == "dev":
    def run(updater):
        updater.start_polling()
elif mode == "prod":
    def run(updater):
        PORT = int(os.environ.get("PORT", "8443"))
        HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
        # Code from https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#heroku
        updater.start_webhook(listen="0.0.0.0",
                              port=PORT,
                              url_path=TOKEN)
        updater.bot.set_webhook("https://{}.herokuapp.com/{}".format(HEROKU_APP_NAME, TOKEN))
 
else:
    logger.error("No MODE specified!")
    sys.exit(1)

    # Command Handler
def start_handler(bot, update):
    # Creating a handler-function for /start command 
    logger.info("User {} started bot".format(update.effective_user["id"]))
    update.message.reply_text("HELLO！歡迎來到Adelaide 2020 開學Group。我係你既AI機器人Alpha")

def introduction_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} introduction bot".format(update.effective_user["id"]))
    update.message.reply_text("ADMIN的話：希望大家可以係adelaide建立一個屬於香港人既community。")

def helpEdit_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} helpedit bot".format(update.effective_user["id"]))
    update.message.reply_text("https://docs.google.com/spreadsheets/d/1mVco-1T4U_U-0jRJ3A2riHlhAh-wnsx5IWHoyNkBt-w/edit?usp=sharing")

def phoneNetwork_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} phonenetwork bot".format(update.effective_user["id"]))
    update.message.reply_text("Telstra is recommended;\nOptus is OK;\nVodafone is not recommended")
def carFaq1_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} carFaq1 bot".format(update.effective_user["id"]))
    update.message.reply_text("首先要去SA Service考左L牌\n25歲以下要hold L牌一年先可以考P1\n25歲或以上就半年\n拎左L牌就可以揾full license driver簽薄儲75個鐘\n儲夠就可以考P1")

def bankingFaq1_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} bankingfaq1 bot".format(update.effective_user["id"]))
    update.message.reply_text("可以到澳洲後準備好學生證,passport同地址證明就可以walkin銀行開戶\nCBA ANZ HSBC NAB 各有各好但學生黎講分別不大")

def bankingFaq2_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} bankingfaq2 bot".format(update.effective_user["id"]))
    update.message.reply_text("開銀行戶口可以唔交tfn\n 但無tfn銀行會扣你47% of interest yield 比ato\n 要自己年底係ATO claim番\n tfn可以係開戶口之係online banking加返")

def fxFaq１_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} fxfaq1 bot".format(update.effective_user["id"]))
    update.message.reply_text("我個人建議用instarem:https://www.instarem.com/invite/8htd9Q. \n由你香港銀行轉錢到公司香港戶口，公司由佢地澳洲戶口轉錢到你澳洲戶口。\n𣾀率為即時Bloomberg rate with zero spread;手續費低0.4%;轉錢最快可以一日到帳\n教學可以參考https://www.finder.com/hk/instarem-money-transfer-ch")


    # Alarm Timer 
def alarm(context):
    """Send the alarm message."""
    job = context.job
    context.bot.send_message(job.context, text='起身啦!')


def set_timer(update, context):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        # Add job to queue and stop current one if there is a timer already
        if 'job' in context.job_queue.jobs:
            old_job = 'job'
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(alarm, due, context=chat_id)
        context.job_queue.jobs = context.job_queue.jobs + new_job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')


def unset(update, context):
    """Remove the job if the user changed their mind."""
    if 'job' not in job_queue.jobs:
        update.message.reply_text('You have no active timer')
        return

    job = context.job_queue.jobs
    job.schedule_removal()
    del context.job_queue.jobs

    update.message.reply_text('Timer successfully unset!')




    # Message Handler
def reply_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} reply bot".format(update.effective_user["id"]))
    update.message.reply_text(update.message.text)

def replysticker_handler(bot, update):
    # Creating a handler-function for /introduction command
    logger.info("User {} replysticker bot".format(update.effective_user["id"]))
    update.message.reply_sticker("👍🏻")

    # error handler
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    logger.info("Starting bot")
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Command Handler
    dispatcher.add_handler(CommandHandler("start", start_handler))
    dispatcher.add_handler(CommandHandler("introduction", introduction_handler))
    dispatcher.add_handler(CommandHandler("helpedit", helpEdit_handler))
    dispatcher.add_handler(CommandHandler("phonenetwork", phoneNetwork_handler))
    dispatcher.add_handler(CommandHandler("carfaq1", carFaq1_handler))
    dispatcher.add_handler(CommandHandler("bankingfaq1", bankingFaq1_handler))
    dispatcher.add_handler(CommandHandler("bankingfaq2", bankingFaq2_handler))
    dispatcher.add_handler(CommandHandler("fxfaq1", fxFaq1_handler))

    dispatcher.add_handler(CommandHandler("set", set_timer,
                                            pass_args=True,
                                            pass_chat_data=True))
    dispatcher.add_handler(CommandHandler("unset", unset))

    # Message Handler
    dispatcher.add_handler(MessageHandler(Filters.sticker, replysticker_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
    
    # log all errors
    dispatcher.add_error_handler(error)

    run(updater)    

if __name__ == '__main__':
    main()