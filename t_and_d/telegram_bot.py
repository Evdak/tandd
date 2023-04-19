import logging
import telebot
from t_and_d.settings import TELEGRAM_BOT_TOKEN, TELEGRAM_SECRET_KEY

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

if __name__ == '__main__':
    import os
    import django
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "t_and_d.settings")
    django.setup()

    from tgbot import models

    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    )

    logger = logging.getLogger("TGBOT")

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message: telebot.types.Message):
        try:
            msg = message.text.lower()
            user, _ = models.TGUser.objects.get_or_create(
                tg_id=message.from_user.id,
                name=message.from_user.username,
            )
            user.save()

            if msg == "/start":
                logger.info(f'{message.from_user.id}:{message.from_user.username} - {message.text.lower()}')
                bot.send_message(message.from_user.id, "Привет")

            elif msg == f"/subscribe {TELEGRAM_SECRET_KEY}":
                logger.warning(f'NEW ADMIN: {message.from_user.id}:{message.from_user.username} - {message.text.lower()}')
                user.is_admin = True
                user.save()
                bot.send_message(message.from_user.id, "Подписан на входящие заявки")

            elif msg == f"/subscribe":
                bot.send_message(message.from_user.id, "Добавьте секретный ключ")

            elif msg == f"/unsubscribe {TELEGRAM_SECRET_KEY}":
                logger.warning(f'DELETE ADMIN: {message.from_user.id}:{message.from_user.username}')
                user.is_admin = False
                user.save()
                bot.send_message(message.from_user.id, "Отписан от входящих заявок")

            elif msg == f"/unsubscribe":
                bot.send_message(message.from_user.id, "Добавьте секретный ключ")

            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю")
        except Exception as err:
            logger.error(err)

    logger.warning(f"TG STARTED")
    logger.info(f"{bot.get_me()}")
    bot.polling(none_stop=True, interval=0)
