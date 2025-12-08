from django import template

register = template.Library()

@register.filter
def uppercase_first(value):
    """Converts the first character of a string to uppercase."""
    if not value:
        return value
    return value[0].upper() + value[1:]

@register.filter(name="addPrefix")
def add_prefix(value, prefix):
    """Adds a prefix to a string."""
    return f"{prefix}{value}"

# second method to register custom filter
# register.filter('addPrefix',add_prefix)