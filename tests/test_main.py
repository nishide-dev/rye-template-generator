# external imports
import shutil
from pathlib import Path

import pytest

# internal imports
from config import Arguments
from src.main import main


@pytest.fixture()
def args() -> Arguments:
    return Arguments(
        name="test",
        template="torch",
        output=".",
    )


def test_main(args: Arguments) -> None:
    main(args)
    assert Path("test").exists()
    assert Path("test/pyproject.toml").exists()
    assert Path("test/README.md").exists()
    assert Path("test/.devcontainer/devcontainer.json").exists()

    # cleanup
    shutil.rmtree(Path("test"))
