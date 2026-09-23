"""
this script is used for creating embeddings from data in the database.
"""

# retrieve rows from db
# create text string for each row
# keep ids for updates
# use embedding model for generating 2000 dim vectors
# NOTE: 2000 because of this - https://github.com/pgvector/pgvector#hnsw
# NEW NOTE: 2048 because i don't care about first note.

import asyncio
import asyncpg
from openai import OpenAI
from config import *
from pgvector import Vector


async def embed(text: str):
    """
    take string and convert to embedding data with ai model.
    """
    ai = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    res = ai.embeddings.create(model=EMB_MODEL, input=text)
    return [Vector(d.embedding) for d in res.data]


async def make_embedding(game_id: int, pool):
    """
    full process of game description embedding: fetch data, embed and update
    vector.
    """
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            "SELECT id, description from game WHERE id = $1",
            game_id
        )
        if not row:
            return

        vec = await embed(row['description'])

        await conn.execute(
            'UPDATE game SET embedding = ($1) WHERE ID = $2',
            vec[0],
            game_id
        )
        print(f"embedding for game with {game_id} done")
