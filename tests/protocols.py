from typing import Protocol, TypeVar


class Model(Protocol):
    type: str


M = TypeVar("M", bound=Model)


class Repository(Protocol[M]):
    type: str
