from django.core.management.base import BaseCommand
from reports.config import bot


@bot.message_handler(commands=['start'])
def begin_conversation(message):
    from reports.states.hello import HelloState
    s = HelloState(message.chat.id)
    s.display()
    user_states[message.chat.id] = s


@bot.callback_query_handler(func=lambda d: True)
def callback_handler(message):
    s = user_states[message.from_user.id]
    s2 = s.proccess(message)
    s2.display()
    user_states[message.from_user.id] = s2


user_states = {}

class Command(BaseCommand):
    help = 'start'

    def handle(self, *args, **options):
        print('ok')
        bot.infinity_polling()