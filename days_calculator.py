from custom_exceptions import InvalidDateInput, InvalidNumber


def is_year_valid(year):
    """
    Function to test if a given year is valid or not
    :param year: integer
    :return True/False
    """
    if type(year) == str:
        raise InvalidNumber('Year input is not a number')
    if not type(year) == int:
        raise InvalidNumber('Input is not an integer')
    return 1952 < year < 9999


def is_month_valid(month):
    """
    Function to test if a given month is valid or not
    :param month: integer
    :return True/False
    """
    if type(month) == str:
        raise InvalidNumber('Month input is not a number')
    if not type(month) == int:
        raise InvalidNumber('Input is not an integer')
    return 0 < month < 13


def is_day_valid(date):
    """
    Function to test if a given date has a valid day
    :param date: tuple (day, month, year)
    :return True/False
    """
    day, month, year = date
    if is_year_valid(year):
        return 0 < day <= get_number_of_days(year, month)


def is_year_leap(year):
    """
    Function to test if a given year is leap or not returns true or false
    :param year: year integer
    :return True/False
    """
    if not is_year_valid(year):
        raise InvalidDateInput('Invalid year')
    if year % 4 == 0 and not year % 100 == 0:
        return True
    if year % 400 == 0:
        return True
    else:
        return False


def is_date_valid(date):
    """
    Function test if a given date (tuple (day, month, year)) is a valid or not
    :param date: tuple (day, month, year)
    :return True/False
    """
    day, month, year = date
    if not is_year_valid(year):
        raise InvalidDateInput('Invalid year')
    elif not is_month_valid(month):
        raise InvalidDateInput('Invalid month')
    elif not is_day_valid(date):
        raise InvalidDateInput('Invalid day')
    return True


def get_number_of_days(year, month):
    """
    Function to to get the number of days of a given month
    :param year: the year of the month to get to know if the year is leap or not
    :param month: number of the month from 1 to 12
    :return: number of the days (integer)
    """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        days[1] = 29
    return days[month - 1]


def compare_date(date_1, date_2):
    """
    Function to compare two given dates
    :param date_1: tuple contains the first date (day, month, year)
    :param date_2: tuple contains the second date (day, month, year)
    :return: 1 if the first date is greater than the second or -1 if the opposite,
        and 0 if they're equal.
    """
    year_1, month_1, day_1 = date_1
    year_2, month_2, day_2 = date_2

    if not is_date_valid(date_1):
        return

    if not is_date_valid(date_2):
        return

    def compare_integers(first_integer, second_integer):
        """
        Function to compare to given integers
        :param first_integer: integer
        :param second_integer: integer
        :return: 1 if the first param is greater than the second or -1 if the opposite,
        and 0 if they're equal.
        """
        if first_integer > second_integer:
            return 1
        elif first_integer < second_integer:
            return -1

        return 0

    if compare_integers(year_1, year_2) == 0:
        if compare_integers(month_1, month_2) == 0:
            return compare_integers(day_1, day_2)
        else:
            return compare_integers(month_1, month_2)
    return compare_integers(year_1, year_2)


def number_of_days_to_complete_month(date):
    """
    Function to get how many days are left in a given month
    :param date: tuple contains the first date (day, month, year)
    :return: the number of days left (integer)
    """
    day, month, year = date

    return get_number_of_days(year, month) - day


def number_days_between_two_months(date_1, date_2):
    """
    Function to get the number of days between two months belonging to the same year
    :param date_1: tuple contains the first date (day, month, year)
    :param date_2: tuple contains the first date (day, month, year)
    :return: number of the days (integer)
    """
    day_1, month_1, year_1 = date_1
    day_2, month_2, _ = date_2
    # the variable sum is preceded with and underscore, because sum is a predefined word in python
    if month_2 - month_1 <= 0:
        return number_of_days_to_complete_month(date_1) + day_2
    _sum = number_of_days_to_complete_month(date_1) + day_2
    for number_days in range((month_1+1), month_2):
        _sum += get_number_of_days(year_1, number_days)

    return _sum


def number_days_between_two_dates(date_1, date_2):
    """
    Function to calculate the number of days between to given dates
    :param date_1: the first date tuple (day, month, year)
    :param date_2: the first date tuple (day, month, year)
    :return: the number of days (integer)
    """
    day_1, month_1, year_1 = date_1
    day_2, month_2, year_2 = date_2

    if not is_date_valid(date_1) or not is_date_valid(date_2):
        raise InvalidDateInput('Dates are invalid')

    comparison_result = compare_date(date_1, date_2)
    if comparison_result == 0:
        return 0
    elif comparison_result == 1:
        return number_days_between_two_dates(date_2, date_1) * (-1)

    number_of_days = number_days_between_two_months(date_1, date_2)
    if year_2 - year_1 > 1:
        for year in range(year_1, year_2):
            if is_year_leap(year):
                number_of_days += 366
            else:
                number_of_days += 365

    if (year_2 - year_1) == 1:
        if is_year_leap(year_1 + 1):
            number_of_days += 366
        else:
            number_of_days += 365

    return number_of_days


if __name__ == '__main__':
    pass
