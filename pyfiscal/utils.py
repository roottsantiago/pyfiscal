# -*- coding: utf-8 -*-
"""
File manage utilities
"""
import datetime
from enum import Enum
from .constants import VOWELS, CONSONANTS


def get_current_year():
    """
    Get current year.
    """
    return datetime.datetime.now().year


def search_consonant(word: str) -> str:
    """
    Search and get consonant
    """
    consonant = ''
    data = word[1:len(word)] if word else None
    for item in data:
        if item == 'Ñ':
            consonant = 'X'
        elif get_consonant(item):
            consonant = item
            break
    return consonant


def get_consonant(param: str) -> bool:
    """
    Iterate list and get consonant.
    """
    exist = [True for cons in CONSONANTS if cons == param]
    data = exist[0] if exist else False
    return data


def search_vowel(last_name: str) -> str:
    """
    Search for paternal surname vowel.
    """
    size = len(last_name) - 1
    last_name = last_name[1:size]
    vowel = ''

    for vow in last_name:
        if get_vocal(vow):
            vowel = vow
            break
    return vowel


def get_vocal(param: str) -> bool:
    """
    Iterate list and get vowel
    """
    exist = [True for vowel in VOWELS if vowel == param]
    data = exist[0] if exist else False
    return data


def to_upper(data: str) -> str:
    """
    Convert text to uppercase.
    """
    return data.upper().strip()


class GenderEnum(Enum):
    """
    Gender Enum
    """
    HOMBRE = 'H'
    MUJER = 'M'
