# python-practice

Практические задания по предмету «Программирование (повышенный уровень)», трек Python (ТОП-ИИ). УрФУ, ИРИТ-РТФ, ПИИ.

## Структура

| Папка | Лекция | Содержание |
|---|---|---|
| `01_python_basics` | 1. Основы Python | Задачи 1–6 |
| `02_workspace_setup` | 2. Настройка рабочего места | Виртуальное окружение, numpy, Git, PEP 8, тесты, шифр Цезаря |

## 02_workspace_setup

- `calculator/` — поэлементные операции над массивами numpy, функция `add_numbers` с docstring и тест на pytest
- `task1.py` — шифр Цезаря: шифрование и расшифровка, русский и английский языки, автоматическое определение языка

## Запуск

```
python -m venv .venv
.venv\Scripts\activate
pip install numpy pytest
python 02_workspace_setup/task1.py
pytest 02_workspace_setup/calculator
```
