import logging

from telegram.ext import Application

from bot import config
from bot.handlers import register_handlers

logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)


def main() -> None:
    app = Application.builder().token(config.BOT_TOKEN).build()
    register_handlers(app)

    if config.WEBHOOK_URL:
        app.run_webhook(
            listen="0.0.0.0",
            port=config.PORT,
            url_path=config.WEBHOOK_PATH,
            webhook_url=f"{config.WEBHOOK_URL}/{config.WEBHOOK_PATH}",
            secret_token=config.WEBHOOK_SECRET,
        )
    else:
        app.run_polling()


if __name__ == "__main__":
    main()
