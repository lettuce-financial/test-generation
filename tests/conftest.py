from inspect import Parameter, Signature
from pathlib import Path

from pytest import Collector, Module, Function
from .protocols import Repository, Model
from .base import validate_repo


pytest_plugins = ["tests.fixtures"]


class RepoCollector(Module):

    def __init__(self, *args, prefix: str, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.prefix = prefix

    def collect(self):
        # We generate our own test functions that map specific fixture names to general ones.
        #
        # In this case, we create a wrapper around `validate_repo` with foo/bar inputs.
        #
        # The usual fixture system will detect this inputs; as long as they follow a naming convention,
        # can call a generalized test function.

        signature = Signature(
            parameters=[
                Parameter(
                    name=f"{self.prefix}_repository",
                    annotation=Repository,
                    kind=Parameter.KEYWORD_ONLY,
                ),
                Parameter(
                    name=self.prefix,
                    annotation=Model,
                    kind=Parameter.KEYWORD_ONLY,
                ),
            ],
        )

        def wrapper(**kwargs):
            return validate_repo(
                repository=kwargs[f"{self.prefix}_repository"],
                model=kwargs[self.prefix],
            )

        wrapper.__name__ = "validate_repo"
        wrapper.__signature__ = signature

        yield Function.from_parent(self, name=f"validate_{self.prefix}_repo", callobj=wrapper)


def pytest_collect_file(file_path: Path, path: str, parent: Collector) -> Collector | None:
    # We use a file name convention to find all "repositories" and generate tests for them.
    if file_path.name.endswith("_repo.py"):
        prefix = file_path.name[:-8]
        return RepoCollector.from_parent(parent, name=file_path.name, path=file_path, prefix=prefix)

    return None
