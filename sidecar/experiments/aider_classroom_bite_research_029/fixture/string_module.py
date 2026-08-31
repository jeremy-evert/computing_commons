"""Freshman-readable string module with several neighboring responsibilities."""


def join_words(words):
    return " ".join(words)


def word_count(text):
    return len(text.split())


def first_word(text):
    words = text.split()
    return words[0] if words else ""


def last_word(text):
    words = text.split()
    return words[-1] if words else ""


def has_word(text, word):
    return word in text.split()


def uppercase_words(words):
    return [word.upper() for word in words]
