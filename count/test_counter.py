import unittest

from counter import count_vowels


class TestCountVowels(unittest.TestCase):
    def test_counting(self):
        testcases = [
            {"input": 'abce', "output": 2},
            {"input": 'bcdfg', "output": 0},
            {"input": 'Mateusz', "output": 3},
            {"input": 'Pawel', "output": 2},
            {"input": '1024', "output": 0},
            {"input": '!!$@#@', "output": 0},
        ]

        for testcase in testcases:
            input_text = testcase["input"]
            expected = testcase["output"]
            self.assertEqual(
                count_vowels(input_text),
                expected, "Expected '%s' to have %d vowels" % (input_text, expected)
            )


if __name__ == '__main__':
    unittest.main()
