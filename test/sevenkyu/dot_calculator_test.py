import codewars_test as test

from sevenkyu.dot_calculator import calculator


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(calculator("..... + ..............."), "....................")
        test.assert_equals(calculator("..... - ..."), "..")
        test.assert_equals(calculator("..... - ."), "....")
        test.assert_equals(calculator("..... * ..."), "...............")
        test.assert_equals(calculator("..... * .."), "..........")
        test.assert_equals(calculator("..... // .."), "..")
        test.assert_equals(calculator("..... // ."), ".....")
        test.assert_equals(calculator(". // .."), "")
        test.assert_equals(calculator(". - ."), "")
