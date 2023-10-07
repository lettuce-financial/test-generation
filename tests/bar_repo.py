from dataclasses import dataclass

from .protocols import Model, Repository


@dataclass
class Bar(Model):
    type: str = "bar"


@dataclass
class BarRepository(Repository[Bar]):
    type: str = "bar"
