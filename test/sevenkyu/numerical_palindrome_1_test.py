import codewars_test as test

from sevenkyu.numerical_palindrome_1 import palindrome


@test.describe("Parts")
def basic_tests():
    @test.it("Basic tests")
    def basics():
        test.it("'1221' should return 'True'")
        test.assert_equals(palindrome(1221), True)

        test.it("'123322' should return 'False'")
        test.assert_equals(palindrome(123322), False)

        test.it("'ACCDDCCA' should return 'Not valid'")
        test.assert_equals(palindrome("ACCDDCCA"), "Not valid")

        test.it("'\"1221\"' should return 'Not valid'")
        test.assert_equals(palindrome("1221"), "Not valid")

        test.it("'-450' should return 'Not valid'")
        test.assert_equals(palindrome(-450), "Not valid")
