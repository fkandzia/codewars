import pytest

from python.kyu_4.strip_comments import solution


class TestStripComments:

    def test_single_line_with_one_marker(self):
        assert solution('Hello world ! foo bar', ['!']) == 'Hello world'

    def test_multiple_lines_with_one_marker(self):
        assert solution('Hello world ! foo bar\nHello again', ['!']) == 'Hello world\nHello again'

    def test_single_lines_with_multiple_markers(self):
        assert solution('Hello world #! foo bar', ['!','#']) == 'Hello world'

    def test_multiple_lines_with_multiple_markers(self):
        assert solution('Hello world @ foo \nHello again  #bar', ['@','#']) == 'Hello world\nHello again'

    def test_string_without_markers(self):
        assert solution('Hello world @ foo\nBla!blubb\#hihi', []) == 'Hello world @ foo\nBla!blubb\#hihi'

    @pytest.mark.parametrize(
        ('input_string', 'comment_char_list', 'result_string'),
        [
            ("apples, pears # and bananas\ngrapes\nbananas !apples",
             ["#", "!"],
             "apples, pears\ngrapes\nbananas"),
            ("a #b\nc\nd $e f g",
             ["#", "$"],
             "a\nc\nd"),
        ])
    def test_should_return_expected_result(self, input_string, comment_char_list, result_string):
        assert solution(input_string, comment_char_list) == result_string
