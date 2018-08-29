from telegram.ext import CommandHandler, RegexHandler

from aisarbot.command import GENDER, AGE, start, gender, age, cancel

handler_config = {
    "entry_points": [CommandHandler('start', start)],
    "states": {
        GENDER: [RegexHandler('^(Male|Female|Other)$', gender)],
        AGE: [RegexHandler('^\d+$', age)]
    },
    "fallbacks": [CommandHandler('cancel', cancel)]
}
