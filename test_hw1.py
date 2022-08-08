import unittest

from hw1 import domain_name
from hw1 import int32_to_ip
from hw1 import zeros
from hw1 import bananas
from hw1 import count_find_num


class TestHomeWorkOneCases(unittest.TestCase):

    def test_finding_domain_name(self):
        self.assertEqual(domain_name("http://google.com"), "gogle")
        self.assertEqual(domain_name("http://google.co.jp"), "google")
        self.assertEqual(domain_name("www.xakep.ru"), "xakep")
        self.assertEqual(domain_name("https://youtube.com"), "youtube")
        self.assertEqual(domain_name("http://www.zombie-bites.com"), "zombie-bites")
        self.assertEqual(domain_name("http://github.com/carbonfive/raygun"), "github")

    def test_int32_to_ip_converter(self):
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(int32_to_ip(0), "0.0.0.0")
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")

    def test_trailing_zeros(self):
        self.assertEqual(zeros(0), 0)
        self.assertEqual(zeros(6), 1)
        self.assertEqual(zeros(30), 7)

    def test_those_bananas(self):
        self.assertEqual(bananas("banann"), set())
        self.assertEqual(bananas("banana"), {"banana"})
        self.assertEqual(bananas("bbananana"), {"b-an--ana", "-banana--", "-b--anana", "b-a--nana", "-banan--a",
                     "b-ana--na", "b---anana", "-bana--na", "-ba--nana", "b-anan--a",
                     "-ban--ana", "b-anana--"})
        self.assertEqual(bananas("bananaaa"), {"banan-a-", "banana--", "banan--a"})
        self.assertEqual(bananas("bananana"), {"ban--ana", "ba--nana", "bana--na", "b--anana", "banana--", "banan--a"})

    def test_count_find_num(self):
        self.assertEqual(count_find_num([2, 3], 200), [13, 192])
        self.assertEqual(count_find_num([2, 5], 200), [8, 200])
        self.assertEqual(count_find_num([2, 3, 5], 500), [12, 480])
        self.assertEqual(count_find_num([2, 3, 5], 1000), [19, 960])
        self.assertEqual(count_find_num([2, 3, 47], 200), [])


if __name__ == '__main__':
    unittest.main()
