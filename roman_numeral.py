class RomanNumerals:
    arabic = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman = {v: k for k, v in sorted(arabic.items())}

    @classmethod
    def to_roman(self, num: int) -> str:
        result = ''
        for i in self.arabic:
            while num >= i:
                num -= i
                result += self.arabic.get(i)
        return result

    @classmethod
    def from_roman(self, num: str) -> int:
        num = num.upper()
        result = 0
        for i in range(len(num)):
            if i == 0 or self.roman.get(num[i]) <= self.roman.get(num[i - 1]):
                result += self.roman.get(num[i])
            else:
                result += self.roman.get(
                    num[i]) - 2 * self.roman.get(num[i - 1])
        return result


def transform_roman_numeral_to_number(roman_numeral: str) -> int:
    roman_char_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    roman_numeral = roman_numeral.upper()
    res = 0
    for i in range(0, len(roman_numeral)):
        if i == 0 or roman_char_dict[roman_numeral[i]] <= roman_char_dict[
                roman_numeral[i - 1]]:
            res += roman_char_dict[roman_numeral[i]]
        else:
            res += roman_char_dict[
                roman_numeral[i]] - 2 * roman_char_dict[roman_numeral[i - 1]]
    return res


def transform_number_to_roman_numeral(number):
    roman_value_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_char_list = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"
    ]
    res = ''
    for i in range(len(roman_value_list)):
        while number >= roman_value_list[i]:
            number -= roman_value_list[i]
            res += roman_char_list[i]
    return res


def roman_to_int(input):
    """
     https://wiki.python.org.br/NumerosRomanos
    """
    if not isinstance(input, type("")):
        raise TypeError("expected string, got %s" % type(input))
    input = input.upper()
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            if i + 1 < len(input) and nums[input[i + 1]] > value:
                sum -= value
            else:
                sum += value
        except KeyError as err:
            raise ValueError('input is not a valid Roman numeral: {}',
                             input) from err
    return sum


def roman_to_arabic(num: str) -> int:
    """Roman to arabic."""
    print('start')
    romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    arabics = [1, 5, 10, 50, 100, 500, 1000]
    num = num.upper()
    result = 0
    print(f'{num=}')
    # result = arabics[romans.index(num[0])]
    for i in range(len(num)):
        value = arabics[romans.index(num[i])]
        if (
            i + 1 < len(num) and 
            value < arabics[romans.index(num[i + 1])]
        ):
            result -= value
        else:
            result += value
    print('end')
    return result
