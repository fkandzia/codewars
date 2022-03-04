import pytest

from python.kyu_4.range_extraction import range_extraction


class TestRangeExtraction:

    def test_empty_input_returns_empty_string(self):
        assert range_extraction([]) == ''

    def test_single_element_list_returns_expected_output(self):
        assert range_extraction([1]) == '1'

    def test_pair_of_consecutive_numbers_returns_expected_output(self):
        assert range_extraction([1, 2]) == '1,2'

    def test_simple_range_returns_expected_output(self):
        assert range_extraction([1, 2, 3]) == '1-3'

    def test_negative_number_range_returns_expected_output(self):
        assert range_extraction([-4, -3, -2]) == '-4--2'

    def test_multiple_ranges_returns_expected_output(self):
        assert range_extraction([-7,-6,-5,-4, 1, 2, 3]) == '-7--4,1-3'

    @pytest.mark.parametrize(("numbers", "ranges"),
                            [(
                                [-99, -11, -10, -3, -2, -1, 0, 1, 2, 3, 6, 22],
                              '-99,-11,-10,-3-3,6,22'
                            ),
                            (
                                [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                                '-6,-3-1,3-5,7-11,14,15,17-20'
                            ),
                            (
                                [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20],
                                '-3--1,2,10,15,16,18-20'
                            )]
                            )
    def test_mix_of_single_numbers_and_elements_returns_expected_output(self, numbers, ranges):
        assert range_extraction(numbers) == ranges