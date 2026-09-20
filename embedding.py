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

async def main():
    ai = OpenAI(api_key=API_KEY, base_url=BASE_URL)

    db = await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        host=DB_ADDR,
    )

    try:
        query = """
        SELECT id, name, description FROM game
        """

        rows = await db.fetch(query)

        texts = []
        ids = []
        for row in rows:
            ids.append(row['id'])
            texts.append(
                f"name: {row['name']}; description: {row['description']};"
            )

        res = ai.embeddings.create(model=EMB_MODEL, input=texts)
        vectors = [d.embedding for d in res.data]

        updates = list(zip(ids, [str(vec) for vec in vectors]))

        await db.executemany(
            'UPDATE game SET embedding = $2::vector WHERE id = $1',
            updates,
        )

    finally:
        await db.close()

asyncio.run(main())
