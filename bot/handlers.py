import logging

from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from bot import config
from bot.ai import ask_ai
from bot.keyboards import (
    BACK_MENU,
    BTN_AI,
    BTN_BACK,
    BTN_CONTACTS,
    BTN_IT,
    BTN_STUDENT,
    MAIN_MENU,
)

logger = logging.getLogger(__name__)

TELEGRAM_MESSAGE_LIMIT = 4096


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the chat bot! Choose a command", reply_markup=MAIN_MENU
    )


async def student(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Student {config.STUDENT_NAME}, group {config.STUDENT_GROUP}", reply_markup=BACK_MENU
    )


async def it_technologies(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"IT technologies: {config.IT_TECHNOLOGIES}", reply_markup=BACK_MENU
    )


async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        f"Contacts\nphone: {config.CONTACT_PHONE}\ne-mail: {config.CONTACT_EMAIL}",
        reply_markup=BACK_MENU,
    )


async def prompt_ai(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Enter your prompt for the AI:", reply_markup=BACK_MENU)


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Main menu", reply_markup=MAIN_MENU)


async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
    try:
        answer = await ask_ai(update.message.text) or "The AI returned an empty response."
    except Exception:
        logger.exception("AI request failed")
        answer = "Failed to get a response from the AI. Please try again later."
    await update.message.reply_text(answer[:TELEGRAM_MESSAGE_LIMIT])


def register_handlers(app: Application) -> None:
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.Text([BTN_STUDENT]), student))
    app.add_handler(MessageHandler(filters.Text([BTN_IT]), it_technologies))
    app.add_handler(MessageHandler(filters.Text([BTN_CONTACTS]), contacts))
    app.add_handler(MessageHandler(filters.Text([BTN_AI]), prompt_ai))
    app.add_handler(MessageHandler(filters.Text([BTN_BACK]), back))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_reply))
