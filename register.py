from telegram.ext import *
import sqlite3
conn = sqlite3.connect('Banking.db', check_same_thread=False)
c= conn.cursor()

PW=0,1
async def register(update, context):
    uid = update.message.chat_id
    name=""
    if update.message.chat.type in ["group", "supergroup"]:
        name=update.message.chat.title
    else:
        last = update.message.chat.last_name
        first= update.message.chat.first_name
        name= last+" "+ first
    c.execute("SELECT uid FROM fbank1 WHERE uid={}".format(uid))
    find=c.fetchone()
    if find is None:
        c.execute("INSERT INTO fbank1 (uid,last,num) VALUES (?, ?, ?)",(uid,name,1000))
        await update.message.reply_text("Please input the password you want to create")
        conn.commit()
        return PW
    else:
        await update.message.reply_text("Already registered")
        ConversationHandler.END

async def create_pw(update, context):
    uid=update.message.chat_id
    passw=update.message.text
    hpw=hash(passw)
    c.execute("""UPDATE fbank1
                 SET password={}
                 WHERE uid= {}""".format(hpw,uid))
    conn.commit()
    await update.message.reply_text("Register completed")
    return ConversationHandler.END

async def change_pw_command(update, context):
    pass