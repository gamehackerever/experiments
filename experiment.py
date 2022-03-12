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
import time
import aiohttp
import os
from datetime import datetime as dt
from pytz import country_names as c_n
from pytz import country_timezones as c_tz
from pytz import timezone as tz

BOT_TOKEN = os.environ.get("BOT_TOKEN")
updater = Updater(BOT_TOKEN,
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "<b>Hemlo Gay! I'm Srinand's Personal Bot. FUCK OFF WEN?</b>",parse_mode='html')

def help(update: Update, context: CallbackContext):
    args = getFinalWord(update.message.text)
    if args == "":
        update.message.reply_text("***Available Commands: \
            \n\n/start\n\t\t\t\tUsage: Get started With The Bot           \
            \n\n/help\n\t\t\t\tUsage: Get Help \
            \n\n/echo <text> \n\t\t\t\tUsage: Echo Messages. \
            \n\n/spam <count> <text> \n\t\t\t\tUsage: Floods text in the chat.  \
            \n\n/rom <rom_name>\n\t\t\t\tUsage: Get Latest ROM post. \
            \n\n/google <search_keyword>\n\t\t\t\tUsage: Google Stuff. \
            \n\n/covid <country>\n\t\t\t\tUsage: Get COVID-19 Stats. \
            \n\n/ofox <device>\n\t\t\t\tUsage: Get Latest OrangeFox Recovery. \
            \n\n/magisk\n\t\t\t\tUsage: Get Latest Magisk Zip/Apk \
            \n\n/time <country name/code> <timezone number>\n\t\t\t\tUsage: Get the time of a country.\
            \n\nUse /help <command> To Know More About It.***",
                parse_mode='markdown')

    elif args == "spam":
        update.message.reply_text("***Available Commands: \
            \n\n/cspam <text> \
            \n\t\t\t\tUsage: Spam the text letter by letter. \
            \n\n/spam <count> <text> \
            \n\t\t\t\tUsage: Floods text in the chat !! \
            \n\n/wspam <text> \
            \n\t\t\t\tUsage: Spam the text word by word. \
            \n\n/picspam <count> <link to image> \
            \n\t\t\t\tUsage: As if text spam was not enough !! \
            \n\n/delayspam <delay> <count> <text> \
            \n\t\t\t\tUsage: /spam but with custom delay. \
            \n\n\nNOTE : Spam at your own risk !!***",parse_mode='markdown')


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

def cspam(update: Update, context: CallbackContext) -> None:
        """Spam Multiple Messages"""

        cspamMessage = update.message.text
        finalMesssage = getFinalWord(cspamMessage)
        message = finalMesssage.replace(" ", "")
        
        for letter in message:
            context.bot.send_message(chat_id=update.effective_chat.id, text=letter)

def wspam(update: Update, context: CallbackContext) -> None:
        wspam = getFinalWord(update.message.text)
        message = wspam.split()
        for word in message:
            context.bot.send_message(chat_id=update.effective_chat.id, text=word)

def spam(update: Update, context: CallbackContext) -> None:
        try:
            counter = int(getFinalWord(update.message.text).split(" ", 1)[0])
        except ValueError or IndexError:
            update.message.reply_text("The usage of this command is /spam <count> <text>")
            return

        textx = getFinalWord(update.message.text)

        spam_message = str(getFinalWord(update.message.text).split(" ", 1)[1])

        for i in range(counter):
            context.bot.send_message(chat_id=update.effective_chat.id, text=spam_message)


def picspam(update: Update, context: CallbackContext) -> None:
        text = getFinalWord(update.message.text).split()  
        try:
            counter = int(text[0])
            link = str(text[1])
        except IndexError:
            update.message.reply_text("The usage of this command is /pspam <count> <link to image>")
            return
        for _ in range(1, counter):
            context.bot.send_photo(update.effective_chat.id, link)


def delayspam(update: Update, context: CallbackContext) -> None:
        try:
            spamDelay = float(getFinalWord(update.message.text).split(" ", 2)[0])
            counter = int(getFinalWord(update.message.text).split(" ", 2)[1])
            spam_message = str(getFinalWord(update.message.text).split(" ", 2)[2])
        except ValueError:
            update.message.reply_text("The usage of this command is .delayspam <delay> <count> <text>")
            return
        for _ in range(1, counter):
            context.bot.send_message(update.effective_chat.id,spam_message)
            time.sleep(spamDelay)

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
    update.message.reply_text("***Fetching Details...\nPlease Wait...***",parse_mode="markdown")
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
        updater.bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id + 1)
        update.message.reply_text(f"Corona Virus Info in {country}:\n\n{output_text}",parse_mode='markdown',disable_web_page_preview='true')

    except ValueError:
        updater.bot.delete_message(chat_id = update.message.chat_id, message_id = update.message.message_id + 1)
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

def time(update:Update, context: CallbackContext) -> None:
    def get_tz():
        """ Get time zone of the given country. """
        con = getFinalWord(update.message.text).split(" ", 1)[0]
        if "(Uk)" in con:
            con = con.replace("Uk", "UK")
        if "(Us)" in con:
            con = con.replace("Us", "US")
        if " Of " in con:
            con = con.replace(" Of ", " of ")
        if "(Western)" in con:
            con = con.replace("(Western)", "(western)")
        if "Minor Outlying Islands" in con:
            con = con.replace("Minor Outlying Islands", "minor outlying islands")
        if "Nl" in con:
            con = con.replace("Nl", "NL")

        for c_code in list(c_n):
            if con.title() == c_n[c_code]:
                return c_tz[c_code]
        try:
            if c_n[con]:
                return c_tz[con]
        except KeyError:
            return

        if con not in list(c_n):
            update.message.reply_text("<b>Invalid Country Probably!</b>",parse_mode="html")

    def time_func():
        """For /time command, return the time of
        1. The country passed as an argument,
        2. The default userbot country(set it by using .settime),
        3. The server where the userbot runs.
        """
        
        con = getFinalWord(update.message.text).split(" ", 1)[0]
        try:
            tz_num = getFinalWord(update.message.text).split(" ", 1)[1]
        except IndexError:
            tz_num = ""

        t_form = "%H:%M"
        c_name = None

        if len(con) > 4:
            try:
                c_name = c_n[con]
            except KeyError:
                c_name = con
            timezones = get_tz()
        elif con==COUNTRY:
            c_name = COUNTRY
            tz_num = TZ_NUMBER
            timezones = get_tz()
        
        if getFinalWord(update.message.text) == "":
            update.message.reply_text(f"`It's`  **{dt.now().strftime(t_form)}**  `here. (IST)`",parse_mode="markdown")
            return
        try:
            if not timezones:
                update.message.reply_text("`Invaild country.`",parse_mode="markdown")
                return
        except UnboundLocalError:
            update.message.reply_text("`Invaild country.`",parse_mode="markdown")

        if len(timezones) == 1:
            time_zone = timezones[0]
        elif len(timezones) > 1:
            if tz_num:
                tz_num = int(tz_num)
                time_zone = timezones[tz_num - 1]
            else:
                return_str = f"`{c_name} has multiple timezones:`\n\n"

                for i, item in enumerate(timezones):
                    return_str += f"`{i+1}. {item}`\n"

                return_str += "\n`Choose one by typing the number "
                return_str += "in the command.`\n"
                return_str += f"`Example: .time {c_name} 2`"

                update.message.reply_text(return_str,parse_mode="markdown")
                return

        dtnow = dt.now(tz(time_zone)).strftime(t_form)

        if c_name != COUNTRY:
            update.message.reply_text(f"`It's`  **{dtnow}**  `in {c_name}({time_zone} timezone).`",parse_mode="markdown")
            return

        elif COUNTRY:
            update.message.reply_text(
                f"`It's`  **{dtnow}**  `here, in {COUNTRY}" f"({time_zone} timezone).`",parse_mode="markdown"
            )
            return

    # Time & Date - Country and Time Zone
    COUNTRY = str(os.environ.get("COUNTRY") or "")
    TZ_NUMBER = os.environ.get("TZ_NUMBER") or 1
    time_func()


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
    updater.dispatcher.add_handler(CommandHandler('cspam', cspam,run_async=True))
    updater.dispatcher.add_handler(CommandHandler('wspam', wspam,run_async=True))
    updater.dispatcher.add_handler(CommandHandler('picspam', picspam,run_async=True))
    updater.dispatcher.add_handler(CommandHandler('delayspam', delayspam,run_async=True))
    updater.dispatcher.add_handler(CommandHandler('rom',rom))
    updater.dispatcher.add_handler(CommandHandler('google',google))
    updater.dispatcher.add_handler(CommandHandler('covid',covid))
    updater.dispatcher.add_handler(CommandHandler('ofox',ofox))
    updater.dispatcher.add_handler(CommandHandler('magisk',magisk))
    updater.dispatcher.add_handler(CommandHandler('time',time))
    updater.start_polling(0)
    updater.idle()

#MAIN PROGRAM
main()
