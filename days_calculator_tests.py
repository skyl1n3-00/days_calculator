from unittest import TestCase, main
from days_calculator import *
from custom_exceptions import *


class TestCases(TestCase):
    def test_valid_year(self):
        self.assertTrue(is_year_valid(2019))
        self.assertFalse(is_year_valid(219))
        with self.assertRaises(InvalidNumber):
            is_year_valid('NaN')

    def test_leap_year(self):
        self.assertTrue(is_year_leap(1992), 'Testing 1992')
        self.assertFalse(is_year_leap(1967), 'Testing 1967')
        with self.assertRaises(InvalidDateInput):
            is_year_leap(210)

    def test_get_number_of_days(self):
        self.assertEqual(get_number_of_days(1992, 2), 29, 'Year 1992')
        self.assertEqual(get_number_of_days(1993, 2), 28, 'Year 1993')
        self.assertEqual(get_number_of_days(2012, 12), 31, 'Year 2012')

    def test_is_month_valid(self):
        self.assertTrue(is_month_valid(2))
        self.assertFalse(is_month_valid(13))

    def test_is_day_valid(self):
        self.assertFalse(is_day_valid((31, 2, 2020)))
        self.assertFalse(is_day_valid((29, 2, 1993)))
        self.assertTrue(is_day_valid((1, 1, 2019)))

    def test_is_date_valid(self):
        self.assertTrue(is_date_valid((12, 12, 2012)))
        with self.assertRaises(InvalidDateInput):
            is_date_valid((12, 13, 2000))

    def test_compare_date(self):
        self.assertEqual(compare_date((12, 12, 2020), (12, 11, 2020)), 1)
        self.assertEqual(compare_date((12, 11, 2020), (12, 12, 2020)), -1)
        self.assertEqual(compare_date((1, 1, 2019), (1, 1, 2019)), 0)
        with self.assertRaises(InvalidDateInput):
            compare_date((33, 3, 2004), (12, 11, 2020))

    def test_number_days_between_two_months(self):
        self.assertEqual(number_days_between_two_months((12, 9, 2020), (19, 12, 2020)), 98)
        self.assertEqual(number_days_between_two_months((1, 1, 2017), (12, 4, 2017)), 101)

    def test_number_days_between_two_dates(self):
        self.assertEqual(number_days_between_two_dates((19, 7, 2011), (31, 12, 2015)), 1626)
        self.assertEqual(number_days_between_two_dates((1, 1, 1993), (31, 12, 1995)), 1094)
        self.assertEqual(number_days_between_two_dates((1, 1, 1993), (31, 12, 1994)), 729)


if __name__ == '__main__':
    main()
