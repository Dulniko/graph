import pytest
from utils.kmp import KMP


@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        (
            "Ala ma kota a kot ma ale",
            "kot",
            [7, 14],
        ),
        # TODO: Add more test cases
    ],
)
def test_kmp(text, pattern, expected):
    kmp = KMP(text)
    result = kmp.KMP_search(pattern)
    assert result == expected
