"""Генератор паролей с настройками через терминал."""

import random
import string


def generate_password(length, use_lower, use_upper, use_digits, use_special):
    """Возвращает случайный пароль по заданным настройкам.

    Args:
        length: длина пароля.
        use_lower: использовать строчные буквы.
        use_upper: использовать заглавные буквы.
        use_digits: использовать цифры.
        use_special: использовать спецсимволы.

    Returns:
        Сгенерированный пароль.
    """
    chars = ""
    if use_lower:
        chars += string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


def ask_yes_no(question):
    """Задаёт вопрос и возвращает True, если пользователь ответил «да».

    Args:
        question: текст вопроса.

    Returns:
        True для ответа «да», False для «нет».
    """
    while True:
        answer = input(f"{question} (да/нет): ").strip().lower()
        if answer in ("да", "д"):
            return True
        if answer in ("нет", "н"):
            return False
        print("Пожалуйста, ответьте «да» или «нет».")


def ask_length():
    """Запрашивает длину пароля, пока не будет введено положительное число.

    Returns:
        Длина пароля.
    """
    while True:
        answer = input("Длина пароля: ")
        if answer.isdigit() and int(answer) > 0:
            return int(answer)
        print("Введите целое положительное число.")


if __name__ == "__main__":
    print("=== Генератор паролей ===")
    length = ask_length()
    use_lower = ask_yes_no("Использовать строчные буквы?")
    use_upper = ask_yes_no("Использовать заглавные буквы?")
    use_digits = ask_yes_no("Использовать цифры?")
    use_special = ask_yes_no("Использовать спецсимволы?")

    if not (use_lower or use_upper or use_digits or use_special):
        print("Нужно выбрать хотя бы один тип символов.")
    else:
        password = generate_password(
            length, use_lower, use_upper, use_digits, use_special
        )
        print(f"\nВаш пароль: {password}")
