import codewars_test as test

from sevenkyu.max_diff_easy import max_diff


@test.describe("Tests")
def basic_tests():
    @test.it("Basic tests")
    def basics():
        test.assert_equals(max_diff([0, 1, 2, 3, 4, 5, 6]), 6)
        test.assert_equals(max_diff([-0, 1, 2, -3, 4, 5, -6]), 11)
        test.assert_equals(max_diff([0, 1, 2, 3, 4, 5, 16]), 16)
        test.assert_equals(max_diff([16]), 0)
        test.assert_equals(max_diff([]), 0)
