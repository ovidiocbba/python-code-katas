import codewars_test as test

from sevenkyu.case_swapping import swap


@test.describe("Case swapping")
def basic_tests():
    @test.it("Example tests")
    def basic_test_cases():
        test.assert_equals(swap('HelloWorld'), 'hELLOwORLD')
        test.assert_equals(swap('CodeWars'), 'cODEwARS')
