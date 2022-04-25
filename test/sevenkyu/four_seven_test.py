import codewars_test as test

from sevenkyu.four_seven import solution


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(solution(7), 4)
        test.assert_equals(solution(4), 7)
