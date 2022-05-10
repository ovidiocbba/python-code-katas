import codewars_test as test

from sixkyu.get_the_square_of_a_number import square


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(square(2), 4)
        test.assert_equals(square(3), 9)
        test.assert_equals(square(4), 16)
