
from aiogram import F, Router, Bot, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.types import LabeledPrice, Message
import keyboards as kb
import telebot


user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f"""Добро пожаловать в бот, {message.from_user.first_name} 💘\n\nКанал бота @treefel
┌──────────────────────────────────\n├ 🆔️ Твой ID : {message.from_user.id}\n├ 👤 Имя аккаунта : {message.from_user.first_name}\n├ 👁️ Юзернейм : @{message.from_user.username}\n├ 💎 Премиум : {message.from_user.is_premium} \n├ 🌐 Язык : {message.from_user.language_code} \n├ 🕒 Время : {message.date}
└──────────────────────────────────\n\n┌─ Здесь ты можешь посмотреть цены на 🛍\n├ Водяные знаки (Магазин - @operotovwm) ✅\n├ Юзернеймы ✅\n├ Телеграм аккаунты✅ \n├ Шаблоны км эдитов ✅\n\nAnadyr Forestov и @axazix это один и тот же человек\n\n‼ Заметили ошибку в боте? Сразу напишите анонимное сообщение в @Anadyrs_bot ‼\n\nДанный бот является просто показателем разной информации. В этом боте нет каких либо полезных функций. Бот буду улучшать.
Мой первый бот, написал Anadyr Forestov, @axazix""",
                         reply_markup=kb.menu)


@user.callback_query(F.data == 'princ')
async def cmd_price(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('🔥 Выбери, интересующую тебя, категорию товара:',
                         reply_markup=kb.price)
     
    
@user.callback_query(F.data == 'obot')
async def cmd_price(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('ℹ️ Выбери какую информацию хочешь получить: ',
                         reply_markup=kb.aboud)
    
    
@user.callback_query(F.data == 'kak')
async def cmd_price(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('✅ Приобрести товар из любой категории можно в этом боте @Anadyrs_bot\n‼ Оплачивать только после согласия @axazix \n\n👇 Ниже представленны способы оплаты 👇',
                         reply_markup=kb.kok)
    
    
@user.callback_query(F.data == 'vanila')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'🔹 Перевод на карту - 5599 0021 2686 2285', show_alert=True)
    
    
@user.callback_query(F.data == 'zv')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'🔹 Звёзды отправлять на этот аккаунт @axazix', show_alert=True)
    
    
@user.callback_query(F.data == 'crypt')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'🔹 Адрес крипто кошелька (Tonkeeper) - UQAtjMIUe3OfzcfuaoAZ1Zx7itJ7bvLmJGcEfh5G2gYJKAA7', show_alert=True)
 
    
    
@user.callback_query(F.data == 'username')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="""Username\n\nTelegram username важен, потому что это:

1. Username это индивидуальность в телеграмме
2. Ваш адрес в Telegram - можно дать людям имя, а не номер телефона
3. Просто для поиска — вас могут найти по нику без вашего номера
4. Для каналов/ботов — на вас можно ссылаться, упоминать, переходить
5. Конфиденциальность — номер телефона остаётся скрытым\n\nВыберите юзернейм:\n🟢 Юзернейм продаётся\n🟠 Юзернейм забронирован\n🔴 Юзернейм не продаётся/продан\n\nВы можете забронировать юзернейм 🧡\nЮзернейм бронируется на 1 неделю , продлить бронь можно всего 3 раза.\nНельзя сразу забронировать юз на 3 раза ❌, каждая продлительная бронь происходит по окончанию срока предыдущей ✅ """, reply_markup=kb.catalog)
    
    
@user.callback_query(F.data == 'vod')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="""Водяные знаки 💧\n\nВодяные знаки в видео нужны для:

1. Защиты от воровства — чтобы другие не выдавали ваше видео за своё
2. Рекламы бренда — зрители видят, кто создатель, даже если видео перепостят
3. Сохранения авторства — доказательство, что видео ваше, если возникнет спор\n\nВыбери группу :""", reply_markup=kb.woter)
    
    
    
@user.callback_query(F.data == 'vodae')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Водяные знаки AFTER EFFECTS\n\nВыбери водяной знак, который тебя интересует :", reply_markup=kb.woterae)
    
    
@user.callback_query(F.data == 'vodnd')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Водяные знаки NODE VIDEO\n\nВыбери водяной знак, который тебя интересует :", reply_markup=kb.woternd)
    

@user.callback_query(F.data == 'num')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Numbers\n\nВыбери номер телефона:", reply_markup=kb.phys)
    
    
@user.callback_query(F.data == 'km')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Эдиты км\n\nВыбери нужный тебе эдит\nВсе шаблоны стоят 25 ⭐, 50 ₽, 0.5 $", reply_markup=kb.edits)
    
    
@user.callback_query(F.data == '+57')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Номер телефона - +57 (301) 929\nСтрана - Колумбия\nАккаунт создан - 14 ноября 2024 год\n\nЦена - 100 ₽, 100 ⭐', show_alert=True)
    
    
@user.callback_query(F.data == 'aut')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери что хочешь узнать о авторе: ", reply_markup=kb.author)
    
    
@user.callback_query(F.data == 'giftfor')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text='🎁 Привет, чтобы получить подарок за 15 звезд от Anadyr Forestov нужно:\n\n• Подписаться на канал @treefel ✅️\n• Кинуть 2 подарка "Мишка" ему -> @axazix ✅️\n• Сказать какой подарок какой подарок вы хотите: Мишка/Сердечко, и какую подпись к подарку вы хотите ✅️\n\nПосле выполнений всех условий я вам кину подарок с вашими указаниями с аккаунта Anadyr Forestov ❤️', reply_markup=kb.gift)
    
    
@user.callback_query(F.data == 'giftback')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="🔥 Выбери, интересующую тебя, категорию товара:", reply_markup=kb.price)
    
    
@user.callback_query(F.data == 'uz')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Юзернейм создателя @axazix ", reply_markup=kb.usir)
    
    
@user.callback_query(F.data == 'av')  
async def check_brand(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="""Данный бот являеться просто показателем разной информации. В этом боте нет каких либо полезных функций. Бот буду улучшать.
Мой первый бот, написал Anadyr Forestov, @axazix""", reply_markup=kb.boti)
    
    
@user.callback_query(F.data == 'no_qp')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм продан!', show_alert=True)
    
    
@user.callback_query(F.data == 'vlastelin_n')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @vlastelin_n\n\nЦена - 175 ⭐, 300 ₽, 3 $', show_alert=True)
    
    
@user.callback_query(F.data == 'csubota')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Забронирован @metaminov до 11.02.2026', show_alert=True)
    
    
@user.callback_query(F.data == 'qponedelnik')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @qponedelnik\n\nЦена - 125 ⭐, 175 ₽, 2 $', show_alert=True)
    
    
@user.callback_query(F.data == 'HAPKOMAH_2000')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @HAPKOMAH_2000\n\nЦена - 100 ⭐, 150 ₽, 2 $', show_alert=True)
    
    
@user.callback_query(F.data == 'c_cpok')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @c_cpok\n\nЦена - 150 ⭐, 250 ₽, 3 $', show_alert=True)
    
    
@user.callback_query(F.data == 'OvnerMorga')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @OvnerMorga\n\nЦена - 125 ⭐, 175 ₽, 2 $', show_alert=True)
    
    
    
@user.callback_query(F.data == 'BazaMorga')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @BazaMorga\n\nЦена - 125 ⭐, 175 ₽, 2 $', show_alert=True)
    
    
@user.callback_query(F.data == 'CTPAX_PY_FSB')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @CTPAX_PY_FSB\n\nЦена - 100 ⭐, 150 ₽, 2 $', show_alert=True)
    
    
@user.callback_query(F.data == 'tera')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @TEPAKT_0\n\nЦена - 175 ⭐, 300 ₽, 4 $', show_alert=True)
    
    
@user.callback_query(F.data == 'bespilotnickk')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @bespilotnickk\n\nЦена - 150 ⭐, 250 ₽, 3 $', show_alert=True)
    
    
@user.callback_query(F.data == 'you_mans')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Не продаётся!', show_alert=True)
    
    
@user.callback_query(F.data == 'qvlastelin')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @qvlastelin\n\nЦена -  200 ⭐, 400 ₽, 4 $', show_alert=True)
    
    
@user.callback_query(F.data == 'qgqpgp')  
async def check_brand(callback: CallbackQuery):
    await callback.answer(f'Юзернейм - @qgqpgp\n\nЦена - 250 ⭐, 450 ₽, 5 $', show_alert=True)
    
    
@user.callback_query(F.data == 'back')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="🔥 Выбери, интересующую тебя, категорию товара:", reply_markup=kb.price)
    
    
@user.callback_query(F.data == 'backk')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="🔥 Выбери, интересующую тебя, категорию товара:", reply_markup=kb.price)
    
    
@user.callback_query(F.data == 'backkk')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="🔥 Выбери, интересующую тебя, категорию товара:", reply_markup=kb.price)
    
    
@user.callback_query(F.data == 'bback')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="🔥 Выбери, интересующую тебя, категорию товара:", reply_markup=kb.price)
    
    
@user.callback_query(F.data == 'botback')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="ℹ️ Выбери какую информацию хочешь получить: ", reply_markup=kb.aboud)
    
    
@user.callback_query(F.data == 'bbaack')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="""Водяные знаки 💧\n\nВодяные знаки в видео нужны для:

1. Защиты от воровства — чтобы другие не выдавали ваше видео за своё
2. Рекламы бренда — зрители видят, кто создатель, даже если видео перепостят
3. Сохранения авторства — доказательство, что видео ваше, если возникнет спор\n\nВыбери группу :""", reply_markup=kb.woter)
    
    
@user.callback_query(F.data == 'bbaacck')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="""Водяные знаки 💧\n\nВодяные знаки в видео нужны для:

1. Защиты от воровства — чтобы другие не выдавали ваше видео за своё
2. Рекламы бренда — зрители видят, кто создатель, даже если видео перепостят
3. Сохранения авторства — доказательство, что видео ваше, если возникнет спор\n\nВыбери группу :""", reply_markup=kb.woter)
    
    
@user.callback_query(F.data == 'kcab')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="Выбери что хочешь узнать о авторе :", reply_markup=kb.author)
    
    
@user.callback_query(F.data == 'backf')  
async def back(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(text="ℹ️ Выбери какую информацию хочешь получить: ", reply_markup=kb.aboud)
 
    
@user.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.from_user.id)
    
