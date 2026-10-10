"""Шифр Цезаря на английском и русском языках."""
def encrypt(text, shift):
    """Возвращает зашифрованный текст
    Args:
        text: текст, который нужно зашифровать
        shift: сдвиг, который изменяет букву
    Returns:
        Зашифрованный текст"""
    alphabeten = "abcdefghijklmnopqrstuvwxyz"
    alphabetrus = "абвгдеёжзийклмнопрстуфхцчшщъиьэюя"
    alph1 = ""
    for sym in text:
        if sym.lower() in alphabeten:
            alphabet = alphabeten
        else:
            alphabet = alphabetrus
        if sym.isupper():
            alph1 += alphabet[(alphabet.find(sym.lower()) + shift) % len(alphabet)]
            alph1 = alph1[:-1] + alph1[-1].upper()
        elif alphabet.find(sym) == -1:
            alph1 += sym
        else:
            alph1 += alphabet[(alphabet.find(sym) + shift) % len(alphabet)]
    return alph1


def decrypt(text, shift):
    """Возвращает дешифрованный текст.
    Args:
        text: текст, который нужно дешифровать
        shift: сдвиг, который использовался при широфке исходного текста
    Returns:
        Дешифрованный текст"""
    return encrypt(text, -shift)