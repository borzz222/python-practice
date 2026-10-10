"""Конвертер чисел из арабских в римские и обратно."""

ROMAN_NUMERALS = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def to_roman(number):
    """Переводит арабское число в римское.

    Args:
        number: целое число от 1 до 3999.

    Returns:
        Строка с римским числом.
    """
    if not 1 <= number <= 3999:
        raise ValueError("Число должно быть от 1 до 3999.")

    result = ""
    for value, symbol in ROMAN_NUMERALS:
        while number >= value:
            result += symbol
            number -= value
    return result


def from_roman(roman):
    """Переводит римское число в арабское.

    Args:
        roman: строка с римским числом, например "XLII".

    Returns:
        Целое число.
    """
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = roman.upper()
    total = 0
    for i in range(len(roman)):
        current = values[roman[i]]
        if i + 1 < len(roman) and current < values[roman[i + 1]]:
            total -= current
        else:
            total += current
    return total


if __name__ == "__main__":
    roman_tests = ["IV", "IX", "XLII", "XCIX", "MMXXIII"]

    print("=== Римские → арабские ===")
    for roman in roman_tests:
        print(f"{roman} = {from_roman(roman)}")

    print("\n=== Арабские → римские ===")
    for number in [4, 9, 42, 99, 2023]:
        print(f"{number} = {to_roman(number)}")
