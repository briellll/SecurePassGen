import secrets
import string

from .schemas import PasswordsOption


def create_password(response_model: PasswordsOption):
    alfabeto = string.ascii_letters

    if response_model.add_number:
        alfabeto += string.digits

    if response_model.add_symbol:
        alfabeto += string.punctuation

    senha = ''.join(
        secrets.choice(alfabeto) for i in range(response_model.length)
    )

    return senha
