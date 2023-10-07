from pytest import fixture

from .bar_repo import Bar, BarRepository
from .foo_repo import Foo, FooRepository


@fixture
def bar() -> Bar:
    return Bar()


@fixture
def bar_repository() -> BarRepository:
    return BarRepository()


@fixture
def foo() -> Foo:
    return Foo()


@fixture
def foo_repository() -> FooRepository:
    return FooRepository()
