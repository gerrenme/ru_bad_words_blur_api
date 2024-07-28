from fastapi import FastAPI
from pydantic import BaseModel

from arms import Arms
from db_connection import DBConnection

class TextRequest(BaseModel):
    """
    Pydantic model for handling text requests.

    Attributes:
        text (str): The text to be analyzed.
    """
    text: str


class Service:
    """
    A class to provide the FastAPI application and manage text analysis services.

    Attributes:
        app (FastAPI): The FastAPI application instance.
        arms (Arms): An instance of the Arms class for text processing.
        db_connection (DBConnection): An instance of the DBConnection class for database operations.
        ban_words (dict[str, int]): A dictionary of forbidden words with their corresponding replacement values.

    Methods:
        read_forbidden_words() -> dict[str, int]:
            Reads forbidden words from the database and returns them as a dictionary.
    """
    def __init__(self):
        """
        Initializes the Service with a FastAPI app, text processing, and database connection instances.
        """
        self.app: FastAPI = FastAPI()
        self.arms: Arms = Arms()
        self.db_connection: DBConnection = DBConnection()
        self.ban_words: dict[str, int] = self.read_forbidden_words()

        @self.app.post("/analyze_text")
        async def get_logs(request: TextRequest) -> str:
            """
            Analyzes the text from the request and replaces forbidden words.

            Args:
                request (TextRequest): The request containing the text to be analyzed.

            Returns:
                str: The analyzed text with forbidden words replaced.
            """
            return self.arms.replace_ban_words(text=request.text, ban_words=self.ban_words)


    def read_forbidden_words(self) -> dict[str, int]:
        """
        Reads forbidden words from the database and returns them as a dictionary.

        Returns:
            dict[str, int]: A dictionary of forbidden words with their corresponding replacement values.
        """
        forbid_words, col_names = self.db_connection.read_gigabuse_words()
        res: dict[str, int] = {t[0]: 1 for t in forbid_words}
        return res
