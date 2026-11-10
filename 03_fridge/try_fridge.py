from decimal import Decimal
from fridge_by_myself import add, add_by_note, find, get_amount, get_expired
items = {}
add_by_note(items, 'Яйца 10 2026-11-15')
add_by_note(items, 'Яйца 20 2026-11-10')
add_by_note(items, 'Яйца гусиные 4 2026-11-11')
add_by_note(items, 'Вода 2.5')
add(items, 'Сыр', Decimal('0.5'), '2026-11-09')

print(items)
print(find(items, 'яйц'))
print(get_amount(items, 'яйц'))
print(get_expired(items))
print(get_expired(items, 2))