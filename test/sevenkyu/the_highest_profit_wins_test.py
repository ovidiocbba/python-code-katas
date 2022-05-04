import codewars_test as test

from sevenkyu.the_highest_profit_wins import min_max


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(min_max([1, 2, 3, 4, 5]), [1, 5])
        test.assert_equals(min_max([2334454, 5]), [5, 2334454])
