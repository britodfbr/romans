import pytest

import roman_numeral


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('I', 1),
        ('MCDLV', 1455),
        ('iii', 3),
        ('cmlxxxvii', 987),
        ('mcmlxxviii', 1978),
        ('CMXCIV', 994),
        ('CMLXXXVII', 987),
        ('MCMLXXVIII', 1978),
    ],
)
def test_roman_to_arabic(entrance, expected):
    assert roman_numeral.roman_to_arabic(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('I', 1),
        ('CMDLV', 1455),
        ('iii', 3),
        ('cmlxxxvii', 987),
        ('mcmlxxviii', 1978),
        ('CMXCIV', 994),
        ('CMLXXXVII', 987),
        ('MCMLXXVIII', 1978),
    ],
)
def test_roman_to_int(entrance, expected):
    assert roman_numeral.roman_to_int(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('I', 1),
        ('CMDLV', 1455),
        ('iii', 3),
        ('cmlxxxvii', 987),
        ('mcmlxxviii', 1978),
        ('CMXCIV', 994),
        ('CMLXXXVII', 987),
        ('MCMLXXVIII', 1978),
    ],
)
def test_RomanNumerals_from_romam(entrance, expected):
    assert roman_numeral.RomanNumerals.from_roman(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'I'),
        (1455, 'MCDLV'),
        (3, 'III'),
        (994, 'CMXCIV'),
        (987, 'CMLXXXVII'),
        (1978, 'MCMLXXVIII'),
    ],
)
def test_transform_number_to_roman_numeral(entrance, expected):
    assert roman_numeral.transform_number_to_roman_numeral(
        entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        (1, 'I'),
        (1455, 'MCDLV'),
        (3, 'III'),
        (994, 'CMXCIV'),
        (987, 'CMLXXXVII'),
        (1978, 'MCMLXXVIII'),
    ],
)
def test_RomanNumerals_to_roman(entrance, expected):
    assert roman_numeral.RomanNumerals.to_roman(entrance) == expected


@pytest.mark.parametrize(
    'entrance expected'.split(),
    [
        ('I', 1),
        ('CMDLV', 1455),
        ('iii', 3),
        ('cmlxxxvii', 987),
        ('mcmlxxviii', 1978),
        ('CMXCIV', 994),
        ('CMLXXXVII', 987),
        ('MCMLXXVIII', 1978),
    ],
)
def test_transform_roman_numeral_to_number(entrance, expected):
    assert roman_numeral.transform_roman_numeral_to_number(
        entrance) == expected
