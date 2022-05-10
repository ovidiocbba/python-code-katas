import codewars_test as test

from sixkyu.determine_the_date_by_the_day_number import get_day


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(get_day(15, False), "January, 15")
        test.assert_equals(get_day(41, False), "February, 10")
        test.assert_equals(get_day(59, False), "February, 28")
        test.assert_equals(get_day(60, False), "March, 1")
        test.assert_equals(get_day(60, True), "February, 29")
