from .protocols import M, Repository


def validate_repo(repository: Repository[M], model: M) -> None:
    # We define a generalize test for a repository.
    assert repository.type == model.type
