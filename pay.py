import telebot
from telebot import types

bot = telebot.TeleBot('ВАШ_ТОКЕН_БОТА')

# Обработчик команды /buy
@bot.message_handler(commands=['buy'])
def send_invoice(message):
    # Создаем цену (1 звезда = 1 XTR)
    prices = [types.LabeledPrice(label='XTR', amount=5)]

    # Отправляем счет
    bot.send_invoice(
        message.chat.id,
        title='Цифровой товар',
        description='Описание вашего товара или услуги',
        invoice_payload='payload_123',  # Уникальный ID платежа
        provider_token='',  # Для Stars оставляем пустым
        currency='XTR',  # Валюта Telegram Stars
        prices=prices
    )

# Подтверждение платежа (должно обработаться за 10 секунд)
@bot.pre_checkout_query_handler(func=lambda query: True)
def pre_checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

# Успешный платеж
@bot.message_handler(content_types=['successful_payment'])
def successful_payment(message):
    bot.send_message(message.chat.id, '✅ Оплата прошла успешно! Товар выдан.')

# Обязательная команда поддержки
@bot.message_handler(commands=['paysupport'])
def pay_support(message):
    bot.send_message(message.chat.id, 'По вопросам оплаты обращайтесь к @support')

bot.polling()