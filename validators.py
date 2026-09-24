import re


def is_valid_email(email):
    """Return True if email looks like name@site.com, otherwise False."""
    if not isinstance(email, str):
        return False
    return re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", email) is not None


def is_strong_password(password):
    """Return True if password has 8+ characters, an uppercase letter,
    a lowercase letter and a digit. Otherwise False."""
    if not isinstance(password, str):
        return False
    return (
        len(password) >= 8
        and any(c.isupper() for c in password)
        and any(c.islower() for c in password)
        and any(c.isdigit() for c in password)
    )


def is_valid_age(age):
    """Return True if age is a whole number from 0 to 120, otherwise False."""
    if isinstance(age, bool) or not isinstance(age, int):
        return False
    return 0 <= age <= 120