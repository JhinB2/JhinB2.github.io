from wappdriver import WhatsApp

with WhatsApp() as bot:
    bot.send('Aleix Munty',  # name of recipient
             ''  # message
            )