import telebot
import threading as t

class BotApi:
    bot = telebot.TeleBot("1223547680:AAEWhvq7osUEcyqIKHcL01zyNKLmQ3UAfZk")

    def __init__(self):
        T = t.Thread(target=self.message_handler)
        T.daemon = True
        T.start()

    def message_handler(self):
        @self.bot.message_handler(func=lambda m: True)
        def echo_all(message):
            self.msg(message)

    def msg(self,m):
        pass


    def run(self):
        T = t.Thread(target=self.bot.polling)
        T.daemon = True
        T.start()

    def stop(self):
        self.bot.stop_polling()

# BotApi().run()
