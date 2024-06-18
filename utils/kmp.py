import re


class KMP:
    def __init__(self, text):
        """Initializes the KMP instance with the given text.

        Args:
            text (str): The text in which pattern searching will be performed.
        """
        self.text = text

    def KMP_search(self, pattern):
        """Performs the KMP search algorithm to find the given pattern in the text.

        Returns a list of indexes of found patterns in text.
        """
        prefix = [0] * len(pattern)
        j = 0

        for i in range(1, len(pattern)):
            while j > 0 and pattern[j] != pattern[i]:
                j = prefix[j - 1]
            if pattern[j] == pattern[i]:
                j += 1
            prefix[i] = j

        result = []
        j = 0

        for i in range(len(self.text)):
            while j > 0 and pattern[j] != self.text[i]:
                j = prefix[j - 1]
            if pattern[j] == self.text[i]:
                j += 1
            if j == len(pattern):
                result.append(i - j + 1)
                j = prefix[j - 1]

        return result

    def KMP_replace(self, pattern, replacement):
        """Replaces all occurrences of the pattern in the text with the replacement string.

        Args:
            pattern (str): The pattern to be replaced.
            replacement (str): The string to replace the pattern with.

        Returns:
            str: The modified text with replacements.
        """
        modified_text = re.sub(re.escape(pattern), replacement, self.text)
        return modified_text
