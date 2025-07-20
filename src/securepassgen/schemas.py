from pydantic import BaseModel, Field


class PasswordsOption(BaseModel):
    length: int = Field(
        default=16, ge=8, le=128, description='Comprimento da senha.'
    )
    add_number: bool = True
    add_symbol: bool = True


class PasswordResponse(BaseModel):
    password_created: str
    parameter: PasswordsOption
