from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot('1907224811:AAHcPAx6wESyk3KocIt4DrnCibJrttm6F1o', parse_mode='html')


dp = Dispatcher(bot, storage=MemoryStorage())

chats = ['-1001434497815', '-1001275423186']


LOG_CHAT = '-1001215465037'

ADMINS = [1952264310]