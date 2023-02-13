import logging

from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN


API_TOKEN = TOKEN
# Configure logging

logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)
    print(message)


@dp.message_handler(content_types=['left_chat_member'])
async def on_user_joined(message: types.Message):
    await message.delete()


@dp.message_handler(content_types=['new_chat_members'])
async def on_user_joined(message: types.Message):
    await message.delete()
    await message.answer("[{}](tg://user?id={}), 🤝 Добро пожаловать в чат\n"
                         " [StackOverflow на русском](https://ru.stackoverflow.com/)"
        .format(message.from_user.first_name, message.from_user.last_name, message.from_user.id),
        disable_web_page_preview=True,
        parse_mode="Markdown")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
