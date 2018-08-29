from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

from aisarbot import logger
from aisarbot.db import update_user, create_user_if_not_exists

GENDER, AGE, LOCATION, INT_GENDER, INT_AGE, INT_RADIUS = range(6)

gender_responds = {
    "Male": "Alright man, now i need your age.",
    "Female": "Now i need your age dear.",
    "Other": "Hmm. We love privacy huh? Anyway, i need your age now."
}

def start(bot, update):
    user = update.message.from_user
    logger.info("{0} (@{1}) has joined the game!".format(
        user.first_name, user.username))

    create_user_if_not_exists(int(user.id))
    update_user(int(user.id), first_name=user.first_name,
        last_name=user.last_name, username=user.username, is_bot=user.is_bot)

    reply_keyboard = [['Male', 'Female', 'Other']]

    update.message.reply_text(
        "Hi! My name is AisarB0t. I am here to find hot chicks near you. "
        "But I need to know about you first. I will hold a conversation "
        "with you. Send me /cancel any time if you want to stop. Let's start."
        "\n\nWhat is your gender?",
        reply_markup=ReplyKeyboardMarkup(reply_keyboard,
            one_time_keyboard=True, resize_keyboard=True))

    return GENDER

def gender(bot, update):
    user = update.message.from_user
    gender = update.message.text

    update_user(int(user.id), gender=gender)

    update.message.reply_text(gender_responds[gender])

    return AGE

def age(bot, update):
    user = update.message.from_user
    age = int(update.message.text)

    update_user(int(user.id), age=age)

    if age < 18:
        update.message.reply_text(
            "You can not join our full-of-chick community boss :(")
        return ConversationHandler.END

    update.message.reply_text("END OF DEMO.")
    return ConversationHandler.END

def cancel(bot, update):
    user = update.message.from_user
    logger.info("User {0} (@{1}) canceled the conversation.".format(
        user.first_name, user.username))
    update.message.reply_text('Bye! I will handle chicks from now on ',
                              reply_markup=ReplyKeyboardRemove())

    return ConversationHandler.END

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
