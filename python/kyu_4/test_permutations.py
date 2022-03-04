from python.kyu_4.permutations import permutations


class TestPermutations:
    def test_single_letter_string_returns_expected_output(self):
        assert permutations('a') == ['a']

    def test_two_letter_string_returns_expected_output(self):
        assert sorted(permutations('ab')) == ['ab', 'ba']

    def test_four_letter_string_returns_expected_output(self):
        assert sorted(permutations('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

    def test_empy_string(self):
        assert sorted(permutations('')) == ['']