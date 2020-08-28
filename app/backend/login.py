from app.libs import *

class LoginScreen(Screen):
    def login(self,token):
        if token.text != '':
            db = database('app-data').read()
            db['bot']['token']= token.text
            database('app-data').add(db)
            self.manager.current = 'menu'
        else:
            token.line_color_focus=1,0,0,1
            token.current_hint_text_color=1,0,0,1

    def _on_focus(self,instance):
        instance.line_color_focus=1,1,1,1
        instance.current_hint_text_color=1,1,1,1
        if instance.text == '' and instance.focus:
            instance.paste()
