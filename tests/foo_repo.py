from dataclasses import dataclass

from .protocols import Model, Repository


@dataclass
class Foo(Model):
    type: str = "foo"


@dataclass
class FooRepository(Repository[Foo]):
    type: str = "foo"
