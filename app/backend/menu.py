from app.libs import *

class AddMessages(ModalView):
    pass

class MenuScreen(Screen):
    def __init__(self,*args,**kwargs):
        super(MenuScreen,self).__init__(*args,**kwargs)
        self.add_messages = AddMessages()
