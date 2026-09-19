"""
available tools for ai.
"""

# get games with specific genre
async def find_by_genre(genre: str, limit: int):
    pass


# recently released games
async def find_recent_releases(period: 1 | 2 | 3, limit: int):
    """
    period in months
    """
    pass


# games that costs less than specific price
async def find_by_price(price_less_than: float, limit: int):
    pass


# semantic search (powerful feature!)
# example: games that supports old pc hardware (semantic)
async def semantic_search(search: str):
    pass
