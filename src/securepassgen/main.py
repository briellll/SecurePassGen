from fastapi import FastAPI

from .core import create_password
from .schemas import PasswordResponse, PasswordsOption

app = FastAPI()


@app.post('/gerar-senha', response_model=PasswordResponse, tags=['Senhas'])
def endpoint_create_password(option: PasswordsOption):
    password_result = create_password(option)

    return PasswordResponse(password_created=password_result, parameter=option)
