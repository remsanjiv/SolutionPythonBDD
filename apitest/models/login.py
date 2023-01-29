from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Login:
    email: str
    password: str

    @staticmethod
    def from_dict(obj: Any) -> 'Login':
        assert isinstance(obj, dict)
        email = from_str(obj.get("email"))
        password = from_str(obj.get("password"))
        return Login(email, password)

    def to_dict(self) -> dict:
        result: dict = {}
        result["email"] = from_str(self.email)
        result["password"] = from_str(self.password)
        return result


def login_from_dict(s: Any) -> Login:
    return Login.from_dict(s)


def login_to_dict(x: Login) -> Any:
    return to_class(Login, x)


