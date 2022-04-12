import unittest


_numbers = {
    0: 'Zero',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Fourty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety',
    100: 'Hundred',
    10**3: 'Thousand',
    10**6: 'Million',
    10**9: 'Billion',
    10**12: 'Trillion'
}


def english_int(n):
    '''
    16.8 English Int: Given any integer, print an English phrase that 
    describes the integer (e.g., "One Thousand, Two Hundred Thirty Four").
    '''
    if abs(n) > 10**15 - 1:
        raise ValueError(f'Number {n} is too large')

    if n == 0:
        return _numbers[0]

    is_negative = n < 0
    n = abs(n)

    result =  []
    divisor = 1000000000000

    while divisor > 0:
        m = n // divisor

        if m > 0:
            group = _convert_to_text(m)

            if divisor > 1:
                group.append(_numbers[divisor])

            result.append(group)

        n = n - m * divisor
        divisor //= 1000

    result = [' '.join(group) for group in result]
    result = ', '.join(result)

    if is_negative:
        result = 'Negative ' + result

    return result


def _convert_to_text(n):
    result = []

    hundreds = n // 100

    if hundreds > 0:
        result.append(_numbers[hundreds])
        result.append('Hundred')

    n %= 100

    if n == 0:
        pass
    elif 1 <= n and n <= 20:
        result.append(_numbers[n])
    else:
        ones = n % 10
        tens = n - ones
        result.append(_numbers[tens])

        if ones > 0:
            result.append(_numbers[ones])

    return result


class EnglishIntTest(unittest.TestCase):
    def test_english_int(self):
        test_cases = [
            (0, 'Zero'),
            (1, 'One'),
            (-1, 'Negative One'),
            (11, 'Eleven'),
            (20, 'Twenty'),
            (21, 'Twenty One'),
            (50, 'Fifty'),
            (51, 'Fifty One'),
            (100, 'One Hundred'),
            (108, 'One Hundred Eight'),
            (123, 'One Hundred Twenty Three'),
            (-123, 'Negative One Hundred Twenty Three'),
            (987, 'Nine Hundred Eighty Seven'),
            (1001, 'One Thousand, One'),
            (1234, 'One Thousand, Two Hundred Thirty Four'),
            (-1234, 'Negative One Thousand, Two Hundred Thirty Four'),
            (123456, 'One Hundred Twenty Three Thousand, Four Hundred Fifty Six'),
            (1234567, 'One Million, Two Hundred Thirty Four Thousand, Five Hundred Sixty Seven'),
            (123456789, 'One Hundred Twenty Three Million, Four Hundred Fifty Six Thousand, Seven Hundred Eighty Nine'),
            (1234567890, 'One Billion, Two Hundred Thirty Four Million, Five Hundred Sixty Seven Thousand, Eight Hundred Ninety'),
            (123456789123456, 'One Hundred Twenty Three Trillion, Four Hundred Fifty Six Billion, Seven Hundred Eighty Nine Million, One Hundred Twenty Three Thousand, Four Hundred Fifty Six')
        ]

        for n, expected in test_cases:
            actual = english_int(n)
            self.assertEqual(expected, actual)

        with self.assertRaises(ValueError):
            english_int(10**15)


if __name__ == '__main__':
    unittest.main()
