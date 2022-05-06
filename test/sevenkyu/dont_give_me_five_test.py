import codewars_test as test

from sevenkyu.dont_give_me_five import dont_give_me_five


@test.describe("Tests")
def basic_tests():
    @test.it("Basic tests")
    def basics():
        test.assert_equals(dont_give_me_five(1, 9), 8)
        test.assert_equals(dont_give_me_five(4, 17), 12)
