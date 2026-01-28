from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# menu = ReplyKeyboardMarkup(
#    keyboard=[
 #       [KeyboardButton(text='Price'), KeyboardButton(text='О боте')],
 #       [KeyboardButton(text='Как приобрести?')]
 #   ],
  #  resize_keyboard=True,
 #   input_field_placeholder='Выберите пункт меню: '
#)


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🛍 Price', callback_data='princ'), InlineKeyboardButton(text='⭕ Информация', callback_data='obot')],
        [InlineKeyboardButton(text='⁉ Как приобрести?', callback_data='kak')]
    ]
)

    
price = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='📂 Username', callback_data='username'), InlineKeyboardButton(text='📂 Водянки', callback_data='vod')],
        [InlineKeyboardButton(text='📂 Numbers', callback_data='num'), InlineKeyboardButton(text='📂 Шаблоны км', callback_data='km')],
        [InlineKeyboardButton(text='📂 Подарок от форестова', callback_data='giftfor')]
    ]
)


gift = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='giftback')]
    ]
)


catalog = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔴 @no_qp', callback_data='no_qp'), InlineKeyboardButton(text='🟢 @TEPAKT_0', callback_data='tera')],
        [InlineKeyboardButton(text='🟢 @vlastelin_n', callback_data='vlastelin_n'), InlineKeyboardButton(text='🟠 @csubota', callback_data='csubota')],
        [InlineKeyboardButton(text='🟢 @qponedelnik', callback_data='qponedelnik'), InlineKeyboardButton(text='🟢 @HAPKOMAH_2000', callback_data='HAPKOMAH_2000')],
        [InlineKeyboardButton(text='🟢 @c_cpok', callback_data='c_cpok'), InlineKeyboardButton(text='🟢 @OvnerMorga', callback_data='OvnerMorga')],
        [InlineKeyboardButton(text='🟢 @BazaMorga', callback_data='BazaMorga'), InlineKeyboardButton(text='🟢 @CTPAX_PY_FSB', callback_data='CTPAX_PY_FSB')],
        [InlineKeyboardButton(text='🟢 @bespilotnickk', callback_data='bespilotnickk'), InlineKeyboardButton(text='🔴 @you_mans', callback_data='you_mans')],
        [InlineKeyboardButton(text='🟢 @qvlastelin', callback_data='qvlastelin'), InlineKeyboardButton(text='🟢 @qgqpgp', callback_data='qgqpgp')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]
    ]
)


woter = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='📂 Водянки AE', callback_data='vodae')],
        [InlineKeyboardButton(text='📂 Водянки NODE VIDEO', callback_data='vodnd')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='bback')]
    ]
)


woterae = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💧 Водяной знак №1', url='https://t.me/operotovwm/151'), InlineKeyboardButton(text='💧 Водяной знак №2', url='https://t.me/operotovwm/154')],
        [InlineKeyboardButton(text='💧 Водяной знак №3', url='https://t.me/operotovwm/156'), InlineKeyboardButton(text='💧 Водяной знак №4', url='https://t.me/operotovwm/158')],
        [InlineKeyboardButton(text='💧 Водяной знак №5', url='https://t.me/operotovwm/160'), InlineKeyboardButton(text='💧 Водяной знак №6', url='https://t.me/operotovwm/161')],
        [InlineKeyboardButton(text='💧 Водяной знак №7', url='https://t.me/operotovwm/162'), InlineKeyboardButton(text='💧 Водяной знак №8', url='https://t.me/operotovwm/163')],
        [InlineKeyboardButton(text='💧 Водяной знак №9', url='https://t.me/operotovwm/164'), InlineKeyboardButton(text='💧 Водяной знак №10', url='https://t.me/operotovwm/165')],
        [InlineKeyboardButton(text='💧 Водяной знак №11', url='https://t.me/operotovwm/166'), InlineKeyboardButton(text='💧 Водяной знак №12', url='https://t.me/operotovwm/167')],
        [InlineKeyboardButton(text='💧 Водяной знак №13', url='https://t.me/operotovwm/168'), InlineKeyboardButton(text='💧 Водяной знак №14', url='https://t.me/operotovwm/169')],
        [InlineKeyboardButton(text='💧 Водяной знак №15', url='https://t.me/operotovwm/170'), InlineKeyboardButton(text='💧 Водяной знак №16', url='https://t.me/operotovwm/171')],
        [InlineKeyboardButton(text='💧 Водяной знак №17', url='https://t.me/operotovwm/172'), InlineKeyboardButton(text='💧 Водяной знак №18', url='https://t.me/operotovwm/173')],
        [InlineKeyboardButton(text='💧 Водяной знак №19', url='https://t.me/operotovwm/174'), InlineKeyboardButton(text='💧 Водяной знак №20', url='https://t.me/operotovwm/191')],
        [InlineKeyboardButton(text='💧 Водяной знак №21', url='https://t.me/operotovwm/195')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='bbaack')]
    ]
)


woternd = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💧 Водяной знак №1', url='https://t.me/operotovwm/185')],
        [InlineKeyboardButton(text='💧 Водяной знак №2', url='https://t.me/operotovwm/186')],
        [InlineKeyboardButton(text='💧 Водяной знак №3', url='https://t.me/operotovwm/187')],
        [InlineKeyboardButton(text='💧 Водяной знак №4', url='https://t.me/operotovwm/188')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='bbaacck')]
    ]
)

aboud = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='🔰 Автор', callback_data='aut'), InlineKeyboardButton(text='🔰 Канал', url="https://t.me/treefel")],
        [InlineKeyboardButton(text='🔰 О боте', callback_data='av')]
    ]
)


phys = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='+57 (301)...', callback_data='+57')],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='backk')]
    ]
)


usir = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='kcab')]
    ]
)


boti = InlineKeyboardMarkup(
     inline_keyboard=[
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='botback')]
    
     ]
)


author = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👁️ Юзернейм создателя', callback_data='uz')],
        [InlineKeyboardButton(text='👍 Отзывы ', url='https://t.me/repatreefel')],
        [InlineKeyboardButton(text='👼 Биография', url="https://t.me/informaytions")],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='backf')]
    ]
)
edits = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='👀 Шаблон №1', url="https://t.me/HAPKOMAH_2000/12")],
        [InlineKeyboardButton(text='👀 Шаблон №2', url="https://t.me/HAPKOMAH_2000/13")],
        [InlineKeyboardButton(text='👀 Шаблон №3', url="https://t.me/HAPKOMAH_2000/14")],
        [InlineKeyboardButton(text='⬅️ Назад', callback_data='backkk')]
    ]
)


kok = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='💘 Оплата рублями', callback_data='vanila')],
        [InlineKeyboardButton(text='💘 Звёздами телеграм', callback_data='zv')],
        [InlineKeyboardButton(text='💘 Крипто кошелёк', callback_data='crypt')]
    ]
)


pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Поддержка бота', callback_data='podbot')]
    ]
)


get_number = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Отправить номер ☎️',
                    request_contact=True)]
    ]
)
    