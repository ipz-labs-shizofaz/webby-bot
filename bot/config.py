import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.environ["BOT_TOKEN"]

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
GROQ_MODEL = os.environ["GROQ_MODEL"]
AI_SYSTEM_PROMPT = os.environ["AI_SYSTEM_PROMPT"]

STUDENT_NAME = os.environ["STUDENT_NAME"]
STUDENT_GROUP = os.environ["STUDENT_GROUP"]
IT_TECHNOLOGIES = os.environ["IT_TECHNOLOGIES"]
CONTACT_PHONE = os.environ["CONTACT_PHONE"]
CONTACT_EMAIL = os.environ["CONTACT_EMAIL"]

WEBHOOK_URL = os.getenv("WEBHOOK_URL") or os.getenv("RENDER_EXTERNAL_URL")
WEBHOOK_PATH = os.environ["WEBHOOK_PATH"]
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET") or None
PORT = int(os.environ["PORT"])
