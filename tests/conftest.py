import random
from pathlib import Path

import pytest


@pytest.fixture
def failed_exit_code():
    return random.randint(1, 10)


@pytest.fixture
def package_path():
    return Path(".", "tests").resolve()


@pytest.fixture
def user_profile():
    return Path.home()
