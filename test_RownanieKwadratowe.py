from unittest import TestCase

from RownanieKwadratowe import ile_pierwiastkow_rzeczywistych


class Test(TestCase):
    def test_ile_pierwiastkow_rzeczywistych1(self):
        actual = ile_pierwiastkow_rzeczywistych(1, 2, 1)

        self.assertEqual(actual, 1)

    def test_ile_pierwiastkow_rzeczywistych2(self):
        actual = ile_pierwiastkow_rzeczywistych(1, 1, 1)

        self.assertEqual(actual, 0)
