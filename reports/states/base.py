from telebot import types
from reports.config import bot
from reports.models import TelegramUser
from django.utils import timezone



class BaseState:
    text: str = ""
    keyboard = None

    def __init__(self, chat_id):
        self.chat_id = chat_id
        keyboard = types.InlineKeyboardMarkup()
        self.keyboard = keyboard
        self.user = self.get_user()


    def display(self):
        if not self.text == '':
            bot.send_message(self.chat_id, self.text, reply_markup=self.keyboard)

    def proccess(self, message: types.Message):
        return self

    def get_user(self) -> TelegramUser:
        if not TelegramUser.objects.filter(chat_id=self.chat_id).exists():
            return TelegramUser.objects.create(first_name='',
                                               last_name= '',
                                               chat_id=self.chat_id,
                                               last_message=timezone.now())
        return TelegramUser.objects.filter(chat_id=self.chat_id).first()



