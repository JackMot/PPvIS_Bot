import logging

from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from app.handlers.messages import MESSAGES
from api.test_api import add_data


class OrderWork(StatesGroup):
    waiting_for_link = State()


# ----------

async def lab_start(message: types.Message):
    logging.info('Lab init by ' + str(message.from_user.id))
    await message.answer(MESSAGES['link_start'])
    await OrderWork.waiting_for_link.set()


# ----------

async def lab_link_send(message: types.Message,state: FSMContext):
    try:
        # здесь должна быть функция по проверке прав доступа к ссылке
        if add_data([str(message.from_user.id), message.text]):
            await message.answer(MESSAGES['link_update'])
        else:
            await message.answer(MESSAGES['error'])
        await state.finish()
    except:
        await message.answer(MESSAGES['error'])


# ----------


def register_handlers_lab(dp: Dispatcher):
    # Все команды обрабатываются здесь.
    # Тут можно задавать параметры выполнения и ключевые слова по которым они будут вызываться.
    dp.register_message_handler(lab_start, commands="lab", state="*")
    dp.register_message_handler(lab_link_send, state=OrderWork.waiting_for_link)
