import pytest

# Function to be tested
def sum(a, b):
    return a + b


# Tests
def test_sum_1():
    # inputs
    a = 1
    b = 2
    # expected result
    result = 3

    # make assert
    print(f"sum({a}+{b})={result}")
    assert sum(a, b) == result


def test_sum_2():
    a = 7 
    b = 2
    result = 9
    print(f"sum({a}+{b})={result}")
    assert sum(a, b) == result


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        pytest.param(1, 2, 3, id="TC00001_BF_f001"),
        pytest.param(3, 4, 7, id="TC00001_BF_f002"),
        pytest.param(5, 6, 11, id="TC00001_BF_f003"),
    ]
)
def test_name(a: int, b: int, expected_result: int) -> None:

    print(f"sum({a}+{b})={expected_result}")
    assert sum(a, b) == expected_result