# -*- coding: utf-8 -*-
"""
Script manages constants
"""
VOWELS = ('A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú')


CONSONANTS = (
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
    'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'
)


DISADVANTAGES_WORDS = (
    ('BUEI', 'BUEX'), ('BUEY', 'BUEX'),
    ('CACA', 'CACX'), ('CACO', 'CACX'),
    ('CAGA', 'CAGX'), ('CAGO', 'CAGX'),
    ('CAKA', 'CAKX'), ('CAKO', 'CAKX'),
    ('COGE', 'COGX'), ('COJA', 'COJX'),
    ('COJE', 'COJX'), ('COJI', 'COJX'),
    ('COJO', 'COJX'), ('CULO', 'CULX'),
    ('FETO', 'FETX'), ('GUEY', 'GUEX'),
    ('JOTO', 'JOTX'), ('KACA', 'KACX'),
    ('KACO', 'KACX'), ('KAGA', 'KAGX'),
    ('KAGO', 'KAGX'), ('KOGE', 'KOGX'),
    ('KOJO', 'KOJX'), ('KAKA', 'KAKX'),
    ('KULO', 'KULX'), ('MAME', 'MAMX'),
    ('MAMO', 'MAMX'), ('MEAR', 'MEAX'),
    ('MEAS', 'MEAX'), ('MEON', 'MEOX'),
    ('MION', 'MIOX'), ('MOCO', 'MOCX'),
    ('MULA', 'MULX'), ('PEDA', 'PEDX'),
    ('PEDO', 'PEDX'), ('PENE', 'PENX'),
    ('PUTA', 'PUTX'), ('PUTO', 'PUTX'),
    ('QULO', 'QULX'), ('RATA', 'RATX'),
    ('RUIN', 'RUIX')
)

ENTITIES = {
    'AGUASCALIENTES': 'AS',
    'BAJA CALIFORNIA': 'BC',
    'BAJA CALIFORNIA SUR': 'BS',
    'CAMPECHE': 'CC',
    'CHIAPAS': 'CS',
    'CHIHUAHUA': 'CH',
    'COAHUILA': 'CL',
    'COLIMA': 'CM',
    'DISTRITO FEDERAL': 'DF',
    'DURANGO': 'DG',
    'GUANAJUATO': 'GT',
    'GUERRERO': 'GR',
    'HIDALGO': 'HG',
    'JALISCO': 'JC',
    'MEXICO': 'MC',
    'MICHOACAN': 'MN',
    'MORELOS': 'MS',
    'NAYARIT': 'NT',
    'NUEVO LEON': 'NL',
    'OAXACA': 'OC',
    'PUEBLA': 'PL',
    'QUERETARO': 'QT',
    'QUINTANA ROO': 'QR',
    'SAN LUIS POTOSI': 'SP',
    'SINALOA': 'SL',
    'SONORA': 'SR',
    'TABASCO': 'TC',
    'TAMAULIPAS': 'TS',
    'TLAXCALA': 'TL',
    'VERACRUZ': 'VZ',
    'YUCATÁN': 'YN',
    'ZACATECAS': 'ZS',
    'NACIDO EXTRANJERO': 'NE'
}

TABLE1 = (
    (' ', '00'), ('B', '12'), ('O', '26'),
    ('0', '00'), ('C', '13'), ('P', '27'),
    ('1', '01'), ('D', '14'), ('Q', '28'),
    ('2', '02'), ('E', '15'), ('R', '29'),
    ('3', '03'), ('F', '16'), ('S', '32'),
    ('4', '04'), ('G', '17'), ('T', '33'),
    ('5', '05'), ('H', '18'), ('U', '34'),
    ('6', '06'), ('I', '19'), ('V', '35'),
    ('7', '07'), ('J', '21'), ('W', '36'),
    ('8', '08'), ('K', '22'), ('X', '37'),
    ('9', '09'), ('L', '23'), ('Y', '38'),
    ('&', '10'), ('M', '24'), ('Z', '39'),
    ('A', '11'), ('N', '25'), ('Ñ', '40'),
)

TABLE2 = (
    (0, '1'), (17, 'I'),
    (1, '2'), (18, 'J'),
    (2, '3'), (19, 'K'),
    (3, '4'), (20, 'L'),
    (4, '5'), (21, 'M'),
    (5, '6'), (22, 'N'),
    (6, '7'), (23, 'P'),
    (7, '8'), (24, 'Q'),
    (8, '9'), (25, 'R'),
    (9, 'A'), (26, 'S'),
    (10, 'B'), (27, 'T'),
    (11, 'C'), (28, 'U'),
    (12, 'D'), (29, 'V'),
    (13, 'E'), (30, 'W'),
    (14, 'F'), (31, 'X'),
    (15, 'G'), (32, 'Y'),
    (16, 'H'), (33, 'Z')
)

TABLE3 = (
    ('0', '00'), ('D', '13'), ('P', '26'),
    ('1', '01'), ('E', '14'), ('Q', '27'),
    ('2', '02'), ('F', '15'), ('R', '28'),
    ('3', '03'), ('G', '16'), ('S', '29'),
    ('4', '04'), ('H', '17'), ('T', '30'),
    ('5', '05'), ('I', '18'), ('U', '31'),
    ('6', '06'), ('J', '19'), ('V', '32'),
    ('7', '07'), ('K', '20'), ('W', '33'),
    ('8', '08'), ('L', '21'), ('X', '34'),
    ('9', '09'), ('M', '22'), ('Y', '35'),
    ('A', '10'), ('N', '23'), ('Z', '36'),
    ('B', '11'), ('&', '24'), (' ', '37'),
    ('C', '12'), ('O', '25'), ('Ñ', '38')
)

CHECKERS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
    'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21,
    'M': 22, 'N': 23, 'Ñ': 24, 'O': 25, 'P': 26, 'Q': 27, 'R': 28,
    'S': 29, 'T': 30, 'U': 31, 'V': 32, 'W': 33, 'X': 34, 'Y': 35,
    'Z': 36
}