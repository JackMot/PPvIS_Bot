import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import IDFilter


# ----------

async def work_start(message: types.Message):
    logging.info('Work init by ' + str(message.from_user.id))
    await message.answer("https://docs.google.com/spreadsheets/d/1Fzhkd4fhKD8ux-Ocv5oXXix_e7wd--7Yweorum8YkI0/edit#gid=0")


# ----------


def register_handlers_work(dp: Dispatcher, admin_id: int, ):
    # Все команды обрабатываются здесь.
    # Тут можно задавать параметры выполнения и ключевые слова по которым они будут вызываться.
    dp.register_message_handler(work_start, IDFilter(user_id=admin_id), commands="work", state="*")
