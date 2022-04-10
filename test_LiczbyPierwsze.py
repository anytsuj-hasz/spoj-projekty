from unittest import TestCase

from LiczbyPierwsze import czy_pierwsza


class Test(TestCase):
    def test_czy_pierwsza(self):
        actual = czy_pierwsza(2)

        self.assertEqual(actual, True)
