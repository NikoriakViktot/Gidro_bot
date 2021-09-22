from reports.states.base import BaseState
from reports.tg_buttons import RiverStateButtons,PostStateButtons
from telebot import types
from reports.states.river import RiverState
from reports.states.post import PostState



class HelloState(BaseState):
    text = "Вибиріть Річку або Гідропост"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.keyboard.add(RiverStateButtons.river_button)
        self.keyboard.add(PostStateButtons.post_button)




    def proccess(self, message:types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:RiverState':
                return RiverState(self.chat_id)
            if message.data == 'nextstate:PostState':
                return PostState(self.chat_id)
        return self