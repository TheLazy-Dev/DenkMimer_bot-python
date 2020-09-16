import random
import re
from random import shuffle

import requests
from telegram.ext import Updater, CommandHandler

token = '1394685669:AAEdUCqCBhtYwMUlYnXK11-7pP2i95XUG4g'
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
print(updater)


def start(update, context):
    print(update)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi " + str(update.message.from_user.username) + ", Welcome to Denish's First Bot! "
                                                                                   "You know, its going to be "
                                                                                   "amazing. Lets Chat" + "\nHere are "
                                                                                                          "list of "
                                                                                                          "commands \n"
                                                                                                          "/roast "
                                                                                                          "@username - "
                                                                                                          "to "
                                                                                                          "roasted them\n"
                                                                                                          "/darkroast "
                                                                                                          "@username - "
                                                                                                          "to roast "
                                                                                                          "them with "
                                                                                                          "dark line "
                                                                                                          "\n/kill "
                                                                                                          "@username - "
                                                                                                          "bored of "
                                                                                                          "someone, "
                                                                                                          "just kill "
                                                                                                          "them "
                                                                                                          "(ps: I don't "
                                                                                                          "support "
                                                                                                          "murder)")


def roast(update, context):
    print(update)
    a = ["My name must taste good because it’s always in your mouth.",
         "Don’t you get tired of putting make up on two faces every morning?",
         "Too bad you can’t count jumping to conclusions and running your mouth as exercise. ",
         "Is your drama going to an intermission soon?",
         "I’m an acquired taste. If you don’t like me, acquire some taste. ",
         "My phone battery lasts longer than your relationships.",
         "Oh you’re talking to me, I thought you only talked behind my back."]
    shuffle(a)
    rand = random.randint(0, len(a) - 1)
    uname = str(update.message.text)
    if uname.__contains__("@"):
        if uname.__contains__("@DenkMemer_bot"):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="@" + str(update.message.from_user.username) + ", " + a[rand])
        else:
            var = uname.split()[1]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=var + ", " + a[rand])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="@" + str(update.message.from_user.username) + ", " + a[rand])


def roastdark(update, context):
    print(str(update))
    a = ["Your face makes onions cry.", "You look so pretty. Not at all gross, today.",
         "’m not insulting you, I’m describing you.",
         "If you’re going to be two-faced, at least make one of them pretty.",
         "I thought of you today. It reminded me to take out the trash.",
         "I love what you’ve done with your hair. \nHow do you get it to come out of your nostrils like that?",
         "You are so full of shit, the toilet’s jealous."]
    rand = random.randint(0, len(a) - 1)
    uname = str(update.message.text)
    if uname.__contains__("@"):
        if uname.__contains__("@DenkMemer_bot"):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="@" + str(update.message.from_user.username) + ", " + a[rand])
        else:
            var = uname.split()[1]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=var + ", " + a[rand])
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="@" + str(update.message.from_user.username) + ", " + a[rand])


def get_url():
    contents = requests.get('http://random.dog/woof.json').json()
    url = contents['url']
    return url


def get_image_url():
    global url
    allowed_extension = ['jpg', 'jpeg', 'png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$", url).group(1).lower()
    print("got url %s " % url)
    return url


def bop(update, context):
    print(update)
    print("reached bop")
    url = get_image_url()
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)


def kill(update, context):
    print(update)
    uname = str(update.message.text)
    if uname.__contains__("@"):
        if uname.__contains__("@DenkMemer_bot"):
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="@" + str(update.message.from_user.username) + ", " + "Ate a load of shit")
        else:
            var = uname.split()[1]
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=var + ", " + "Ate a load of shit")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="@" + str(update.message.from_user.username) + ", " + "Ate a load of shit")


start_handler = CommandHandler('start', start)
roast_handler = CommandHandler('roast', roast)
dark_roast_handler = CommandHandler('roastdark', roastdark)
bop_handler = CommandHandler('bop', bop)
kill_handler = CommandHandler('kill', kill)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(roast_handler)
dispatcher.add_handler(bop_handler)
dispatcher.add_handler(kill_handler)
dispatcher.add_handler(dark_roast_handler)
updater.start_polling()
print(updater.start_polling())


def main():
    updater = Updater('1394685669:AAEdUCqCBhtYwMUlYnXK11-7pP2i95XUG4g', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop', bop))
    updater.start_polling()
    updater.idle()
