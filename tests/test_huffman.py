import pytest
from utils.huffman import HuffmanCoding


@pytest.mark.parametrize(
    "input_text, codes, encoded, decoded",
    [
        (
            "Ala ma kota a kot ma ale",
            {'m': '000', 't': '001', ' ': '01', 'a': '10', 'o': '1100', 'k': '1101', 'l': '1110', 'e': '11110', 'A': '11111'},
            "1111111101001000100111011100001100110011101110000101000100110111011110",
            "Ala ma kota a kot ma ale"
        ),
        # TODO: Add more test cases
    ],
)
def test_huffman(input_text, codes, encoded, decoded):
    text = input_text
    huffman = HuffmanCoding(text)
    assert codes == huffman.codes
    assert encoded == huffman.encode_text()
    assert decoded == huffman.decode_text(huffman.encode_text())
