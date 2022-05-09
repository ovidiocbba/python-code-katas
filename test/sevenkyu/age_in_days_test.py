from datetime import date, timedelta

import codewars_test as test

from sevenkyu.age_in_days import age_in_days


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basics():
        today = date.today()

        bday = today - timedelta(days=2)
        test.assert_equals(age_in_days(bday.year, bday.month, bday.day), 'You are 2 days old')

        bday = today - timedelta(days=365)
        test.assert_equals(age_in_days(bday.year, bday.month, bday.day), 'You are 365 days old')
