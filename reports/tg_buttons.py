from telebot import types



class RiverStateButtons:
    river_button = types.InlineKeyboardButton(text='Річки', callback_data='nextstate:RiverState')
    pryt_button = types.InlineKeyboardButton(text='Річка Прут', callback_data='nextstate:PostState')
    # siret_button = types.InlineKeyboardButton(text='Річка Сірет', callback_data='nextstate:PostState')
    # cheremosh_button = types.InlineKeyboardButton(text='Річка Черемош', callback_data='nextstate:PostState')
    # biluy_cheremosh_button = types.InlineKeyboardButton(text='Річка Білий Черемош', callback_data='nextstate:PostState')
    # chornuy_cheremosh_button = types.InlineKeyboardButton(text='Річка Чорний Черемош', callback_data='nextstate:PostState')



class PostStateButtons:
    post_button = types.InlineKeyboardButton(text='ГідроПост', callback_data='nextstate:PostState')
    cher_button = types.InlineKeyboardButton(text='ГідроПост Чернівці', callback_data='nextstate:PostCher')


class PostDataButtons:
    last_report_button = types.InlineKeyboardButton(text="Рівень", callback_data='nextstate:Level')
    pagodas_button = types.InlineKeyboardButton(text="Погода", callback_data='nextstate:Pogoda')