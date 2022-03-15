import codewars_test as test

from eightkyu.usd_cny import usdcny


@test.describe("USD=>CNY")
def basic_tests():
    @test.it("Basic test case")
    def basic_test_cases():
        test.assert_equals(usdcny(15), "101.25 Chinese Yuan")
        test.assert_equals(usdcny(465), "3138.75 Chinese Yuan")
