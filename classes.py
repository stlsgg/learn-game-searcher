"""
game class placed here!
"""

class Game:
    """game object with all information."""
    id: int
    name: str
    price: float
    description: str
    genre: str
    categories: str
    hardware_requirements: str
    released_at: datetime
    embedding: Vector

    def __init__(self):
        # TODO
        pass


class GameTable:
    """game table contains all games."""

    def create(game: Game):
        """add new game to the database."""
        # TODO
        pass

    def update(game: Game):
        """partial or full game update in the database."""
        pass

    def delete(game_id: int):
        """delete game from the database by specified id."""
        pass

    def get():
        """retrieve game or games from database by search filters."""
        pass


class Embedder:
    """class for creating embeddings."""
    pass
