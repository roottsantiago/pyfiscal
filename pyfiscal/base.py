# -*- coding: utf-8 -*-
"""
Script manages base classes for calculating fiscal data.
"""
import datetime
import unicodedata

from .utils import (
    to_upper,
    search_vowel,
    search_consonant
)
from .constants import ENTITIES, DISADVANTAGES_WORDS


class BaseGenerator:
    """
    Base Generator Class
    """
    full_name = None
    first_name_master = None
    last_name_master = None
    mothers_last_name_master = None
    state = None
    last_name = None
    mother_last_name = None
    complete_name = None

    def generate(self):
        """
        Generation method
        """
        raise NotImplementedError('No implement.')

    def parse(self, name, last_name,
              mother_last_name=None, state=None):
        """
        Method in charge of parsing data.
        """
        self.state = to_upper(state) if state else None

        if mother_last_name:
            mother_last_name = self.remove_accents(to_upper(mother_last_name))
            self.mothers_last_name_master = mother_last_name
            mother_last_name = self.remove_articles(mother_last_name)
            mother_last_name = self.remove_precisions(mother_last_name)
            self.mother_last_name = mother_last_name

        first_name = self.remove_accents(to_upper(name))
        self.first_name_master = first_name
        first_name = self.remove_names(first_name)
        first_name = self.remove_articles(first_name)
        first_name = self.remove_precisions(first_name)
        self.complete_name = first_name

        last_name = self.remove_accents(to_upper(last_name))
        self.last_name_master = last_name
        last_name = self.remove_articles(last_name)
        last_name = self.remove_precisions(last_name)
        self.last_name = last_name

        self.full_name = f'{self.last_name_master} '\
            f'{self.mothers_last_name_master} {self.first_name_master}'

    def data_fiscal(self, name, last_name,
                    mother_last_name, birth_date):
        """
        method tax data
        """
        birth_date = self.parse_date(birth_date)

        if len(last_name) == 1 or len(last_name) == 2:
            initials = self.initials_name_comp(name, last_name,
                                               mother_last_name)
        elif mother_last_name is None or mother_last_name == '':
            # Rule 7
            initials = self.initials_single_last_name(name, last_name)
        else:
            initials = self.initials_name(name,
                                          last_name, mother_last_name)
        # Rule 9
        full_name_initials = self.verify_initials(initials)
        return f'{full_name_initials}{birth_date}'

    def initials_name(self, first_name, last_name, mother_last_name):
        """Rule 1 - The key is integrated with the following data:

        1.- The first letter of the father's last name and
            the next first vowel of the same.
        2.- The first letter of the mother's last name.
        3.- The first letter of the name.
        """

        ini_last_name = last_name[0:1]
        last_name_vowel = search_vowel(last_name)
        ini_mothlast_name = self.get_ini_mothlast_name(mother_last_name)
        ini_first_name = first_name[0:1]

        # Rule 5
        # When the paternal or maternal surname are composed,
        # the first word that corresponds
        # to any of them will be taken for the classification.
        # Dolores San Martín Dávalos SADD-180812
        # Mario Sánchez de la Barquera Gómez SAGM-190224
        # Antonio Jiménez Ponce de León JIPA-170808

        initials = f'{ini_last_name}{last_name_vowel}'\
            f'{ini_mothlast_name}{ini_first_name}'
        return initials

    @staticmethod
    def remove_precisions(phrase):
        """ Rule 3 - When the initial letter of any of the surnames
        or first names is composed, only its initial will be noted.
        In Ch la C and in Ll la L.

        For example:
            Manuel Chávez González CAGM-240618
            Felipe Camargo Llamas CALF-450228
            Charles Kennedy Truman KETC-511012
        """
        letters = phrase[0:2]
        data = phrase[2:len(phrase)]

        if letters == 'CH':
            phrase = f'C{data}'
        elif letters == 'LL':
            phrase = f'L{data}'
        return phrase

    @staticmethod
    def remove_articles(phrase):
        """
        Replace all the occurrences of string in list.

        Rule 8 - When articles, prepositions, conjunctions or contractions
        appear in the name of natural persons, they will not be taken aselements
        of integration of the code, examples:
            Carmen de la Peña Ramírez PERC-631201
            Mario Sánchez de los Cobos SACM-701110
            Roberto González and Durán GODR-600101
            Juan del Valle Martínez VAMJ-691001
        """
        data = [
            'DE LA ',
            'DE LOS ',
            'DEL ', 'DE ',
            'LAS ',
            'LA ',
            'LOS ',
            'Y ',
            'MC ',
            'MAC ',
            'VON ',
            'VAN '
        ]
        # Iterate over the strings to be replaced
        for elem in data:
            # Check if string is in the main string
            if elem in phrase:
                # Replace the string
                phrase = phrase.replace(elem, '').strip()
        return phrase

    @staticmethod
    def remove_names(first_name):
        """ Rule 6 - When the name is composed, that is,
        it is made up of two or more words, the initial letter of the first
        will be taken for the conformation, provided it is not MARIA or JOSE
        given its frequent use, in which case the first letter will be
        taken of the second word.

        For example:
            Luz María Fernández Juárez FEJL-200205
            José Antonio Camargo Hernández CAHA-211218
            María Luisa Ramírez Sánchez RASL-251112
        """
        data = ['JOSE ', 'MARIA ']

        # Iterate over the strings to be replaced
        for item in data:
            # Check if string is in the main string
            if item in first_name:
                # Replace the string
                first_name = first_name.replace(item, '').strip()
        return first_name

    @staticmethod
    def get_ini_mothlast_name(mother_last_name):
        """
        The first letter of the mother's last name.
        """
        result = mother_last_name[0:1] if mother_last_name else ''
        return result

    def initials_name_comp(self, first_name, last_name, mother_last_name):
        """Rule 4 - In cases where the paternal surname of the natural person
        is made up of one or two letters, the password will be
        formed as follows:

            1.- The first letter of the paternal surname.
            2.- The first letter of the mother's last name.
            3.- The first and second letters of the name.

        For example:
            Alvaro de la O Lozano 	OLAL-401201
            Ernesto Ek Rivera 	ERER-071120
        """
        ini_last_name = last_name[0:1]
        ini_mthlast_name = self.get_ini_mothlast_name(mother_last_name)
        data = f"{ini_last_name}{ini_mthlast_name}{first_name[0:2]}"
        return data

    @staticmethod
    def initials_single_last_name(first_name, last_name):
        """Rule 7 - In the cases in which the natural person has only one
        surname, he will comply with the first and second letters of the
        paternal or maternal surname, as it appears on the birth certificate,
        plus the first and second letters of the name.

        For example:
        Juan Martínez MAJU-420116
        Gerarda Zafra ZAGE-251115
        """
        result = f'{last_name[0:2]}{first_name[0:2]}'
        return result

    @staticmethod
    def verify_initials(initials):
        """
        Rule 9 - When an inconvenient word appears from the four letters
        that make up the alphabetical expression, the last letter will be
        replaced by an "X".
        """
        words = dict((x, y) for x, y in DISADVANTAGES_WORDS)
        words = words.get(initials) if words.get(initials) else initials
        return words

    @staticmethod
    def remove_accents(text):
        """ Normalise (normalize) unicode data in Python
        to remove umlauts, accents etc.

        Rule 10 - When special characters appear as part of the name,
        paternal surname and maternal surname,
        they must be excluded for the calculation of the homonym
        and the verification digit.
        The characters will be interpreted, yes and only if,
        they are individually within the name, paternal surname
        and maternal surname.
        Examples:

        Roberto O’farril Carballo OACR-661121
        Rubén D’angelo Fargo DAFR-710108
        Luz Ma. Fernández Juárez FEJL-830120
        """
        try:
            text = unicode(text, 'utf-8')
        except (TypeError, NameError):
            pass
        text = unicodedata.normalize('NFD', text)
        text = text.encode('ascii', 'ignore')
        text = text.decode("utf-8")
        return str(text)

    @staticmethod
    def parse_date(birthdate):
        """Rule 2 - The taxpayer's date of birth will be noted below,
            in the following order:

        1. Year: The last two figures will be taken,
            writing them in Arabic numerals.
        2.- Month: The month of birth will be taken in its order number,
            in a calendar year, writing it with Arabic numbers.
        3.- Day: It will be written in Arabic numerals.

        Args:
            birthdate: The first parameter.

        Returns:
        As a result we will have the numerical expression: 070401
        """
        try:
            dtype = type(birthdate) if birthdate else None
            if dtype:
                if not (dtype is datetime.datetime or dtype is datetime.date):
                    birthdate = datetime.datetime.strptime(
                        birthdate,
                        '%d-%m-%Y'
                    ).date()
            else:
                birthdate = datetime.datetime.today()

            year = str(birthdate.year)
            year = year[2:4]
            # When in the year, month or day, of the date of birth,
            # only one figure appears, a ZERO will be put before it.
            month = str(birthdate.month).zfill(2)
            day = str(birthdate.day).zfill(2)
            return f'{year}{month}{day}'
        except Exception as exc:
            raise Exception(exc)

    @staticmethod
    def get_federative_entity(state: str):
        """
        Method get states
        """
        data = [value for key, value in ENTITIES.items() if key == state]
        status_code = data[0] if data else ''
        return status_code

    @staticmethod
    def get_consonant(word: str):
        """
        Method get consonant
        """
        return search_consonant(word)

    @staticmethod
    def get_year(str_date: str):
        """
        Get year of birth date.
        """
        try:
            date = (datetime.datetime.strptime(str_date, '%d-%m-%Y').date()
                    if str_date else datetime.datetime.today())
            return date.year
        except Exception as exc:
            raise Exception(exc)
