import codewars_test as test

from sevenkyu.computer_problem_series_1 import save


@test.describe("Computer problem series #1: Fill the Hard Disk Drive")
def basic_tests():
    @test.it("Calculate number of files")
    def basic_test_cases():
        test.assert_equals(save([4, 4, 4, 3, 3], 12), 3)
        test.assert_equals(save([4, 4, 4, 3, 3], 11), 2)
        test.assert_equals(save([4, 8, 15, 16, 23, 42], 108), 6)
        test.assert_equals(save([13], 13), 1)
        test.assert_equals(save([1, 2, 3, 4], 250), 4)
        test.assert_equals(save([100], 500), 1)
        test.assert_equals(save([11, 13, 15, 17, 19], 8), 0)
        test.assert_equals(save([45], 12), 0)
