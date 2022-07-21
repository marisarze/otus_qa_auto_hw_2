import pytest

@pytest.fixture
def arbitrary_class():
    class A: pass
    return A