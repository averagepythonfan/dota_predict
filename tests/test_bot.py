from bot.handlers.handlers import help_command
from unittest.mock import AsyncMock

async def test_start_handler():
    message = AsyncMock()
    await help_command(message)
    message.reply.assert_called_with('This is a help command')
