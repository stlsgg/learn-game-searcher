from config import *
from openai import OpenAI
from fastapi import FastAPI
from objects import Question

app = FastAPI()
ai = OpenAI(api_key=API_KEY, base_url=BASE_URL)
SYSTEM_PROMPT = """
youre helpful assistant. answer to user question shortly (up to three
sentences).
"""

@app.get("/healthcheck")
async def healthcheck():
    """simple http server live check."""
    return { "status": "ok" }


@app.post("/ask")
async def ask_ai(question: Question):
    """ask ai agent question, related to the app data."""
    res = ai.responses.create(
        model=MODEL,
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": question.text,
            },
        ],
        reasoning={
            "effort": "none",
        },
        max_output_tokens=200
    )
    print(f"usage:\ninput tokens {res.usage.input_tokens},\noutput tokens \
          {res.usage.output_tokens}\ntotal tokens {res.usage.total_tokens}")
    return res.output_text
