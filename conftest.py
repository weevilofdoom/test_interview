import pytest
from typing import Generator, Tuple
from ddp.ddp import DDP


@pytest.fixture(scope="session")
def ddp(pytestconfig) -> Generator[DDP, None, None]:
    print("initializing setup...")
    ddp = DDP()
    yield ddp
    print("uninitializing setup...")