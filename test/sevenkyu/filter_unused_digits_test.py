import codewars_test as test

from sevenkyu.filter_unused_digits import unused_digits


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(unused_digits(12, 34, 56, 78), "09")
        test.assert_equals(unused_digits(2015, 8, 26), "3479")
        test.assert_equals(unused_digits(276, 575), "013489")
        test.assert_equals(unused_digits(643), "0125789")
        test.assert_equals(unused_digits(864, 896, 744), "01235")
