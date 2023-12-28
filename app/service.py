"""Service."""

import repository


class PasswordService:

    @classmethod
    def generate_password(
        cls,
        length: int,
        use_special_chars: int,
        use_numbers: int,
        use_capital_letters: int,
        password_hint: str,
        repository: repository.BaseRepository,
    ) -> str:
        password = ""
        if use_special_chars:
            password += "$"
        if use_numbers:
            password += "1"
        if use_capital_letters:
            password += "A"
        remainming_lentgh = length - len(password)
        password += "b" * remainming_lentgh
        repository.create_element(password=password, password_hint=password_hint)
        return password

    @classmethod
    def is_unique_password(
        cls,
        password: str,
        password_hint: str,
        repository: repository.BaseRepository,
    ) -> bool:
        if repository.get_element(password=password):
            return True
        return False
