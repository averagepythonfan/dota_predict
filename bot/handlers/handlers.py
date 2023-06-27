from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Text

router = Router()


@router.message(Command(commands=['help']))
async def help_command(message: Message):
    await message.reply('This is a help command')