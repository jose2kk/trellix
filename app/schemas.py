"""Schemas."""

from pydantic import BaseModel, Field, validator


class GeneratePasswordPayload(BaseModel):
    length: int
    use_numbers: int = Field(default=0, alias="useNumbers")
    use_special_chars: int = Field(default=0, alias="useSpecialChars")
    use_capital_letters: int = Field(default=0, alias="useCapitalLetters")    
    password_hint: str = Field(alias="passwordHint")

    @validator("length")
    def is_valid_length(cls, val: int) -> int:
        if val > 5 and val < 17:
            return val
        raise ValueError("Length has to be a value between 6 and 16 inclusive.")
    
    @validator("use_numbers,use_special_chars,use_capital_letters")
    def is_valid_length(cls, val: int) -> int:
        if val == 0 or val == 1:
            return val
        raise ValueError("Value has to be either 0 or 1.")


class IsUniquePasswordPayload(BaseModel):
    password: str
    password_hint: str = Field(alias="passwordHint")
