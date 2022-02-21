from cgitb import html
from html.parser import HTMLParser
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import time as t
from telegram import ParseMode
from duckduckgo_search import ddg
from covid import Covid
from requests import get
import json
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN")
updater = Updater(BOT_TOKEN,
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "<b>Hemlo Gay! I'm Srinand's Personal Bot. FUCK OFF WEN?</b>",parse_mode='html')

def help(update: Update, context: CallbackContext):
    update.message.reply_text("<b>Available Commands: \
        \n/start :\n\t\t\t\tUsage :To Start and Get a Brief Description of the Bot \
        \n\n/help :\n\t\t\t\tUsage :To Get Help \
        \n\n/echo :\n\t\t\t\tSyntax: /echo MESSAGE \n\t\t\t\tUsage :To Echo your Messages \
        \n\n/spam :\n\t\t\t\tSyntax: /spam MESSAGE \n\t\t\t\tUsage :To Spam \
        \n\n/rom :\n\t\t\t\tSyntax: /rom ROM_NAME\n\t\t\t\tUsage :To Get Latest ROM post Of The Specified ROM. \
        \n\n/google :\n\t\t\t\tSyntax: /google SEARCH_KEYWORD\n\t\t\t\tUsage :To Google Stuff. \
        \n\n/covid :\n\t\t\t\tSyntax: /covid COUNTRY_NAME\n\t\t\t\tUsage :To Get COVID-19 Stats for COUNTRY_NAME., \
        \n\n/ofox :\n\t\t\t\tSyntax: /ofox DEVICE_NAME\n\t\t\t\tUsage :To Get Latest OrangeFox Recovery for Specified Device. \
        \n\n/magisk :\n\t\t\t\tUsage :To Get Latest Magisk Zip/Apk.</b>", \
            parse_mode='html')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    final = ""

    orgMessageText = update.message.text
    messageText = getFinalWord(orgMessageText)
    
    for words in messageText:
        final = final + words + ""

    if final == "":
        update.message.reply_text("<b>FUCK OFF! GIVE A MESSAGE FFS!</b>",parse_mode='html')
    else:
        update.message.reply_text(final)

def spam(update: Update, context: CallbackContext) -> None:
    """Spam Multiple Messages"""

    no = 1
    final = ""
    orgMessageText = update.message.text
    messageText = getFinalWord(orgMessageText)
    
    for words in messageText:
        final = final + words + ""
 
    if final=="":
        update.message.reply_text("FUCK OFF! GIVE A MESSAGE FFS!")

    while no<21:
        context.bot.send_message(chat_id=update.effective_chat.id, text=final)  
        no+=1
    else:
        update.effective_chat.send_message("STOPPING SPAM!!\nReason: Spam Count Over 20!")

def rom(update: Update, context: CallbackContext) -> None:
    """Used For Getting ROM Posts"""
    messageText = update.message.text
    romName = getFinalWord(messageText)

    if update.effective_chat.id == -1001366493089:
        if romName.lower() == "arrow" or romName.lower() == "arru" or romName.lower() == "arrowos":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id ="@srinandschannel",message_id="230")
        elif romName in roms:
            update.message.reply_text("<b>DONT ASK HERE FFS.</b> I <b>DONT</b> Maintain <b>{}</b>. Look Somewhere Else For Its Link.\nK THX".format(romName),parse_mode='html')
        else:
            update.message.reply_text("<b>FUCK OFF! IS THERE EVEN A ROM WITH THE NAME: {}</b>".format(romName),parse_mode='html')

    elif update.effective_chat.id == -1001382651252:
        if romName.lower() == "elixir" or romName.lower() == "project-elixir":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1416")
        elif romName in roms:
            update.message.reply_text("<b>DONT ASK HERE FFS.</b> I <b>DONT</b> Maintain <b>{}</b>. Look Somewhere Else For Its Link.\nK THX".format(romName),parse_mode='html')
        else:
            update.message.reply_text("<b>FUCK OFF! IS THERE EVEN A ROM WITH THE NAME: {}</b>".format(romName),parse_mode='html')

    else:
        if romName.lower() == "arrow" or romName.lower() == "arru" or romName.lower() == "arrowos":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id=from_chat_id,message_id="1406")
        elif romName.lower() == "octavi" or romName.lower() == "octavios":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1410")
        elif romName.lower() == "pixelextended" or romName.lower() == "pex":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1277")
        elif romName.lower() == "pixelexperience" or romName.lower() == "pe":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1407")
        elif romName.lower() == "derpfest" or romName.lower() == "derp":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1409")            
        elif romName.lower() == "superioros" or romName.lower() == "superior":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1405")
        elif romName.lower() == "elixir" or romName.lower() == "project-elixir":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1416")
        elif romName.lower() == "aex" or romName.lower() == "aospextended":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1401")
        elif romName.lower() == "ancient" or romName.lower() == "ancientos":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1400")
        elif romName.lower() == "flos" or romName.lower() == "forklineageos":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1399")
        elif romName.lower() == "nusantara" or romName.lower() == "nusantaraos" :
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1398")
        elif romName.lower() == "cherish" or romName.lower() == "cherishos" :
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id ="@kernel4vincechat",message_id="326787")
        elif romName.lower() == "radiant" or romName.lower() == "project radiant" or romName.lower() == "pr":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1418")
        elif romName.lower() == "cipheros" or romName.lower() == "cipher":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1414")
        elif romName.lower() == "crdroid":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1413")
        elif romName.lower() == "havocos" or romName.lower() == "havoc":
            updater.bot.forward_message(chat_id=update.effective_chat.id, from_chat_id =from_chat_id,message_id="1412")
        elif romName.lower() in roms:
            update.message.reply_text("<b>Will Be Added Later: {}</b>".format(romName),parse_mode='html')
        else:
            update.message.reply_text("<b>FUCK OFF! IS THERE EVEN A ROM WITH THE NAME: {}</b>".format(romName),parse_mode='html')

def google(update: Update, context: CallbackContext) -> None:
    """Used For Googling Stuff"""
    searched = []
    msg = ""
    finalQuery = ""
    givenQuery = update.message.text
    query = getFinalWord(givenQuery)

    if query.lower() == "porn" or query == "":
        update.message.reply_text("<b>FUCK OFF FOR FUCKS SAKE!!</b>",parse_mode='html')


    else:
        update.message.reply_text("<b>Searching on Google!\nPLease wait for 3-4 Seconds.</b>",parse_mode='html')
        rst = ddg(query)
        i = 1
        while i <=5:
            result = rst[i]
            msg += f"{i}: [{result['title']}]({result['href']})\n"
            msg += f"{result['body']}\n\n"
            i += 1
        updater.bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id + 1)
        update.message.reply_text("Found This On The Web for: ***{}*** \n\n{}".format(query,msg),disable_web_page_preview=True,parse_mode='markdown')


def covid(update: Update, context: CallbackContext) -> None:
    def format_integer(number, thousand_separator="."):
        def reverse(string):
            string = "".join(reversed(string))
            return string

        s = reverse(str(number))
        count = 0
        result = ""
        for char in s:
            count = count + 1
            if count % 3 == 0:
                if len(s) == count:
                    result = char + result
                else:
                    result = thousand_separator + char + result
            else:
                result = char + result
        return result

    givenQuery = update.message.text
    country = getFinalWord(givenQuery)
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
        output_text = (
            f"`Confirmed   : {format_integer(country_data['confirmed'])}`\n"
            + f"`Active      : {format_integer(country_data['active'])}`\n"
            + f"`Deaths      : {format_integer(country_data['deaths'])}`\n"
            + f"`Recovered   : {format_integer(country_data['recovered'])}`\n\n"
            + f"`New Cases   : {format_integer(country_data['new_cases'])}`\n"
            + f"`New Deaths  : {format_integer(country_data['new_deaths'])}`\n"
            + f"`Critical    : {format_integer(country_data['critical'])}`\n"
            + f"`Total Tests : {format_integer(country_data['total_tests'])}`\n\n"
            + f"Data provided by [Worldometer](https://www.worldometers.info/coronavirus/country/{country})"
        )
        update.message.reply_text(f"Corona Virus Info in {country}:\n\n{output_text}",parse_mode='markdown',disable_web_page_preview='true')

    except ValueError:
        update.message.reply_text(f"No information found for: {country}!\nCheck your spelling and try again.",parse_mode='markdown',disable_web_page_preview='true')

def ofox(update: Update,context: CallbackContext) -> None:
    """Get Latest OrangeFox Recovery For Specified Device"""

    givenQuery = update.message.text
    device = getFinalWord(givenQuery)
    if device:
        pass

    else:
        update.message.reply_text("`Usage: .ofox <codename>`")
        return

    url = get(f"https://api.orangefox.download/v3/devices/get?codename={device}")
    if url.status_code == 404:
        update.message.reply_text(f"***`Couldn't find OrangeFox Recovery for {device}!`\n***",parse_mode="markdown")
        return

    info = json.loads(url.text)
    if 'url' in info:
        ed = (
          f"***Latest OFOX Recovery for {info['full_name']}:***\n"
          f"[{device}]({info['url']})\n"
          f"Maintainer: {info['maintainer']['name']}"
           )
        update.message.reply_text(ed,parse_mode="markdown",disable_web_page_preview="true")

    else:
        update.message.reply_text("Mmmm... Some issue occured")

def magisk(update: Update, context: CallbackContext) -> None:
    """Get Latest Magisk Zip"""

    magisk_dict = {
        "***Stable***": "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/stable.json",
        "***Beta***": "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/beta.json",
        "***Canary***": "https://raw.githubusercontent.com/topjohnwu/magisk-files/master/canary.json",
    }
    releases = "***Latest Magisk Releases:\n***"
    for name, release_url in magisk_dict.items():
        data = data = get(release_url).json()
        releases += (
            f'{name}: [APK v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | '
            f'[Changelog]({data["magisk"]["note"]})\n'
        )
    update.message.reply_text(releases,parse_mode="markdown",disable_web_page_preview="true")

def getFinalWord(message):
    """Get The Final Message (after removing  /xxxx) """
    j=""
    messageText = message
    finalMesssage = messageText.split()
    finalMesssage.pop(0)

    if len(finalMesssage) == 1:
        return finalMesssage[0]
    else:
        for i in finalMesssage:
            j += i + " "
        return j

def main():
    """Main"""

    global roms
    global from_chat_id

    from_chat_id="@kernel4vince"
    roms = ["octavi","elixir","superior","crdroid","lineageos","pixelextended", \
        "pixelexperience","blissrom","derpfest","fluid","elixir","aex","ancientos" "project radiant" "cipheros" , \
            "flos","nusantara","derp","arru","arrowos","octavios","pex","pe","superior" "pr" "cipher" "orangefox" , \
                "project-elixir","aospextended","ancientos","forklineageos","nusantaraos" "radiant" "ofox" , \
                "los","havoc","cherish","shapeshiftos","shapeshiftos","sakuraos","sakura", \
                    "ssos","havocos","cherish","cherishos","arrow","arru","arrowos" ]

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('echo', echo))
    updater.dispatcher.add_handler(CommandHandler('spam', spam,run_async=True))
    updater.dispatcher.add_handler(CommandHandler('rom',rom))
    updater.dispatcher.add_handler(CommandHandler('google',google))
    updater.dispatcher.add_handler(CommandHandler('covid',covid))
    updater.dispatcher.add_handler(CommandHandler('ofox',ofox))
    updater.dispatcher.add_handler(CommandHandler('magisk',magisk))
    updater.start_polling(0)
    updater.idle()

#MAIN PROGRAM
main()
