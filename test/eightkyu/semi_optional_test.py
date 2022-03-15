import codewars_test as test

from eightkyu.semi_optional import wrap


@test.describe("example")
def basic_tests():
    @test.it("fixed_test")
    def basic_test_case():
        res = wrap("my_test")
        test.assert_equals(res["value"], "my_test")
        test.assert_equals(wrap(343)["value"], 343)
        obj = {"test": "testy"}
        test.assert_equals(wrap(obj)["value"], obj)
