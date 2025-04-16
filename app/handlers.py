from aiogram import Dispatcher, types
from aiogram.filters import CommandStart, Command

async def start_handler(message: types.Message):
    await message.answer("¡Hola! Soy tu bot de prueba.")

async def help_handler(message: types.Message):
    await message.answer("Aquí están los comandos disponibles:\n/start - Iniciar\n/help - Ayuda")

async def echo_handler(message: types.Message):
    await message.answer(f"Dijiste: {message.text}")

def setup_handlers(dp: Dispatcher):
    dp.message.register(start_handler, CommandStart())
    dp.message.register(help_handler, Command("help"))
    dp.message.register(echo_handler)
