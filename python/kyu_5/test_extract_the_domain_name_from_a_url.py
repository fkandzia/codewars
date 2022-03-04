import pytest

from python.kyu_5.extract_the_domain_name_from_a_url import domain_name, domain_name_2


class TestDomainName:
    @pytest.mark.parametrize(
        ("url", "domain"),
        [
            ("http://github.com/carbonfive/raygun", "github"),
            ("http://www.zombie-bites.com", "zombie-bites"),
            ("https://www.cnet.com", "cnet"),
            ("http://google.com", "google"),
            ("http://google.co.jp", "google"),
            ("https://youtube.com", "youtube"),
            ("www.xakep.ru", "xakep"),
            ("google.com", "google")
        ])
    def test_valid_url_should_return_domain_name(self, url, domain):
        assert domain_name(url) == domain

    def test_url_without_protocol_should_return_None(self):
        assert domain_name("Lorem ipsum") is None


class TestDomainName2:
    @pytest.mark.parametrize(
        ("url", "domain"),
        [
            ("http://github.com/carbonfive/raygun", "github"),
            ("http://www.zombie-bites.com", "zombie-bites"),
            ("https://www.cnet.com", "cnet"),
            ("http://google.com", "google"),
            ("http://google.co.jp", "google"),
            ("https://youtube.com", "youtube"),
            ("www.xakep.ru", "xakep"),
            ("google.com", "google")
        ])
    def test_valid_url_should_return_domain_name(self, url, domain):
        assert domain_name_2(url) == domain

    def test_url_without_protocol_should_return_None(self):
        assert domain_name_2("Lorem ipsum") is None



