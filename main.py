from aiogram.utils import executor
from commands import dp

async def bot_start(_):
    print('Бот запущен!') #Доработать уже готового телеграм-бота или создать новое приложение
    # (любое) с использованием сторонних библиотек


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=bot_start)
