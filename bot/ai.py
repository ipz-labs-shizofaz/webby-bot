from groq import AsyncGroq

from bot import config

client = AsyncGroq(api_key=config.GROQ_API_KEY)


async def ask_ai(prompt: str) -> str:
    response = await client.chat.completions.create(
        model=config.GROQ_MODEL,
        messages=[
            {"role": "system", "content": config.AI_SYSTEM_PROMPT},
            {"role": "user", "content": prompt},
        ],
    )
    return response.choices[0].message.content
