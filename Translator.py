# --------------------------------------------TRANSLATOR PROJECT-------------------------------------------------------#

# Import related libraries in this project
from typing import Callable
import translators as ts


# --------------------------Second part of project : Translate decorator with parameters-------------------------------#

# Define a decorator function
def prefix_translator(**kwargs):
    def second_translator(func: Callable[[str], str]) -> Callable:
        def inner(argument):
            translated_text = getattr(ts, kwargs['provider'])(func(argument), from_language=kwargs['from_language'],
                                                              to_language=kwargs['to_language'])
            return translated_text

        return inner

    return second_translator


# Define a function with it's decorator for translating from English to persian
@prefix_translator(provider='google', from_language='auto', to_language='fa')
def second_original_text(text: str) -> str:
    return text


# Example for Second part of project
test_text = "apple"
print("Original text(English):\n{}\n\nTranslated text(Persian):\n{}".format(test_text, second_original_text(test_text)))


# --------------------------Third part of project : TTranslate decorator class-----------------------------------------#

# First class for translate decorator with no parameter

class ThirdTranslator1:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        translated_text = ts.google(self.function(*args, **kwargs), to_language='fa')
        return translated_text


# Define a function with it's decorator for translating from English to persian
@ThirdTranslator1
def third_first_original_text(text: str) -> str:
    return text


# Example for first part of project
test_text = "apple cat"
print("Original text(English):\n{}\n\nTranslated text(Persian):\n{}".format(test_text, third_first_original_text(test_text)))


