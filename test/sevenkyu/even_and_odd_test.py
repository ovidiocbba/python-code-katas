import codewars_test as test

from sevenkyu.even_and_odd import even_and_odd


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(even_and_odd(126453), (264, 153))
        test.assert_equals(even_and_odd(3012), (2, 31))
        test.assert_equals(even_and_odd(4628), (4628, 0))
