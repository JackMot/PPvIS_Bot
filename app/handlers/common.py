import logging

from aiogram.dispatcher.filters import Text
from app.handlers.messages import MESSAGES
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext


async def cmd_start(message: types.Message, state: FSMContext):
    logging.info('start init by ' + str(message.from_user.id))
    await state.finish()
    await message.answer(
        MESSAGES['start'],
        reply_markup=types.ReplyKeyboardRemove()
    )


# ----------


async def cmd_help(message: types.Message):
    logging.info('help init by ' + str(message.from_user.id))
    await message.answer(
        MESSAGES['help'],
        reply_markup=types.ReplyKeyboardRemove()
    )


# ----------

async def cmd_cancel(message: types.Message, state: FSMContext):
    logging.info('cancel init by ' + str(message.from_user.id))
    await state.finish()
    await message.answer(MESSAGES['cancel'], reply_markup=types.ReplyKeyboardRemove())


# ----------

def register_handlers_common(dp: Dispatcher):
    # Все команды обрабатываются здесь.
    # Тут можно задавать параметры выполнения и ключевые слова по которым они будут вызываться.
    dp.register_message_handler(cmd_start, commands="start", state="*")
    dp.register_message_handler(cmd_help, commands="help", state="*")
    dp.register_message_handler(cmd_cancel, commands="cancel", state="*")
    dp.register_message_handler(cmd_cancel, Text(equals="отмена", ignore_case=True), state="*")
