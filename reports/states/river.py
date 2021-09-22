
from telebot import types
from reports.states.base import BaseState
from reports.tg_buttons import RiverStateButtons



class RiverState(BaseState):
    text = "Вибиріть річку"

    def __init__(self, chat_id=None):
        super().__init__(chat_id)
        self.user = self.get_user()
        self.keyboard.add(RiverStateButtons.pryt_button)
        # self.keyboard.add(RiverStateButtons.siret_button)
        # self.keyboard.add(RiverStateButtons.cheremosh_button)
        # self.keyboard.add(RiverStateButtons.biluy_cheremosh_button)
        # self.keyboard.add(RiverStateButtons.chornuy_cheremosh_button)



    def proccess(self, message:types.Message):
        if hasattr(message, 'data'):
            if message.data == 'nextstate:PostState':
                from reports.states.post import PostState
                return PostState(self.chat_id)
        return self

