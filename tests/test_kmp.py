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
        (
            "Konstantynopolitanczykowianeczka",
            "tan",
            [4, 15],
        ),
        (
            "nam strzelac nie kazano - wstapilem na dzialo i spojrzalem na pole; 200 armiat grzmialo.",
            "rz",
            [6, 52, 80],
        ),
        (
            "AAAAABAAABA",
            "AAA",
            [0, 1, 2, 6],
        ),
        (
            "ABABABCABABABCABAB",
            "ABAB",
            [0, 2, 7, 9, 14],
        ),
        (
            "AAAAAAA",
            "AA",
            [0, 1, 2, 3, 4, 5],
        ),
        (
            "ABABABABA",
            "AB",
            [0, 2, 4, 6],
        ),
        (
            "SHORT",
            "LONGPATTERN",
            [],
        ),
        (
            "SENTINO SENTINO SENTINO SENTINO SENTINO SENTINO SENTINO SENTINO SENTINO SENTINO",
            "SENTINO",
            [0, 8, 16, 24, 32, 40, 48, 56, 64, 72],
        ),
        # TODO: Add more test cases
    ],
)
def test_kmp(text, pattern, expected):
    kmp = KMP(text)
    result = kmp.KMP_search(pattern)
    assert result == expected
