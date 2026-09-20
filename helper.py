"""
this code contains main logic. put here core tasks, functions and flows.
"""
import asyncpg
from config import EMB_MODEL

async def semantic_search(text: str, pool: asyncpg.Pool, ai):
    """
    use embedding model to search through database games.
    """
    async with pool.acquire() as conn:
        # embed text from user
        res = ai.embeddings.create(
            model=EMB_MODEL,
            input=text,
        )

        # get related rows from db
        emb = str(res.data[0].embedding)
        query = "SELECT id, name, description\
            FROM game\
            ORDER BY embedding <-> $1 LIMIT 5"
        rows = await conn.fetch(query, emb)
        return rows
