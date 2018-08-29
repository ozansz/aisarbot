from telegram.ext import CommandHandler, RegexHandler, MessageHandler, Filters

from aisarbot.command import (GENDER, AGE, LOCATION, start, gender, age,
                              location, skip_location, cancel)

handler_config = {
    "entry_points": [CommandHandler('start', start)],
    "states": {
        GENDER: [RegexHandler('^(Male|Female|Other)$', gender)],
        AGE: [RegexHandler('^\d+$', age)],
        LOCATION: [MessageHandler(Filters.location, location),
                   CommandHandler("skip", skip_location)]
    },
    "fallbacks": [CommandHandler('cancel', cancel)]
}
