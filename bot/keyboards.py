from telegram import ReplyKeyboardMarkup

BTN_STUDENT = "Student"
BTN_IT = "IT technologies"
BTN_CONTACTS = "Contacts"
BTN_AI = "Prompt AI"
BTN_BACK = "Back"

MAIN_MENU = ReplyKeyboardMarkup(
    [[BTN_STUDENT], [BTN_IT], [BTN_CONTACTS], [BTN_AI]],
    resize_keyboard=True,
)

BACK_MENU = ReplyKeyboardMarkup([[BTN_BACK]], resize_keyboard=True)
