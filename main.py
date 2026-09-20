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


@app.get("/game")
async def get_game():
    """retrieve games from library."""
    # TODO route accept query filters: /game?query_filters
    # TODO add query filters: limit, offset, genre, category, release_before,
    # release_after, price
    # TODO add /game/{id} for retrieving specific game from library by its id
    # TODO add /game/{id}?query_filters with basic filters:
    # - release_before and release_after: takes dd.mm.yyyy
    # - genre, category: takes string
    # - price: float with two positions in manticca (10, 2)
    # TODO find out: can we write multiple times to search query same field or
    # not, like https://foo.bar/?genre=roguelike&genre=smasher to combine
    # filters together?
    return {}


@app.post("/game/{id}")
async def change_game_info():
    """full or partial game information change."""
    # TODO return 200, object: new game
    # TODO fields which can be modified:
    # name, description, released_at, genre, categories, price,
    # hardware_requirements; if passed other fields - reject with 400.
    return {}


@app.post("/game")
async def add_new_game():
    """create new game and add it to library."""
    # TODO return custom code 201 on successful creation
    return {}


@app.delete("/game/{id}")
async def delete_game():
    """remove game from library completely."""
    # TODO custom http code 204 'no content' without return body
    return {}


@app.post("/game/{id}/embed")
async def create_embedding():
    """process game info into vectors and save it to game data."""
    # TODO return immediately to user, return 202 accepted
    # NOTE: process must go away from fastapi and should be handled in the
    # background
    return {}

# general TODO:
# TODO custom error handler for all wrong dto:
# { "status": "error", "message": "bad request" }
# TODO keep returning object shapes the same:
# { "status": "error|ok", "message": "string|{object with fields}"}
# TODO rate limiting with floating window 2 minutes, 25 requests max. for all
# routes - one user cannot make >25 requests per 2 minutes. for learning purpose
# only.
# NOTE: if you have idea what to add in routes, youre welcome to tell about it.

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
