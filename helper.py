"""
this code contains main logic. put here core tasks, functions and flows.
"""
import asyncpg
from embedding import embed

async def semantic_search(text: str, pool: asyncpg.Pool):
    """
    use embedding model to search through database games.
    """
    async with pool.acquire() as conn:
        emb = await embed(text)
        query = "SELECT id, name, description\
            FROM game\
            ORDER BY embedding <-> $1 LIMIT 5"
        rows = await conn.fetch(query, emb[0])
        return rows
