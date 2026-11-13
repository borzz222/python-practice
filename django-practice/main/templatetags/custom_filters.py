from django import template

register = template.Library()


@register.filter
def format_currency(value):
    """Форматирует число как цену: 1250 → 1 250 ₽."""
    return f"{value:,.0f}".replace(",", " ") + " ₽"