import datetime as dt
from decimal import Decimal

DATE_FORMAT = '%Y-%m-%d'


def add(items, title, amount, expiration_date=None):
    if title not in items:
        items[title] = []
    if expiration_date is not None:
        expiration_date = dt.datetime.strptime(
            expiration_date, DATE_FORMAT
        ).date()
    items[title].append({'amount': amount, 'expiration_date': expiration_date})


def add_by_note(items, note):
    parts = note.split(' ')
    if len(parts[-1].split('-')) == 3:
        expiration_date = parts[-1]
        amount = Decimal(parts[-2])
        title = ' '.join(parts[:-2])
    else:
        expiration_date = None
        amount = Decimal(parts[-1])
        title = ' '.join(parts[:-1])
    add(items, title, amount, expiration_date)


def find(items, needle):
    result = []
    for title in items:
        if needle.lower() in title.lower():
            result.append(title)
    return result


def get_amount(items, needle):
    product_amount = Decimal('0')
    for title in find(items, needle):
        for part in items[title]:
            product_amount += part['amount']
    return product_amount


def get_expired(items, in_advance_days=0):
    result = []
    today = dt.date.today()
    for title, parts in items.items():
        amount = Decimal('0')
        for part in parts:
            expiration_date = part['expiration_date']
            if expiration_date is not None and (
                expiration_date <= today + dt.timedelta(days=in_advance_days)
            ):
                amount += part['amount']
        if amount > 0:
            result.append((title, amount))
    return result
