# Task
# 1. Create a ReST-API for generating password and keep a track of the generated passwords, based on the user requirements.
# 2. The app will have 2 endpoints,
#   A. GetPassword (Generate a new password)
#    Payload:'{"lenght":<int>[6,16],\n "useSpecialChars":<int>[0,1],\n "useNumbers":<int>[0,1],\n "useCapitalLetters":<int>[0,1],\n "passwordHint":<string>}'
#   B. IsUniquePassword (Is the given password unique)
#    Payload:'{"password":<string>, "passwordHint":<string>}'
 
# Requirements for the ReST-API.
# 1. Use any of the tools (FastAPI, Flask or Django)
# 2. Use data validation modules such as (Pydantic, dataclasses, atters etc....)
# 3. Store the generated password locally.
# 4. Check the local collection against the given password.
# 5. Use class based approach instead of simple functions.
# 6. Use decorators when possible.
 
 
# Share the code at the end of the interview.

from fastapi import FastAPI

import repository
import schemas
import service

app = FastAPI()


@app.post("/password")
def generate_password(payload: schemas.GeneratePasswordPayload):
    password = service.PasswordService.generate_password(
        length=payload.length,
        use_capital_letters=payload.use_capital_letters,
        use_numbers=payload.use_numbers,
        use_special_chars=payload.use_special_chars,
        password_hint=payload.password_hint,
        repository=repository.repository,
    )
    return {
        "password": password,
    }


@app.post("/check_password")
def check_password(payload: schemas.IsUniquePasswordPayload):
    ...
