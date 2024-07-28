import re


def add_space_before_punctuation(text: str) -> str:
    """
    Adds a space before punctuation marks in the given text.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: The text with spaces added before punctuation marks.
    """
    pattern: str = r'([.,!?:;_])(?=\S)'
    replacement: str = r' \1 '
    return re.sub(pattern, replacement, text)


def remove_punctuation(text: str) -> str:
    """
    Removes all punctuation from the given text.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: The text with all punctuation removed.
    """
    pattern: str = r'[^\w\s]'
    return re.sub(pattern, '', text)


def remove_spaces(text: str) -> str:
    """
    Removes spaces before punctuation marks in the given text.

    Args:
        text (str): The input text to be processed.

    Returns:
        str: The text with spaces removed before punctuation marks.
    """
    pattern = r'\s+([,.:;!?_])'
    return re.sub(pattern, r'\1', text)


def censor_word(word: str) -> str:
    """
    Replaces the core text of the word with asterisks while retaining the original punctuation.

    Args:
        word (str): The input word to be censored.

    Returns:
        str: The censored word with asterisks replacing the core text.
    """
    core_text: str = remove_punctuation(word)
    censored_core: str = '*' * len(core_text)
    return word.replace(core_text, censored_core)


class Arms:
    """
    A class providing methods for text processing, particularly for replacing banned words.

    Methods:
        replace_ban_words(text: str, ban_words: dict[str, int]) -> str:
            Replaces banned words in the text with their censored versions.
    """
    @staticmethod
    def replace_ban_words(text: str, ban_words: dict[str, int]) -> str:
        """
        Replaces banned words in the text with their censored versions.

        Args:
            text (str): The input text to be processed.
            ban_words (dict[str, int]): A dictionary of banned words with their corresponding replacement values.

        Returns:
            str: The text with banned words replaced by their censored versions.
        """
        res: list[str] = []
        text = add_space_before_punctuation(text=text)
        for t in text.split():
            formatted_text: str = remove_punctuation(text=t)
            if ban_words.get(formatted_text.lower(), 0):
                res.append(censor_word(t))
            else:
                res.append(t)

        return remove_spaces(text=" ".join(res))
