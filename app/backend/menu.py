from app.libs import *
from app.backend.bot import BotApi
from kivy.app import App

class Start(CircularRippleBehavior,CircularElevationBehavior,ButtonBehavior,MDFloatLayout):
    def __init__(self,*args, **kwargs):
        super(Start,self).__init__(*args,**kwargs)
        self.bind(on_release=self.do_animation)
        BotApi.token = database('app-data').read()['bot']['token']
        BotApi.on_message = self.on_message
        BotApi.on_image = self.on_image
        BotApi.on_audio = self.on_audio

        self.bot_api = BotApi()

    def do_animation(self,widget):
        wid = widget.ids.start_label
        if wid.text == 'Stop':
            anim = Animation(text_color=(0,1,0,1))
            anim.start(wid)
            wid.text='Start'
            anim = Animation(circle_color=(0,1,0,1))
            anim.start(widget)
            self.bot_api.run()

        else: # Stop
            anim = Animation(text_color=(1,0,0,1))
            anim.start(wid)
            wid.text='Stop'
            anim = Animation(circle_color=(1,0,0,1))
            anim.start(widget)
            self.bot_api.stop()

    def on_message(self,message):
        self.all.text = str(int(self.all.text)+1)
        if message.text in database('bot-msg').read():
            self.bot_api.bot.reply_to(
                message,
                database('bot-msg').read()[message.text],
                parse_mode='MARKDOWN',
            )
            self.reply.text = str(int(self.reply.text)+1)

    def on_image(self,image):
        self.image.text = str(int(self.image.text)+1)

    def on_audio(self,audio):
        self.audio.text = str(int(self.audio.text)+1)

class AddMessages(ModalView):
    callback = None

class SwipeToDeleteItem(MDCardSwipe):
    send = StringProperty()
    reply = StringProperty()
    delete=lambda x:x

class MenuScreen(Screen):
    def __init__(self,*args,**kwargs):
        super(MenuScreen,self).__init__(*args,**kwargs)
        self.app = App.get_running_app()
        self.add_messages = AddMessages()
        self.add_messages.callback = self.on_add_message

        self.msg_db()

    def msg_db(self):
        for send,reply in database('bot-msg').read().items():
            SwipeToDeleteItem.delete=self.remove_item
            self.ids.messages.add_widget(
                SwipeToDeleteItem(
                    send=send,
                    reply=reply,
                )
            )

    def on_add_message(self, type, send, reply):
        if type == self.app.ar(self.app.language['add']):
            if send not in database('bot-msg').read():
                SwipeToDeleteItem.delete=self.remove_item
                self.ids.messages.add_widget(
                    SwipeToDeleteItem(
                        send=send,
                        reply=reply,
                    )
                )
                db = database('bot-msg').read()
                db[send]=reply
                database('bot-msg').add(db)
                toast(self.app.language['done'])
            else:
                toast(self.app.language['is already in use'])

    def remove_item(self,instance):
        database('bot-msg').delete(instance.send)
        self.ids.messages.remove_widget(instance)
