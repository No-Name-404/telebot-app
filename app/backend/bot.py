import telebot
import threading as t

class BotApi:
    token = None
    on_message = None
    on_image = None
    on_audio = None

    def __init__(self):
        self.bot = telebot.TeleBot(self.token)

        T = t.Thread(target=self.message_handler)
        T.daemon = True
        T.start()

        T = t.Thread(target=self.image_handler)
        T.daemon = True
        T.start()

        T = t.Thread(target=self.audio_handler)
        T.daemon = True
        T.start()

    def message_handler(self):
        @self.bot.message_handler(func=lambda m: True)
        def all(message):
            self.on_message(message)

    def image_handler(self):
        @self.bot.message_handler(content_types=['photo'])
        def image(message):
            self.on_image(message)

    def audio_handler(self):
        @self.bot.message_handler(content_types=['audio'])
        def audio(message):
            self.on_audio(message)

    def run(self):
        T = t.Thread(target=self.bot.polling)
        T.daemon = True
        T.start()

    def stop(self):
        self.bot.stop_polling()
