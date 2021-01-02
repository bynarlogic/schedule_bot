from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


# Uncomment the following lines to enable verbose logging
# import logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'logic.schedule_adapter.Schedule',
         {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': "I'm sorry I don't understand. I schedule appointments. Is there a date and time you have in mind?",
            'maximum_similarity_threshold': 0.90
        }
    ],
    preprocessors=[
        'preprocessors.format_dates'
    ],
    database_uri='sqlite:///database.db'
)

trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english.greetings')

print('Type something to begin...')

# The following loop will execute each time the user enters input
while True:
    try:
        user_input = input()

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
